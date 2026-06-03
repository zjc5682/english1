from datetime import datetime, timezone, timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, func
from app.db.session import get_session
from app.models.word import Word
from app.models.progress import UserWordProgress
from app.schemas.progress import RecordRequest, ProgressStats
from app.api.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/learning",tags=["learning"])
#定义一个POST请求接口，路径为/record，用于记录用户学习单词的进度，响应数据格式为ProgressStats

@router.get("/next-word")
def get_next_word(
    current_user:User = Depends(get_current_user),
    session:Session = Depends(get_session)
):
    """返回当前用户下一个需要学习的单词"""
    #1.先找从未学习过的单词
    learned_word_ids = session.exec(
        #exec方法执行查询，返回一个结果集对象，all()方法将结果集转换为列表
        select(UserWordProgress.word_id)
        .where(UserWordProgress.user_id == current_user.id)
        #.where方法添加查询条件，过滤出当前用户的学习进度记录，获取已经学习过的单词ID列表
    ).all()

    if learned_word_ids:
        unlearned_word = session.exec(  
            select(Word)
            .where(~Word.id.in_(learned_word_ids))
            .order_by(Word.difficulty) #优先推送简单单词
        ).first() #获取第一个未学习过的单词
        if unlearned_word:
            return {
                "id":unlearned_word.id,
                "english":unlearned_word.english,
                "chinese": unlearned_word.chinese or "",
                "part_of_speech":unlearned_word.part_of_speech,
                "example_sentence":unlearned_word.example_sentence,
                "difficulty":unlearned_word.difficulty,
                "status":"new"
            }
    #2.已全部学过，返回需要复习的单词（按next——review时间排序，优先推送需要复习的单词）
    now =datetime.now(timezone.utc)
    review_word = session.exec(
        select(Word,UserWordProgress)
        .join(UserWordProgress,Word.id == UserWordProgress.word_id)
        .where(UserWordProgress.user_id == current_user.id)
        .where(UserWordProgress.next_review <= now)
        .order_by(UserWordProgress.next_review.asc())
        .limit(1)
    ).first()

    if review_word:
        word,progress = review_word
        return{
            "id":word.id,
            "english":word.english ,
            "chinese": word.chinese or "",
            "part_of_speech":word.part_of_speech,
            "example_sentence":word.example_sentence,
            "difficulty": word.difficulty,
            "status":"review",
            "correct_count":progress.correct_count,
            "incorrect_Count":progress.incorrect_count
        }
    
    #3.没有任何需要复习的单词，随机返回一共简单单词（可选）
    fallback_word = session.exec(
        select(Word).order_by(Word.difficulty).limit(1)
    ).first()
    if fallback_word:
        return {
            "id":fallback_word.id,
            "english":fallback_word.english,
            "chinese":fallback_word.chinese or "",
            "part_of_speech":fallback_word.part_of_speech,
            "example_Sentence":fallback_word.example_sentence,
            "difficulty":fallback_word.difficulty,
            "status":"review"
        }
    raise HTTPException(status_code=404,detail = "没有可用单词")

@router.post("/record")
def record_result(
    request:RecordRequest,
    current_user:User = Depends(get_current_user),
    session:Session = Depends(get_session)
):
    """记录学习结果"""
    #查找已有的学习记录
    progress = session.exec(
        select(UserWordProgress).where(
            UserWordProgress.user_id == current_user.id,
            UserWordProgress.word_id == request.word_id
        )
    ).first()

    if not progress:
        progress = UserWordProgress(
            user_id = current_user.id,
            word_id = request.word_id,
            level = 0
        )
        session.add(progress)

    # 更新统计和下次复习时间
    progress.study_count += 1
    progress.last_studied = datetime.now(timezone.utc)

    if request.is_correct:
        progress.correct_count += 1
        if progress.level < 3:
            progress.level += 1
        # 复习间隔递增（简单版间隔重复）
        days = [0, 1, 3, 7, 14][min(progress.level, 4)]
        progress.next_review = progress.last_studied + timedelta(days=days)
    else:
        progress.incorrect_count += 1
        if progress.level > 0:
            progress.level -= 1
        # 错误后缩短复习时间
        progress.next_review = progress.last_studied + timedelta(hours=2)

    session.commit()
    return {"status": "ok"}

@router.get("/stats", response_model=ProgressStats)
def get_stats(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """获取学习统计"""
    total_words = session.exec(select(func.count(Word.id))).one()
    learned_count = session.exec(
        select(func.count(UserWordProgress.id))
        .where(UserWordProgress.user_id == current_user.id)
    ).one()
    mastered_count = session.exec(
        select(func.count(UserWordProgress.id))
        .where(UserWordProgress.user_id == current_user.id)
        .where(UserWordProgress.level >= 2)
    ).one()
    review_count = session.exec(
        select(func.count(UserWordProgress.id))
        .where(UserWordProgress.user_id == current_user.id)
        .where(UserWordProgress.next_review <= datetime.now(timezone.utc))
    ).one()

    return {
        "total_words": total_words,
        "learned_count": learned_count,
        "mastered_count": mastered_count,
        "review_count": review_count
    }
