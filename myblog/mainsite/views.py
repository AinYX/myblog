from django.template.loader import get_template
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post


# Create your views here.


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()          # 返回<class 'django.db.models.query.QuerySet'>返回queryset
    # print(type(posts))
    now = datetime.now()
    html = template.render(locals())    # 返回<class 'django.utils.safestring.SafeText'>数据库的数据 然后写成字典格式的  返回json数据  浏览器能识别
    # print(type(html))
    return HttpResponse(html)


def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
