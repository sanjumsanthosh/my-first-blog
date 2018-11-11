from .models import users,insert_blog,image_data_collector
from PIL import Image,ImageFilter,ImageEnhance
import glob
def top_posts():
    user_data = insert_blog.objects.all()
    data_dictionary = []
    #data.0 -->author
    #data.1 -->date
    #data.2 -->category
    #data.3 -->main_title
    #data.4 -->link
    author = [user_data[0].blogger_name,user_data[1].blogger_name]
    date = [user_data[0].Date_of_publish,user_data[1].Date_of_publish]
    category = [user_data[0].category,user_data[1].category]
    main_title = [user_data[0].blog_post_name,user_data[1].blog_post_name]
    link = [user_data[0].Blog_link,user_data[1].Blog_link]
    url1 = user_data[0].image_upload.url.split('/')
    url1[2]='edited_media'
    url1 = '/'.join(url1)
    url2 = user_data[1].image_upload.url.split('/')
    url2[2]='edited_media'
    url2 = '/'.join(url2)
    images = [url1,url2]
    data_dictionary = [author,date,category,main_title,link,images]
    return data_dictionary

def edit_image(img,width,height):
    x,y = img.size
    temp = img.resize((width,height),Image.ANTIALIAS)
    temp = temp.filter(ImageFilter.BoxBlur(9))
    enhancer = ImageEnhance.Color(temp)
    temp = enhancer.enhance(.3)
    print('baground size : ',temp.size)
    print('required size : ',width,height)
    
    w_dif = x-width 
    h_dif = y-height
    print('width diff : ',x-width,'height diff : ',y-height)
    temp2 = temp
    if w_dif<h_dif:
        new_width = int(x/(y/height))
        print('new_width : ',new_width)
        temp2 = img.resize((new_width,height),Image.ANTIALIAS)
    else:
        new_height = int(y/(x/width))
        print('new_height : ',new_height)
        temp2 = img.resize((width,new_height),Image.ANTIALIAS)
        
    #print('temp = ',temp.size)
    #print('temp2 = ',temp2.size)
    img_w,img_h=temp2.size
    print('after editing size of image : ',temp2.size)
    offset = ((width-img_w) // 2, (height-img_h) // 2)
    temp.paste(temp2, offset)
    return temp

def edit_images():
    data = glob.glob('media/media/*')
    if(len(data)!=0):
        for images in data:
            try:
                img = Image.open(images)
                print ('...........................')
                print('image name : ',images)
                print ('original size : ',img.size)
                edited = edit_image(img,700,450)
                edited.save('media/edited_media/%s'%images.split('/')[2],edited.format)
            except :
                print("**********    something's wrong with this file %s"%images)

#  from homepage.main_progs import edit_images
#  edit_images()
def recent_post():
    user_data = insert_blog.objects.all().reverse()
    edit_images()
    data_dictionary = []
    #data.0 -->author
    #data.1 -->date
    #data.2 -->category
    #data.3 -->main_title
    #data.4 -->link
    # author=[]
    # date=[]
    # category=[]
    # main_title=[]
    # link=[]
    # images = []
    # index_number = []
    index = len(user_data)-1
    
    for i in range(0,len(user_data),1):
        data=[]
        p = index-i
        data.append(user_data[p].blogger_name)#0
        data.append(user_data[p].Date_of_publish)#1
        data.append(user_data[p].category)#2
        data.append(user_data[p].blog_post_name)#3
        data.append(user_data[p].Blog_link)#4
        url = user_data[p].image_upload.url.split('/')
        url[2]='edited_media'
        url = '/'.join(url)
        data.append(url)#5
        data.append(i)#6
        data_dictionary.append(data)
        
    # author = [user_data[len(user_data)-1].blogger_name   ,   user_data[len(user_data)-2].blogger_name,   user_data[len(user_data)-3].blogger_name]
    # date = [user_data[len(user_data)-1].Date_of_publish   ,   user_data[len(user_data)-2].Date_of_publish,  user_data[len(user_data)-3].Date_of_publish]
    # category = [user_data[len(user_data)-1].category   ,   user_data[len(user_data)-2].category,   user_data[len(user_data)-3].category]
    # main_title = [user_data[len(user_data)-1].blog_post_name   ,   user_data[len(user_data)-2].blog_post_name,   user_data[len(user_data)-3].blog_post_name]
    # link = [user_data[len(user_data)-1].Blog_link   ,   user_data[len(user_data)-2].Blog_link,   user_data[len(user_data)-3].Blog_link]
    return data_dictionary
