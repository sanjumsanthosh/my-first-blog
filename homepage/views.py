from django.shortcuts import render
from homepage.models import insert_blog


# Create your views here.
def main_page(request):
    
    return render(request,'homepage/index.html')

def login(request):
    
    return render(request,'homepage/contact.html')