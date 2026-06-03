from pydantic import BaseModel 
#导入pydantic库中的BaseModel类，用于定义数据模型

class RecordRequest(BaseModel):
    word_id:int
    is_correct:bool
    #RecordRequest类继承自BaseModel，定义了一个数据模型，包含三个

class ProgressStats(BaseModel):
    total_words:int
    learned_count:int
    mastered_count:int
    review_count:int
    #ProgressStats类继承自BaseModel，定义了一个数据模型，包含五个整数类型的字段，用于统计用户的学习进度