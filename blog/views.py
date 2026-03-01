from django.http import (HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseBadRequest,
                         HttpResponseForbidden)
from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return render(request, 'blog/index.html', context={'body': '<h1>Hello Word!<h1>'})

def about(request, name, age):
    return HttpResponse(f'''<h2>О сайте</h2>
                        <p>Имя: {name}</p>
                        <p>Возраст: {age}</p>
                        ''')

def contact(request):
    return HttpResponseRedirect('/about/')

def detail(request):
    return HttpResponsePermanentRedirect('/')

def user(request):
    age = request.GET.get('age', 0)
    name = request.GET.get('name', 'vova')
    return HttpResponse(f'<h2>Пользователь</h2>'
                        f' <p>Имя: {name}</p>'
                        f' <p>Возраст: {age}</p>'
                        )

def products(request, id):
    return HttpResponse(f'Список товаров {id}')

def comments(request, id):
    return HttpResponse(f'Комментарии к товару {id}')

def questions(request, id):
    return HttpResponse(f'Вопросы по товару {id}')

def new(request):
    return HttpResponse(f'Новый товары')

def top(request):
    return HttpResponse(f'Наиболее продаваемые товары')

def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age < 1 or age > 110:
        return HttpResponseBadRequest('Недопустимый возраст')
    if age < 18:
        return HttpResponseForbidden('Доступ запрещен')
    else:
        return HttpResponse('Доступ разрешен')