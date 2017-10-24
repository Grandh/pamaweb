# -*- coding: utf-8 -*-
from dataRegular import *
from regularHub import *

def activeRegualrHub(dataList):
    
    if not dataList: return False
    
    # 标签更新过滤器
    all_tag_filter = []
    tag_numbers = len(tagType.__members__.keys())
    for i in range(0,tag_numbers): all_tag_filter.append(0)
    
    # 更新要获取的用户标签
    for data_type in dataList.keys():
        # -- 实际应用时加上字符转换
        real_data_type = dataType(int(data_type))
        if real_data_type in data2tag_reflect_dict.keys():
            for item in data2tag_reflect_dict[real_data_type]:
                all_tag_filter[item.value-1] += 1

        else:print str(data_type) + " not in the dataType?"
    
#     print all_tag_filter

    tagResultDict = {}
    # 抽象标签获取函数
    def getTagFilter(tag_type,func):
        if all_tag_filter[tag_type.value-1] == len(tag2data_reflect_dict[tag_type][0]):
            tagResultDict[tag_type.name] = func(dataList)

    # 进行标签更新过滤
    
    # =========== class 1 ===========
    # 1 性别 —— gender
    getTagFilter(tagType.gender,
                 genderReguler)
    # 2 教育程度 —— education
    getTagFilter(tagType.education,
                 educationRegular)
    # 婚姻状况 —— marriage
    getTagFilter(tagType.marriage,
                 marriageRegular)
    # 职业 —— occupation
    getTagFilter(tagType.occupation,
                 occupationRegular)
    # 生活环境 —— surrounding
    getTagFilter(tagType.surrounding,
                 surroundingRegular)
    # 口腔状况 —— mouth
    getTagFilter(tagType.mouth,
                 mouthRegular)
    # 身体缺陷 —— disable
    getTagFilter(tagType.disable,
                 disableRegular)
    # =========== class 2 ===========
    # 年龄 —— age 五级划分
    getTagFilter(tagType.age,
                 ageRegular)
    # 吸烟 —— smoke 量划分，以及吸烟历史记录？
    getTagFilter(tagType.smoke,
                 smokeRegular)
    # 饮酒 —— drink 量的划分，结合饮酒记录？
    getTagFilter(tagType.drink,
                 drinkRegular)
    # 运动 —— movement 运动的评估？
    getTagFilter(tagType.movement,
                 movementRegular)
    # BMI   weight/height^2 之后进行量划分
    getTagFilter(tagType.BMI,
                BMIRegular)
    # 体脂率 gender- waistline+weight 量的划分
    getTagFilter(tagType.BF,
                 BFRegular)
    ## 综合评估 BMI+体脂率 综合评估

    # 血压状况 diastolic,systolic量检测
    getTagFilter(tagType.bloodpressure,
                 bloodpressureReguler)
    # 血糖 glucose 量检测
    getTagFilter(tagType.bloodglucose,
                 bloodglucoseRegular)
    # 疾病 disease-诊断结果判别
    getTagFilter(tagType.treatment,
                 treatmentRegular)
    # 遗传病史 —— heredopathis 无、某些遗传疾病
    getTagFilter(tagType.heredopathis,
                 heredopathiaRegular)
    # 暴露史料 —— exposure
    getTagFilter(tagType.exposure,
                 exposureRegular)
    # =========== class 3 ===========

    # 高血压危险分层 —— 血压情况diastolic&systolic + 遗传病 + 检测记录

    # 影像诊断 —— imageology，CRF结构化文档处理-需要数据学习

    # 处方 —— medicine 药物编码与复合数据库
    print tagResultDict
    for key in tagResultDict.keys():
        tag_type = tagType[key]
        index = tagResultDict[key]
        try:
            tagResultDict[key] = tag2data_reflect_dict[tag_type][1][index]
        except Exception,e:
            print e
            tagResultDict[key] = ""

    print tagResultDict
    return tagResultDict