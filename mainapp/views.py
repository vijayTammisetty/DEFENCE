from django.shortcuts import render

# Create your views here.

def main_dashbord(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request,'main/about.html')

def contact(request):
    ''' this is the contact page for home page'''
    return render(request, 'main/contact.html')