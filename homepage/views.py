from django.shortcuts import render
from homepage.models import insert_blog
data = insert_blog.objects.all()

# Create your views here.
def main_page(request):
    return render(request,'homepage/mainpage.html',{'posts':data})
