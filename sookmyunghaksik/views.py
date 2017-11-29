# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def keyboard(request):
    keyboard = {
        "type" : "buttons",
        "buttons" : ["스노로즈 가기", "학식 확인", "버튼3"]
    }

    return JsonResponse(keyboard)