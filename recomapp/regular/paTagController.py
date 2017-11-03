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
    print all_tag_filter
    tagResultDict = {}
    # 进行标签的数据源同步更新
    for i,data_num in enumerate(all_tag_filter):
        tag_type = tagType(i+1)
        if data_num == len(tag2data_reflect_dict[tag_type][0]):
                tagResultDict[tag_type.value]=RegularHubList[tag_type.name](dataList)
    #输出显示
    # print tagResultDict
    for key in tagResultDict.keys():
        tag_type = tagType(key)
        index = tagResultDict[key]
        try:
            tagResultDict[key] = tag_type.name + " " + tag2data_reflect_dict[tag_type][1][index]
        except Exception,e:
            print e
            tagResultDict[key] = ""

    print tagResultDict
    return tagResultDict