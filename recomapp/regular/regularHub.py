# -*- coding: utf-8 -*-
from dataRegular import *

# 辅助逻辑判断
def valueindictionary(datatuple,tag_type):

    try:
        taglist = tag2data_reflect_dict.get(tag_type)
        data_type = taglist[0][0]
        data = datatuple.get(data_type.value)
        if data in taglist[1]:return taglist[1].index(data)
        else:return 0
    except Exception,e:pass
    return 0

def valueingap(datatuple,tag_type):
    try:
        taglist = tag2data_reflect_dict[tag_type]
        data_type = taglist[0][0]
        data = float(datatuple.get(data_type.value))
        gaplist = taglist[2]
        for num in gaplist:
            if data < num: return gaplist.index(num)
    except Exception,e:pass
    return 0

def valueincustomgap(data,gaplist):
    try:
        for num in gaplist:
            if data < num:return gaplist.index(num)
    except Exception,e:pass
    return 0

# 字符检验
def valuecontainsth(data,word,n=1):
    if word in data:return n
    else:return 0
def valueequalsth(data,word,n=1):
    if data == word:return n
    else:return 0
    
# 检验数据是否存在，并转换类型
def turndata2float(data):
    try:
        float_data = float(data)
        return float_data
    except Exception,e:
        print False
## 规则函数集合，建议保留单个文件维护
# 部分规则缺少检验，可以添加
# ========== class 1 ============= 9
def genderReguler(datatuple): # 将数据封装为tuple形式，便于调用
    return valueindictionary(datatuple,tagType.gender)
def educationRegular(datatuple):
    return valueindictionary(datatuple,tagType.education)
def marriageRegular(datatuple):
    return valueindictionary(datatuple,tagType.marriage)
def occupationRegular(datatuple):
    return valueindictionary(datatuple,tagType.occupation)
def surroundingRegular(datatuple):
    return valueindictionary(datatuple,tagType.surrounding)

def mouthRegular(datatuple):
    return valueindictionary(datatuple,tagType.mouth)
def disableRegular(datatuple):
    return valueindictionary(datatuple,tagType.disable)
def movementRegular(datatuple):
    return valueindictionary(datatuple,tagType.movement)
def dietRegular(datatuple):
    return valueindictionary(datatuple,tagType.diet)
def treatmentRegular(datatuple):
    return valueindictionary(datatuple,tagType.treatment)

def heredopathiaRegular(datatuple):
    return valueindictionary(datatuple,tagType.heredopathia)
def psychologyRegular(datatuple):
    return valueindictionary(datatuple,tagType.psychology)
def eyeRegular(datatuple):
    return valueindictionary(datatuple,tagType.eye)
def skinRegular(datatuple):
    return valueindictionary(datatuple,tagType.skin)
def heartRegular(datatuple):
    return valueindictionary(datatuple,tagType.heart)

def kidneyRegular(datatuple):
    return valueindictionary(datatuple,tagType.kidney)
def codpRegular(datatuple):
    return valueindictionary(datatuple,tagType.copd)
def diabetesRegular(datatuple):
    return valueindictionary(datatuple,tagType.diabetes)
def exposureRegular(datatuple):
    return valueindictionary(datatuple,tagType.exposure)
# ========== class 2 ============= 5
def ageRegular(datatuple):
    return valueingap(datatuple,tagType.age)
def smokeRegular(datatuple):
    return valueingap(datatuple,tagType.smoke)
def drinkRegular(datatuple):
    return valueingap(datatuple,tagType.drink)
def pregnantRegular(datatuple):
    return valueingap(datatuple,tagType.pregnant)

# ========= 长期数据处理需要考虑 ========
def BMIRegular(datatuple): # body mess index
    
    height_data = turndata2float(datatuple.get(dataType.height.value))
    weight_data = turndata2float(datatuple.get(dataType.weight.value))
    print weight_data,height_data
    if not height_data :return 0
    if not weight_data :return 0
    # 计算BMI
    bmivalue = weight_data/(height_data**2)

    gap = [0,18,24,27,30,35]
    return valueincustomgap(bmivalue,gap)

def BFRegular(datatuple):

    age_data = turndata2float(datatuple.get(dataType.age.value))
    height_data = turndata2float(datatuple.get(dataType.height.value))
    weight_data = turndata2float(datatuple.get(dataType.weight.value))
    if not age_data:return 0
    if not height_data:return 0
    if not weight_data:return 0
    # 计算BMI
    bmivalue = weight_data/(height_data**2)
    print "bmivalue:"
    print bmivalue

    gender = genderReguler(datatuple) # 其他地方调用规则数据，记得输入为tuple或list的形式

    bfvalue = 0
    if gender == 1:
        bfvalue = 1.2*bmivalue + 0.23*age_data - 16.2
        gap = [0,15,18,100]
        print bfvalue
        return valueincustomgap(bfvalue,gap)
    elif gender == 2:
        bfvalue = 1.2*bmivalue + 0.23*age_data - 5.4
        gap = [0,25,28,100]
        return valueincustomgap(bfvalue,gap)
    else:
        return 0

def bloodpressureReguler(datatuple):
    
    diastolic_data = turndata2float(datatuple.get(dataType.diastolic.value))
    systolic_data  = turndata2float(datatuple.get(dataType.systolic.value))
    if not diastolic_data:return 0
    if not systolic_data :return 0

    if diastolic_data < systolic_data: return 0  #输入错误检测
    elif diastolic_data > 300 or systolic_data < 0:
        print "输入可能有误"
    if diastolic_data > 140 or systolic_data > 90:return 2
    elif diastolic_data < 90 or systolic_data <60:return 3
    elif diastolic_data <140 and systolic_data <90:return 1
    else:return 0

def bloodglucoseRegular(datatuple):
    
    glucose_data = turndata2float(datatuple.get(dataType.glucose.value))
    # 错误判断
    if glucose_data < 0: return 0
    if glucose_data < 3.9:return 3
    elif glucose_data > 6.1:return 2
    else:return 1

# ============ class 3 ===============
def hypertensionclassifyRegular(datatuple):
    return 0

def imageologyRegular(datatuple):
    data = datatuple[dataType.imageology.value]
    return 0

def medicineRegular(datatuple):
    data = datatuple[dataType.medicine.value]
    return 0

RegularHubList = [genderReguler,educationRegular,marriageRegular,occupationRegular,surroundingRegular,\
                 mouthRegular, disableRegular, ageRegular, pregnantRegular, psychologyRegular,\
                 BMIRegular, BFRegular, smokeRegular,drinkRegular,dietRegular,\
                 movementRegular,eyeRegular,skinRegular,heartRegular,kidneyRegular,\
                 bloodpressureReguler,bloodglucoseRegular,treatmentRegular,heredopathiaRegular,exposureRegular,\
                 codpRegular,diabetesRegular,hypertensionclassifyRegular,imageologyRegular,medicineRegular]