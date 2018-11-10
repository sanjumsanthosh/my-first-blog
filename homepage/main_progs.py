from .models import users,insert_blog,image_data_collector
from PIL import Image
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
    images = [user_data[0].image_upload.url,user_data[1].image_upload.url]
    data_dictionary = [author,date,category,main_title,link,images]
    return data_dictionary

#set data width and height and show
def format_image_data(width_req,height_req):
    image_data = image_data_collector.objects.all()
    all_data = glob.glob("media/img/*")
    print(all_data)
    print()
    print(image_data)

    for image_path in all_data:
        image = Image.open(image_path)
        width, height = image.size
        wid_dif =abs(width-width_req)
        hei_dif = abs(height-height_req)
        if wid_dif>hei_dif:
            factor = height/height_req
            image.thumbnail([width/factor,height],Image.ANTIALIAS)
        else:
            factor = width/width_req
            image.thumbnail([width,height/factor],Image.ANTIALIAS)
        final_image = image.crop((0,0,width_req,height_req))
        
# from homepage.main_progs import format_image_data
# format_image_data()

def recent_post():
    user_data = insert_blog.objects.all().reverse()
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
    
    for i in range(0,6,1):
        data=[]
        p = index-i
        data.append(user_data[p].blogger_name)#0
        data.append(user_data[p].Date_of_publish)#1
        data.append(user_data[p].category)#2
        data.append(user_data[p].blog_post_name)#3
        data.append(user_data[p].Blog_link)#4
        data.append(user_data[p].image_upload.url)#5
        data.append(i)#6
        data_dictionary.append(data)
    # author = [user_data[len(user_data)-1].blogger_name   ,   user_data[len(user_data)-2].blogger_name,   user_data[len(user_data)-3].blogger_name]
    # date = [user_data[len(user_data)-1].Date_of_publish   ,   user_data[len(user_data)-2].Date_of_publish,  user_data[len(user_data)-3].Date_of_publish]
    # category = [user_data[len(user_data)-1].category   ,   user_data[len(user_data)-2].category,   user_data[len(user_data)-3].category]
    # main_title = [user_data[len(user_data)-1].blog_post_name   ,   user_data[len(user_data)-2].blog_post_name,   user_data[len(user_data)-3].blog_post_name]
    # link = [user_data[len(user_data)-1].Blog_link   ,   user_data[len(user_data)-2].Blog_link,   user_data[len(user_data)-3].Blog_link]
    return data_dictionary
