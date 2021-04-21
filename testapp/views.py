from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from .forms import *
# Create your views here.



def display_images(request):
    if request.method == 'GET':
        images = Pictures.objects.all()
        return render(request, 'displayimages.html',
                      {'images': images})

def Userview(request):
    if request.method == 'GET':
        form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        query_name = request.POST.get('name', '')
        query_url = request.POST.get('URL', '')
        query_phone = request.POST.get('phone_number', '')

        if form.is_valid():
            results = Validation.objects.get_or_create(name=query_name, URL=query_url, phonenumber=query_phone)
            if results[1]:
                return HttpResponse('data Submitted successfully')
            return HttpResponse('data Already exist')


    return render(
        request, 'home.html', {
            'form': form
        }
    )


def search_name(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', '')
        results = Validation.objects.filter(name__icontains=query_name)
        return render(request, 'searchit.html', {"results":results})

    return render(request, 'searchit.html')
