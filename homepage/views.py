from django.shortcuts import render
from homepage.models import insert_blog


# Create your views here.
def main_page(request):
    data = insert_blog.objects.all()
    return render(request,'homepage/mainpage.html',{'posts':data})
