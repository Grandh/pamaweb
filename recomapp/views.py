# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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
        inputData[int(key)] = inputdataDict[key][0]

    print inputData
    result = activeRegualrHub(inputData)
    return JsonResponse(result)