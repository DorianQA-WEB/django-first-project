from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Главная страница</h2>')

def about(request, name, age):
    return HttpResponse(f'''<h2>О сайте</h2>
                        <p>Имя: {name}</p>
                        <p>Возраст: {age}</p>
                        ''')

def contact(request):
    return HttpResponse('<h2>Контакты</h2>')

def user(request, name='Vladimir', age=29):
    return HttpResponse(f'<h2>Имя пользователя: {name}, Возраст: {age}</h2>')
