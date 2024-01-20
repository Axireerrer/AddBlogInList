from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FamousPersonForm
from .models import CategoryPerson, FamousPerson


@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = FamousPersonForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except:
                form.add_error(None, 'Внутрення ошибка в базе данных')
    else:
        form = FamousPersonForm()
    category = CategoryPerson.objects.all()
    data = {
        'title': 'Записи постов',
        'header': 'ИЗВЕСТНЫЕ ЛЮДИ',
        'form': form,
        'category': category,
    }
    return render(request, 'WebSite/index.html', context=data)


@login_required(login_url='login')
def show_persons(request, some_slug):
    rubrics = CategoryPerson.objects.get(slug=some_slug)
    items = FamousPerson.objects.filter(category_id=rubrics.pk)
    data = {
        'category': rubrics,
        'title': rubrics.name,
        'items': items,
        'header': 'ИЗВЕСТНЫЕ ЛЮДИ',
    }
    return render(request, 'WebSite/persons.html', context=data)

