from django.shortcuts import render,HttpResponse,redirect
from base.models import Category,Articles
from base.forms import RegisterationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    context={
        # 'categories':Category.objects.all(),
        'articles':Articles.objects.filter(status='published',is_treanding=True).order_by('-updated_at'),
        'not_treanding_articles':Articles.objects.filter(status="published",is_treanding=False),
        # 'recent_articles':Articles.objects.filter().order_by('-updated_at')
    }

    return render(request,'home.html',context)

def category_articles(request,cat):
    key=Category.objects.get(category_name=cat)
    context={
        'articles':Articles.objects.filter(category=key.id),
        # 'categories':Category.objects.all(),
        'category':key
    }
    return render(request,'category.html',context)


@login_required(login_url='login page')
def single_article(request,info):
    context={
        'article':Articles.objects.get(slug=info)
    }
    return render(request,'single_article.html',context)
    

def register(request):
    if request.method=='POST':
        form=RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'register.html',{'form':form})
    form=RegisterationForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'login.html',{'form':form})
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    auth.logout(request)
    return redirect('home')