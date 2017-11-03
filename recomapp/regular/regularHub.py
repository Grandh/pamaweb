# -*- coding: utf-8 -*-
from dataRegular import *

# 辅助逻辑判断

DATA_TYPE_ORDER = 0
OUTPUT_TAG_ORDER = 1
INPUT_DATA_ORDER = 2
INPUT_GAP_ORDER = 2
def valueindictionary(datatuple,tag_type):

    try:
        taglist = tag2data_reflect_dict.get(tag_type)
        data_type = taglist[DATA_TYPE_ORDER][0] # 适用于只有一个数据输入类型的
        data = datatuple.get(data_type.value)
        if data in taglist[OUTPUT_TAG_ORDER]:return taglist[OUTPUT_TAG_ORDER].index(data)
        else:return 0
    except Exception,e:pass
    return 0

def valuereflectdictionary(datatuple,tag_type):
    try:
        taglist = tag2data_reflect_dict.get(tag_type)
        data_type = taglist[DATA_TYPE_ORDER][0] # 适用于只有一个数据输入类型的
        data = datatuple.get(data_type.value)
        if data in taglist[INPUT_DATA_ORDER]:return taglist[INPUT_DATA_ORDER].index(data)+1
        else:return 0
    except Exception,e:pass
    return 0

def valueingap(datatuple,tag_type):
    try:
        taglist = tag2data_reflect_dict[tag_type]
        data_type = taglist[DATA_TYPE_ORDER][0]
        data = float(datatuple.get(data_type.value))
        gaplist = taglist[INPUT_GAP_ORDER]
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
def disableRegular(datatuple):
    return valueindictionary(datatuple,tagType.disable)


def psychologyRegular(datatuple):
    return valueindictionary(datatuple,tagType.psychology)
def eyeRegular(datatuple):
    return valueindictionary(datatuple,tagType.eye)
def skinRegular(datatuple):
    return valueindictionary(datatuple,tagType.skin)
def heartRegular(datatuple):
    return valueindictionary(datatuple,tagType.heart)
def familydiseaseRegular(datatuple):
    return valueindictionary(datatuple,tagType.familydisease)

def kidneyRegular(datatuple):
    return valueindictionary(datatuple,tagType.kidney)
def codpRegular(datatuple):
    return valueindictionary(datatuple,tagType.copd)
def diabetesRegular(datatuple):
    return valueindictionary(datatuple,tagType.diabetes)
def strokeRegular(datatuple):
    return valueindictionary(datatuple,tagType.stroke)
def hyperlipemiaRegular(datatuple):
    return valueindictionary(datatuple,tagType.hyperlipemia)
def hypertensionRegular(datatuple):
    return valueindictionary(datatuple,tagType.hypertension)

# 需要对数据进行映射
def surroundingRegular(datatuple):
    return valuereflectdictionary(datatuple,tagType.surrounding)
def movementRegular(datatuple):
    return valuereflectdictionary(datatuple,tagType.movement)
def dietRegular(datatuple):
    return valuereflectdictionary(datatuple,tagType.diet)
def mouthRegular(datatuple):
    return valuereflectdictionary(datatuple,tagType.mouth)
def exposureRegular(datatuple):
    return valuereflectdictionary(datatuple,tagType.exposure)

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
    if diastolic_data >= 180 or systolic_data >= 110:return 5
    elif diastolic_data >= 160 or systolic_data >= 100:return 4
    elif diastolic_data >= 140 or systolic_data >= 90:return 3
    elif diastolic_data < 90 or systolic_data < 60:return 1
    elif diastolic_data < 140 and systolic_data < 90:return 2
    else:return 0

def bloodglucoseRegular(datatuple):
    
    glucose_data = turndata2float(datatuple.get(dataType.glucose.value))
    # 错误判断
    if glucose_data < 0: return 0
    if glucose_data < 3.9:return 3
    elif glucose_data > 6.1:return 2
    else:return 1
    
def lipidRegular(datatuple):
    
    tc_value = turndata2float(datatuple.get(dataType.lipidtc.value))
    tg_value = turndata2float(datatuple.get(dataType.lipidtg.value))
    hdl_value = turndata2float(datatuple.get(dataType.lipidhdl.value))
    ldl_value = turndata2float(datatuple.get(dataType.lipidldl.value))

    normalValue = 2
    tc_gap = [0,2.86,5.98,100]
    tc_value = valueincustomgap(tc_value,tc_gap)
    if tc_value != normalValue:return tc_value
    tg_gap = [0,0.22,1.7,100]
    tg_value = valueincustomgap(tg_value,tg_gap)
    if tg_value != normalValue: return tg_value
    hdl_gap = [0,0.90,2.19,100]
    hdl_value = valueincustomgap(hdl_value,hdl_value)
    if hdl_value != normalValue:return hdl_value
    ldl_gap = [0,0,3.12,100]
    ldl_value = valueincustomgap(ldl_value,ldl_gap)
    if ldl_value != normalValue:return ldl_value

    return normalValue


# ============ class 3 ===============
def hypertensionclassifyRegular(datatuple): #完成后记得更新Tag-data表

    if(hypertensionRegular(datatuple) != 1): return 0  #未诊断高血压，不进行危险分层

    # 危险分层在一定程度上，只是为了辅助高血压管理
    hazards = 0
    hypertension_class = 0  # 血压现状分级，默认为0

    bloodpressureState = bloodpressureReguler(datatuple)  # 若遗失血压数据如何处理？
    if(bloodpressureState > 2):
        hazards+=1
        hypertension_class = bloodpressureState - 3

    age_data = turndata2float(datatuple.get(dataType.age.value))
    # 性别与年龄因素
    if age_data:
        gender_data = valueindictionary(datatuple,tagType.gender)
        if gender_data == 1:
            if age_data > 55:hazards+=1
        elif gender_data == 2:
            if age_data > 65:hazards+=1
    # 是否吸烟
    if(smokeRegular(datatuple) >= 1):hazards += 1
    # 血脂异常
    if(lipidRegular(datatuple) != 2 ):hazards += 1
    # 早发心血管病家族史
    if(familydiseaseRegular(datatuple) == 1):hazards+=1
    # 肥胖
    if(BMIRegular(datatuple) > 3):hazards += 1
    # 左心室肥厚
    if(imageologyRegular(datatuple) == 1):hazards += 1

    #劲动脉超声 xxx
    #脑血管病
    if(strokeRegular(datatuple) == 1):hazards += 1
    #心脏疾病
    if(heartRegular(datatuple) != 0):hazards += 1
    #肾脏疾病
    if(kidneyRegular(datatuple) != 0):hazards += 1
    #视网膜病变
    if(eyeRegular(datatuple) == 1):hazards += 1

    # 糖尿病 # 合并糖尿病，最危险因素
    if(diabetesRegular(datatuple) == 1):hazards += 50

    gap = [2,4,50,100]
    class_1 = [1,2,3,4]
    class_2 = [2,2,3,4]
    class_3 = [3,4,4,4]
    class_gap = [class_1,class_2,class_3]
    print hypertension_class
    return class_gap[hypertension_class][valueincustomgap(hazards,gap)]

def imageologyRegular(datatuple):
    data = datatuple[dataType.imageology.value]
    return valuecontainsth(data,u"左心室肥厚",1)

def medicineRegular(datatuple):
    data = datatuple[dataType.medicine.value]
    return 0

RegularHubList = {'gender':genderReguler,'education':educationRegular,'marriage':marriageRegular,'occupation':occupationRegular,'surrounding':surroundingRegular,\
            'mouth':mouthRegular,'disable':disableRegular,'age':ageRegular,'pregnant':pregnantRegular,'psychology':psychologyRegular,\
            'BMI':BMIRegular ,'BF':BFRegular ,'smoke':smokeRegular,'drink':drinkRegular,'diet':dietRegular,\
            'movement':movementRegular,'eye':eyeRegular,'skin':skinRegular,'heart':heartRegular,'kidney':kidneyRegular,\
            'bloodpressure':bloodpressureReguler,'bloodglucose':bloodglucoseRegular,'familydisease':familydiseaseRegular,'exposure':exposureRegular,\
            'copd':codpRegular,'diabetes':diabetesRegular,'hypertensionclassify':hypertensionclassifyRegular,'imageology':imageologyRegular,'medicine':medicineRegular,\
            'stroke':strokeRegular,'hyperlipemia':hyperlipemiaRegular,'lipid':lipidRegular,'hypertension':hypertensionRegular,
            }