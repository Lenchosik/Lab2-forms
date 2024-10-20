from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import UserForm
# Create your views here.
def index(request):
    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        adoyou = request.POST.get("adoyou")
        bdoyou = request.POST.get("bdoyou")
        email = request.POST.get("email")
        cdoyou = request.POST.get("cdoyou")
        url_text = request.POST.get("url_text")
        file = request.FILES.get("file")
        file_path = request.FILES.get("file_path")
        regex = request.POST.get("regex")
        choice = request.POST.get("choice")

        context = {
            'name': name,
            'age': age,
            'adoyou': adoyou,
            'bdoyou': bdoyou,
            'email': email,
            'cdoyou': cdoyou,
            'url_text': url_text,
            'file': file,
            'file_path': file_path,
            'regex': regex,
            'choice': choice
        }
        return render(request, 'result.html', context)

    else:
        userform = UserForm()
        return render(request, 'index.html', {"form": userform})
def about(request):
    return HttpResponse("<h2>О сайте</h2>")
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
#def products(request, productid=1):
 #   output = "<h2>Продукт № {0}</h2>".format(productid)
  #  return HttpResponse(output)
#def users(request, id, name):
 #   output = "<h2>Пользователь</h2> <h3>id: {0} Имя:{1}</h3>".format(id, name)
  #  return HttpResponse(output)
