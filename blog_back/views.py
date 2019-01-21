from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from blog_back.forms import StuForm
from blog_back.models import User, Category, CategoryInfo, Article


def index(request):
    return render(request, 'web_back/index.html')


# 文章首页
def article(request):
    if request.method == 'GET':
        # 获取分页的角码，默认为1
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        # 设置显示数据和条数量
        pg = Paginator(articles, 5)
        articles = pg.page(page)
        return render(request, 'web_back/article.html', {'articles': articles})


# 添加文章
def add_article(request):
    if request.method == 'GET':
        all_cat = Category.objects.all()
        return render(request, 'web_back/add-article.html', {'all_cat': all_cat})
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('content')
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')
        c_id = request.POST.get('category')
        tags = request.POST.get('tags')
        icon = request.FILES.get('titlepic')
        Article.objects.create(title=title,
                               text=text,
                               key_words=keywords,
                               discribe=describe,
                               tage=tags,
                               icon=icon,
                               c_id=c_id)
        return HttpResponseRedirect(reverse('blog_back:add_article'))


# 删除文章
@csrf_exempt
def del_article(request):
    if request.method == 'POST':
        art_id = request.POST.get('id')
        Article.objects.filter(pk=art_id).delete()
        return JsonResponse({'code': 200, 'msg': '请求成功'})


# 修改文章
def update_article(request, id):
    if request.method == 'GET':
        art = Article.objects.filter(pk=id).first()
        all_cate = Category.objects.all()
        return render(request, 'web_back/update-article.html', {'all_cate': all_cate, 'art': art})
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('content')
        key_words = request.POST.get('keywords')
        discribe = request.POST.get('describe')
        tage = request.POST.get('tags')
        c_id = request.POST.get('category')
        icon = request.FILES.get('titlepic')
        # 修改
        art = Article.objects.filter(pk=id).first()
        art.title = title
        art.text = text
        art.key_words = key_words
        art.discribe = discribe
        art.tage = tage
        art.c_id = c_id
        art.icon = icon
        art.save()
        return HttpResponseRedirect(reverse('blog_back:article'))


# 栏目首页
def category(request):
    if request.method == 'GET':
        all_cat = Category.objects.all()
        return render(request, 'web_back/category.html', {'all_cat': all_cat})
    if request.method == 'POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        fid = request.POST.get('fid')
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')
        cat = Category.objects.create(c_name=name,
                                      b_name=alias,
                                      f_id_id=fid)
        cat1 = Category.objects.filter(c_name=name).first()
        catinfo = CategoryInfo.objects.create(key_words=keywords,
                                              catinfo=describe,
                                              cat_id=cat1.id)
        return HttpResponseRedirect(reverse('blog_back:category'))


# 删除栏目
def del_category(request, id):
    if request.method == 'GET':
        Category.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('blog_back:category'))


# 修改栏目
def update_category(request, id):
    if request.method == 'GET':
        cat = Category.objects.filter(pk=id).first()
        all_cat = Category.objects.all()
        return render(request, 'web_back/update-category.html', {'cat': cat, 'all_cat': all_cat})
    if request.method == 'POST':
        c_name = request.POST.get('name')
        b_name = request.POST.get('alias')
        key_words = request.POST.get('keywords')
        catinfo = request.POST.get('describe')
        cat = Category.objects.filter(pk=id).update(c_name=c_name,
                                                    b_name=b_name)
        catinfo = CategoryInfo.objects.filter(cat_id=id).update(key_words=key_words,
                                                                catinfo=catinfo)
        return HttpResponseRedirect(reverse('blog_back:category'))


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'web_back/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = User.objects.filter(username=username).first()
        if user:
            if check_password(password, user.password):
                # 1.向cookie中保存键值对，键为sessionid
                # 2.向django_session表中存为sessionid值
                # 3.向django_session表中存储键值对{‘username':ly}
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('blog_back:index'))
            else:
                msg = '密码错误'
                return render(request, 'web_back/login.html', {'msg': msg})
        else:
            msg = '账号错误'
            return render(request, 'web_back/login.html', {'msg': msg})


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'web_back/register.html')
    elif request.method == 'POST':
        # 获取页面提交的内容
        form = StuForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userkname = form.cleaned_data['userkname']
            gender = form.cleaned_data['gender']
            password = form.cleaned_data['password1']
            password = make_password(password)
            userage = form.cleaned_data['userage']
            User.objects.create(username=username,
                                userkname=userkname,
                                s_gender=gender,
                                password=password,
                                userage=userage)
            return HttpResponseRedirect(reverse('blog_back:login'))
        else:
            errors = form.errors
            return render(request, 'web_back/register.html', {'errors': errors})


# 退出
def logout(request):
    if request.method == 'GET':
        del request.session['user_id']
        return HttpResponseRedirect(reverse('blog_back:login'))
