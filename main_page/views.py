from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Мое полное имя Абдыкадыров Даниель, мне 15 лет. Я живу и учусь в Кыргызско-Турецком лицее')

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse('У меня нету питомцев, но я хотел бы завести себе котенка, так как они нравятся мне больше всех')

def show_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())
