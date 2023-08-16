from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def index(req):
    return render(req, 'index.html')

def contacts(req):
    return render(req, 'contacts.html')

def workers(req):
    return render(req, 'workers.html')

def month(req, id):
    id = int(id)
    month = ['МАРТ', 'АПРЕЛЬ', 'МАЙ']
    workers = ['Василий Хвостович', 'Люся Кусьевна', 'Барсик Мурхалыч']
    imgs = ['img/vas.jpg', 'img/lus.jpg', 'img/bars.jpg']
    data = {'kmon': month[id], 'kwor': workers[id], 'kimg': imgs[id]}
    return render(req, 'month.html', context=data)

def product(req, id):
    id = int(id)
    name = ['СЛИВКИ', 'ЛЕЖАНКА', 'КОЛБАСА']
    desc = ['Вкуснейшие и нежные', 'Мягкие и удобные', 'Питательная и ароматная']
    imgs = ['img/sli.jpg', 'img/lej.jpg', 'img/kolb.jpg']
    data = {'kname': name[id], 'kdesc': desc[id], 'kimg': imgs[id]}
    return render(req, 'product.html', context=data)