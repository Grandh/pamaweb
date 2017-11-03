# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from regular.dataRegular import *
from regular.paTagController import *

# Create your views here.
# Ahead --
def patientTagForm(request):
    return render(request,'recomapp/main.html')

def getPatientTags(request):
    inputdataDict = dict(request.POST.iterlists())
    del inputdataDict[u'csrfmiddlewaretoken']

    # 构建成实际的数据表
    inputData = {}
    for key in inputdataDict.keys():
        data_type = dataType[key]  #[]表示读取Name ()用于读取number
        inputData[data_type.value] = inputdataDict[key][0]

    for key in inputData.keys():
        print key," ",inputData[key]
    result = activeRegualrHub(inputData)
    return JsonResponse(result)