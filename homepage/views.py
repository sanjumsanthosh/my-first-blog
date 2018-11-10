from django.shortcuts import render
from homepage.models import insert_blog
from .models import users
from .main_progs import top_posts,recent_post
# Create your views here.
#initialize
def main_page(request):
    return render(request,'homepage/index.html',{'top_posts':top_posts(),'recent_posts':recent_post})

def login(request):
    
    return render(request,'homepage/contact.html')