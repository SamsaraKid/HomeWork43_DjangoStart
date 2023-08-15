from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def contacts(req):
    return render(req, 'contacts.html')

def workers(req):
    return render(req, 'workers.html')