import json
import os
from sqlmodel import Session
from app.db.session import engine
from app.models.word import Word

# 1. 读取 Oxford 5000 JSON 文件
json_path = os.path.join("..", "Oxford-5000-words-main", "full-word.json")
with open(json_path, encoding="utf-8") as f:
    data = json.load(f)

# 2. 等级映射
level_map = {
    "A1": 1,
    "A2": 2,
    "B1": 3,
    "B2": 4,
    "C1": 5,
}

words_to_insert = []
skipped = 0

for item in data:
    value = item.get("value")
    if not value:
        skipped += 1
        continue

    word_text = value.get("word", "").strip()
    if not word_text:
        skipped += 1
        continue

    # 排除明显不是英文单词的条目（例如短语、带空格的）
    if " " in word_text or "-" in word_text:
        skipped += 1
        continue

    level_str = value.get("level", "")
    difficulty = level_map.get(level_str, 1)  # 未知等级默认为1

    part_of_speech = value.get("type", "") or ""
    examples = value.get("examples", [])
    example_sentence = examples[0] if examples else ""

    # 中文暂时为空，后面可以批量翻译补充
    chinese = ""

    words_to_insert.append({
        "english": word_text,
        "chinese": chinese,
        "part_of_speech": part_of_speech,
        "example_sentence": example_sentence,
        "difficulty": difficulty,
    })

# 3. 批量写入数据库
with Session(engine) as session:
    for w in words_to_insert:
        word_obj = Word(**w)
        session.add(word_obj)
    session.commit()

print(f"✅ 成功导入 {len(words_to_insert)} 个单词！")
print(f"⏭️ 跳过 {skipped} 个非单词条目（短语、空词等）")