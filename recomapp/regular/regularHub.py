# -*- coding: utf-8 -*-
from dataRegular import *

# 辅助逻辑判断
def valueindictionary(data,dict):
    if not dict:return 0
    try:
        if data in dict.keys():return dict[data]
    except Exception,e:print e
    return 0

def valueingap(data,gaplist):
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

## 规则函数集合，建议保留单个文件维护
# 部分规则缺少检验，可以添加
# ========== class 1 =============
# 1
def genderReguler(datatuple): # 将数据封装为tuple形式，便于调用

    gender_data = datatuple.get(dataType.gender.value)
    if u'男' in gender_data:return 1;
    elif u'女' in gender_data:return 2;
    else:return 0
    
def educationRegular(datatuple):
    
    education_data = datatuple.get(dataType.education.value)
    switch = {u"本科及以上":1,
              u"高中":2,
              u"职高":2,
              u"初中":3,
              u"小学":4,
              u"无教育经历"  :5,
             }
    return valueindictionary(education_data,switch)

def marriageRegular(datatuple):
    
    marriage_data = datatuple[dataType.marriage.value]
    switch = {u"未婚":1,
              u"已婚":2,
              u"离异":3,}
    return valueindictionary(marriage_data,switch)
    
def occupationRegular(datatuple):
    
    occupation_data = datatuple[dataType.occupation.value]
    switch = {u"无":0,
              u"学生":1,
              u"工作":2} #对工作进行危险分级，需要和输入匹配:$('#').val() 
    return valueindictionary(occupation_data,switch)

# 5
def surroundingRegular(datatuple):
    
    surrounding_data = datatuple.get(dataType.surrounding.value)
    print surrounding_data
    switch = {u"良好":1,
              u"一般":2,
              u"较差":3,}
    return valueindictionary(surrounding_data,switch)

def mouthRegular(datatuple):
    
    mouth_data = datatuple.get(dataType.mouth.value)
    switch = {u"良好":1,
            u"一般":2,
            u"较差":3,}
    return valueindictionary(mouth_data,switch)

def disableRegular(datatuple):
    
    disable_data = datatuple[dataType.disable.value]
    switch = {u"无残疾":1,
             u"残疾":2,}
    return valueindictionary(disable_data,switch)

# ========== class 2 =============
def ageRegular(datatuple):
    
    age_data = datatuple[dataType.age.value]
    if not age_data:return 0
    age_data = int(age_data)
    gap=[0,3,7,14,45,60,200]
    return valueingap(age_data,gap)

def smokeRegular(datatuple):
    
    smoke_data = datatuple.get(dataType.smoke.value)
    if smoke_data:smoke_data=int(smoke_data)
    else:return 0
    gap = [0,1,2,3]
    return valueingap(smoke_data,gap)

# 10
def drinkRegular(datatuple):
    
    drink_data = datatuple.get(dataType.drink.value)
    if drink_data:drink_data=int(drink_data)
    else:return 0
    gap = [0,200,1000]
    return valueingap(drink_data,gap)

# ========= 长期数据处理需要考虑 =======
def movementRegular(datatuple):
    
    movement_data = datatuple.get(dataType.movement.value)
    switch = {u"良好":1,
              u"一般":2,
              u"较差":3,}
    return valueindictionary(movement_data,switch)

def BMIRegular(datatuple): # body mess index
    
    height_data = float(datatuple[dataType.height.value])
    weight_data = float(datatuple[dataType.weight.value])
    # 计算BMI
    bmivalue = weight_data/(height_data**2)
    print bmivalue
    gap = [0,18,24,27,30,35]
    return valueingap(bmivalue,gap)

def BFRegular(datatuple):
    
    gender_data = datatuple.get(dataType.gender.value)
    waistline_data = datatuple.get(dataType.waistline.value)
    weight_data = datatuple.get(dataType.weight.value)
    if waistline_data:waistline_data=float(waistline_data)
    else:return 0
    if weight_data:weight_data=float(weight_data)
    else:return 0
    
    gender = genderReguler({dataType.gender.value:gender_data}) # 其他地方调用规则数据，记得输入为tuple或list的形式
    bfvalue = 0
    if gender == 1:
        bfvalue = (waistline_data*0.74 - weight_data*0.0082-34.89)/weight_data*0.01
        gap = [0,0.15,0.18,1]
        print "bfvalue " + str(bfvalue)
        return valueingap(bfvalue,gap)
    elif gender == 2:
        bfvalue = (waistline_data*0.74 - weight_data*0.0082-44.47)/weight_data*0.01
        gap = [0,0.25,0.28,1]
        return valueingap(bfvalue,gap)
    else:
        return 0
def bloodpressureReguler(datatuple):
    
    diastolic_data = datatuple.get(dataType.diastolic.value)
    if diastolic_data:diastolic_data = float(diastolic_data)
    else:return 0

    systolic_data = datatuple.get(dataType.systolic.value)
    if systolic_data:systolic_data = float(systolic_data)
    else:return 0

    if diastolic_data < systolic_data: return 0  #输入错误检测
    elif diastolic_data > 300 or systolic_data < 0:
        print "输入可能有误"
    if diastolic_data > 140 or systolic_data > 90:return 2
    elif diastolic_data < 90 or systolic_data <60:return 3
    elif diastolic_data <140 and systolic_data <90:return 1
    else:return 0

# 15
def bloodglucoseRegular(datatuple):
    
    glucose_data = float(datatuple.get(dataType.glucose.value))
    # 错误判断
    if glucose_data < 0: return 0
    
    if glucose_data < 3.9:return 3
    elif glucose_data > 6.1:return 2
    else:
        return 1

def treatmentRegular(datatuple):
    
    treatment_data = datatuple.get(dataType.treatment.value)
    if not treatment_data:return 0

    if valueequalsth(treatment_data,u"无",1):return 1
    elif valuecontainsth(treatment_data,u"高血压",2):return 2
    elif valuecontainsth(treatment_data,u"糖尿病",3):return 3
    else:
        return 0

def heredopathiaRegular(datatuple):
    
    data = datatuple[dataType.heredopathia.value]
    if valueequalsth(data,"无",1):return 1
    elif not data:return 2  # 其他遗传病全确定为有
    else:
        return 0
    
def exposureRegular(datatuple):
    
    data = datatuple[dataType.exposure.value]
    if valueequalsth(data,"无",1):return 1
    elif not data:return 2  
    else:
        return 0
# ============ class 3 ===============
def imageologyRegular(datatuple):
    
    data = datatuple[dataType.imageology.value]
    return False

def medicineRegular(datatuple):
    
    data = datatuple[dataType.medicine.value]
    return False