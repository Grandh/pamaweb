# -*- coding: utf-8 -*-
# ========== 枚举数据类型
# 数据类型
import sys,json
from enum import Enum

# 第一维护表：枚举数据类型
tagType = Enum('tagType',('gender','education','marriage','occupation','surrounding',\
                          'mouth','disable','age','pregnant','psychology',\
                          'BMI'  ,'BF'     ,'smoke','drink','diet',\
                          'movement','eye','skin','heart','kidney',\
                          'bloodpressure','bloodglucose','familydisease','exposure',\
                          'copd','diabetes','hypertension','hypertensionclassify','imageology','medicine',\
                          'stroke','hyperlipemia','lipid'))

# tagValue = {'gender':3,'education','marriage','occupation','surrounding',\
#                           'mouth','disable','age','pregnant','psychology',\
#                           'BMI'  ,'BF'     ,'smoke','drink','diet',\
#                           'movement','eye','skin','heart','kidney',\
#                           'bloodpressure','bloodglucose','familydisease','exposure',\
#                           'copd','diabetes','hypertensionclassify','imageology','medicine',\
#                           'stroke','hyperlipemia','lipid'}

dataType = Enum('dataType',('gender','age','height','waistline','weight','education',\
                            'marriage','occupation','surrounding','psychology','pregnant',\
                            'diastolic','systolic','lipidtc','lipidtg','lipidhdl','lipidldl','glucose',\
                            'mouth','eye','disable','skin','heart','kidney',\
                            'smoke','drink','diet','movement',\
                            'diabetes','copd','stroke','hyperlipemia','hypertension',\
                            'familydisease','exposure','imageology','medicine'))

# 第二维护表：标签-数据 & 数据-标签映射表 & 输出结果的映射
tag2data_reflect_dict = {  # 
                           # 较差的：生活环境、口腔、吸烟、饮酒、饮食、运动、注意体重、体脂率
                           # 涉及即推荐：遗传病、暴露史、残疾
    # 1:更新标签需要的数据 2:最后显示的标签 # 3:输入的数值
    tagType.gender:[[dataType.gender],
                    ["",u"男",u"女",],],             # 部分区分性别的疾病
    tagType.marriage:[[dataType.marriage],
                      ["",u"未婚",u"已婚",u"离异",],], # 暂时无区别
    tagType.education:[[dataType.education],
                       ["",u"本科及以上",u"高中或职高",u"初中",u"小学",u"无教育经历",],], # 与教育频率与难易度有关
    tagType.occupation:[[dataType.occupation],
                        ["",u"无危险工作",u"轻危工作",u"高危工作"],],     # 关于工作职业、危险等级（暂时只匹配特定对象）
    tagType.disable:[[dataType.disable],
                     ["",u"有残疾",]],            # 针对有残疾，建议区分种类

    tagType.age:[[dataType.age],
                 ["",u"婴幼儿",u"儿童",u"少年",u"青年",u"中年",u"老年",],
                 [0,3,7,14,45,60,200]],  # 区分年龄层
    tagType.smoke:[[dataType.smoke],
                   ["",u"吸烟",u"吸烟过度",],
                   [1,5,20],],      #吸烟单位：支                # 针对吸烟与过度
    tagType.drink:[[dataType.drink],
                   ["",u"饮酒",u"饮酒过度",],
                   [200,500,1000],],                # 针对饮酒与过度 饮酒单位：ml
    tagType.BMI:[[dataType.height,dataType.weight],
                 ["",u"体重过轻",u"体重正常",u"体重过重",u"轻度肥胖",u"肥胖",u"重度肥胖",],
                 []], # 针对过轻或肥胖
    tagType.BF:[[dataType.gender,dataType.age,dataType.height,dataType.weight],
                ["",u"体脂率较低",u"体脂率正常",u"体脂率较高",]],   # 注意体脂率
    
    tagType.bloodglucose:[[dataType.glucose],
                          ["",u"血糖正常",u"血糖较高",u"血糖较低",]],   # 注意血糖
    tagType.familydisease:[[dataType.familydisease],
                          ["",u"早发心血管家族史",u"家庭遗传糖尿病史"],],  

    tagType.imageology:[[dataType.imageology],
                        ["",u"左心室肥厚",]],  # 暂无-可能对应疾病

    tagType.medicine:[[dataType.medicine],
                      ["",u"利尿药",u"β受体拮抗剂","钙通道阻滞剂","血管紧张素",""]],  # 暂无，可能需要对应数据库？
    # 需要进行输入不同映射的标签
    tagType.surrounding:[[dataType.surrounding],
                         ["",u"生活环境良好",u"生活环境一般",u"生活环境较差",],
                         [u"良好",u"一般",u"较差"],],  # 针对一般及以下
    tagType.mouth:[[dataType.mouth],
                   ["",u"口腔良好",u"口腔一般",u"口腔较差",],
                   [u"良好",u"一般",u"较差"]], # 针对一般以下
    tagType.psychology:[[dataType.psychology,],
                    ["",u"心理紧张",u"精神焦虑",u"态度消极"],
                    [u"紧张",u"焦虑",u"消极"],],
    tagType.diet:[[dataType.diet],
                  ["",u"饮食良好",u"饮食一般",u"饮食较差",],
                  [u"良好",u"一般",u"较差"],],            # 针对一般与较差

    tagType.movement:[[dataType.movement],
                      ["",u"运动良好",u"运动一般",u"运动较差",],
                      [u"良好",u"一般",u"较差"],],        # 针对一般及以下
    tagType.exposure:[[dataType.exposure],
                      ["",u"有暴露史",],
                      [u"流行病区域",u"环境污染区域",],],                # 科普，涉及即推荐
    # 20171027 新增8个标签
    tagType.pregnant:[[dataType.pregnant,],
                    ["",u"孕早期",u"孕中期",u"孕晚期",u"待产"],
                    [0,12,27,40,42]],
    tagType.eye:[[dataType.eye,],
                ["",u"视网膜病变",u"晶状体异常",]],
    tagType.skin:[[dataType.skin,],
            ["",u"糖尿病足",u"慢性皮肤病",]],

    tagType.heart:[[dataType.heart,],
            ["",u"心脏病",u"血管病变",u"肺源性心脏病",u"心脏肿瘤",u"冠心病",u"风湿性心脏病",u"心肌病"]],
    tagType.kidney:[[dataType.kidney],
            ["",u"肾炎",u"肾功能不全",u"肾功能衰竭"]],
    tagType.copd:[[dataType.copd,],
            ["",u"慢阻肺"]],
    tagType.diabetes:[[dataType.diabetes,],
            ["",u"糖尿病"]],

    # 20171103 新增4个标签：stroke,hyperlipemia,hypertension,lipid
    tagType.stroke:[[dataType.stroke],
            ["",u"脑卒中"],],
    tagType.hyperlipemia:[[dataType.hyperlipemia],
            ["",u"高血脂"],],
    tagType.lipid:[[dataType.lipidtc,dataType.lipidtg,dataType.lipidhdl,dataType.lipidldl],
            ["",u"低血脂",u"血脂正常",u"高血脂"],],

    tagType.bloodpressure:[[dataType.diastolic,dataType.systolic],
                           ["",u"血压较低",u"血压正常",u"一级高血压",u"二级高血压",u"三级高血压"]],  # 注意血压
    tagType.hypertension:[[dataType.hypertension],
            ["",u"高血压"],],
    tagType.hypertensionclassify:[[dataType.diastolic,dataType.systolic], 
            ["",u"低危高血压",u"中危高血压",u"高危高血压",u"极高危高血压"]],
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


