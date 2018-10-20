from django.db import models


# Create your models here.
categories = (
    ('Technology','tech'),
    ('sports','sports'),
    ('fasion','fasion')
)
class users(models.Model):
    user_name  = models.CharField(max_length=30,blank=False, null=False,default = 'random_blogger')
    user_id = models.IntegerField(blank=False)
    blog_name = models.CharField(max_length = 30 , blank=False , default = 'random_blog')
    blog_url = models.URLField(blank = False)

    def __str__(self):
        data = self.user_name + ':' + self.blog_name
        return data
class insert_blog(models.Model):
    
    blogger_name = models.CharField(max_length=30,blank=False, null=False,default = 'random_blogger')
    blog_post_name = models.CharField(max_length = 50 ,blank=False, null=False,default='random_blog')
    image_name = models.TextField(blank=False)
    user_id = models.IntegerField(blank=False)
    category = models.TextField(blank=False, null=False,choices = categories)
    Date_of_publish = models.DateField(auto_now=True)

    def __str__(self):
        data = self.blogger_name + ':' + str(self.blog_post_name)[:6]+ '...'
        return data
