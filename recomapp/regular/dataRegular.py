# -*- coding: utf-8 -*-
# ========== 枚举数据类型
# 数据类型
import sys,json
from enum import Enum

# 第一维护表：枚举数据类型
dataType = Enum('dataType',('gender','age','height','weight','waistline',\
                            'education','marriage','occupation','surrounding','diastolic',\
                           'systolic','glucose','mouth','disable','smoke',\
                            'drink','diet','movement','treatment','heredopathia',\
                           'exposure','imageology','medicine'))

tagType = Enum('tagType',('gender','marriage','occupation','surrounding','education',
                          'mouth','disable','age','smoke','drink',
                          'diet','treatment','movement','BMI',
                          'BF','bloodpressure','bloodglucose','heredopathis',
                          'exposure','hypertensionclssify','imageology','medicine'))

# 第二维护表：标签-数据 & 数据-标签映射表 & 输出结果的映射
tag2data_reflect_dict = {  # 较差的：生活环境、口腔、吸烟、饮酒、饮食、运动、注意体重、体脂率
                           # 涉及即推荐：遗传病、暴露史
    
    tagType.gender:[[dataType.gender],
                    ["","男","女",]],             # 部分区分性别的疾病
    tagType.marriage:[[dataType.marriage],
                      ["","未婚","已婚","离异",]], # 基本无区别
    tagType.occupation:[[dataType.occupation],
                        ["","学生","工作",]],     # 关于工作职业、危险等级
    tagType.surrounding:[[dataType.surrounding],
                         ["","生活环境良好","生活环境一般","生活环境较差",]],  # 针对一般及以下
    tagType.education:[[dataType.education],
                       ["","本科及以上","高中","初中","小学","无教育经历",]], # 与教育频率与难易度有关
    
    tagType.mouth:[[dataType.mouth],
                   ["","口腔良好","口腔一般","口腔较差",]], # 针对一般以下
    tagType.disable:[[dataType.disable],
                     ["","无残疾","有残疾",]],   # 针对有残疾，建议区分种类
    tagType.age:[[dataType.age],
                 ["","婴幼儿","儿童","少年","青年","中年","老年",]],  # 区分年龄层
    tagType.smoke:[[dataType.smoke],
                   ["","不吸烟","吸烟","吸烟过度",]],                # 针对吸烟与过度
    tagType.drink:[[dataType.drink],
                   ["","不饮酒","饮酒","饮酒过度",]],                # 针对饮酒与过度
    
    tagType.diet:[[dataType.diet],
                  ["","饮食良好","饮食一般","饮食较差",]],            # 针对一般与较差
    tagType.treatment:[[dataType.treatment],
                      ["","无疾病","高血压","糖尿病",]],             # 特殊疾病的对待
    tagType.movement:[[dataType.movement],
                      ["","运动良好","运动一般","运动较差",]],        # 针对一般及以下
    tagType.BMI:[[dataType.height,dataType.weight],
                 ["","体重过轻","体重正常","体重过重","轻度肥胖","肥胖","重度肥胖",]], # 针对过轻或肥胖
    tagType.BF:[[dataType.gender,dataType.waistline,dataType.weight],
                ["","体脂率较低","体脂率正常","体脂率较高",]],   # 注意体脂率
    
    tagType.bloodpressure:[[dataType.diastolic,dataType.systolic],
                           ["","血压正常","血压较高","血压较低",]],  # 注意血压
    tagType.bloodglucose:[[dataType.glucose],
                          ["","血糖正常","血糖较高","血糖较低",]],   # 注意血糖
    tagType.heredopathis:[[dataType.heredopathia],
                          ["","无遗传病","有遗传病",]],            #  遗传病科普，涉及
    tagType.exposure:[[dataType.exposure],
                      ["","无暴露史","有暴露史",]],                # 科普，涉及即推荐
    
    tagType.hypertensionclssify:[[dataType.treatment,dataType.diastolic,dataType.systolic,dataType.heredopathia],
                                   ["","一级高血压","二级高血压","三级高血压",]],
                                   # 高血压防治的推荐频率、力度与方向
    tagType.imageology:[[dataType.imageology],
                        ["","影像无结果","有结果",]],  # 暂无
    tagType.medicine:[[dataType.medicine],
                      ["","无处方","有处方",]],  # 暂无，可能需要对应数据库？
}
data2tag_reflect_dict = {}
def tag2data_transform():
    for tag_type in tag2data_reflect_dict.keys():
        datalist = tag2data_reflect_dict[tag_type][0]
        for data_type in datalist:
            if data_type not in data2tag_reflect_dict.keys():
                data2tag_reflect_dict[data_type] = [tag_type]
            else:
                data2tag_reflect_dict[data_type].append(tag_type)
tag2data_transform()


