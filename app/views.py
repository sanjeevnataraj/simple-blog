from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_protect
from app.forms import Signupform, Loginform, CitiesForm, ArticleForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View, ListView, CreateView, UpdateView
from django.contrib.auth.models import User
from .models import Cities, Article
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Count
from django.conf import settings
from django.core.paginator import Paginator


@csrf_protect
@login_required
def special(request):
    return HttpResponse("you are login successfully")


def user_logout(requets):
    logout(requets)
    return HttpResponseRedirect(reverse('login'))


class signupview(CreateView):
    def post(self, request, *args, **kwargs):
        form = Signupform(self.request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
        return render(request, "signup.html", {'form': form})

    def get(self, request, *args, **kwargs):
        form = Signupform(self.request.GET)
        return render(request, "signup.html", {'form': form})


class Loginview(View):
    def post(self, request, *args, **kwargs):
        form = Loginform(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user or form.is_valid():
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
        return render(request, 'login.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = Loginform()
        return render(request, 'login.html', {'form': form})


def validate_user(request):
    if request.is_ajax():
        name = request.GET.get('user_name', None)
        password = request.GET.get('password', None)
        data = {}
        if name:
            data = {'is_taken': User.objects.filter(username=name).exists()}
            if data['is_taken']:
                data['error_message'] = 'This user name is already selected'
        if password:
            if len(password) < 6:
                data['password_error'] = True
            else:
                data['password_error'] = False
        if authenticate(username=name, password=password):
            data['valid_user'] = True
        else:
            data['valid_user'] = False
        return JsonResponse(data)


def homepage(request):
    context = dict()
    context['data'] = Article.objects.all().order_by('-created')[:10]
    context['article_data'] = Article.objects.all().order_by('-created')
    context['tags'] = Article.objects.values('article_type').annotate(Count('article_type'))
    page = request.GET.get('page', 1)
    paginator = Paginator(Article.objects.all(), 10)
    context['pagination'] = paginator.page(page)
    return render(request, 'index.html', context)


class ArchivePage(ListView):
    template_name = "archive.html"
    context_object_name = 'article'
    paginate_by = 10
    ordering = ['-created']

    def get_queryset(self):
        return Article.objects.all()


@csrf_protect
@login_required(login_url=settings.LOGIN_PATH)
def add_edit_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            if 'artcle_image' in request.FILES:
                form_data = form.save(commit=False)
                form_data.artcle_image = request.FILES['artcle_image']
                form_data.author = request.user
                form_data.save()
                return HttpResponseRedirect(reverse('home'))

    else:
        form = ArticleForm(request.GET)
    return render(request, 'add_article.html', {'form': form})


def articleView(request, pk=None):
    context = dict()
    context['article'] = Article.objects.filter(id=pk)
    context['tags'] = Article.objects.values('article_type').annotate(Count('article_type'))
    return render(request, 'article_view.html', context)


def contact_page(request):
    return render(request, 'contact.html', {})


def category(request, pk=None):
    context = dict()
    print(pk)
    context['tags'] = Article.objects.values('article_type').annotate(Count('article_type'))
    if not pk:
        context['article_data'] = Article.objects.all().order_by('-created')
    else:
        context['article_data'] = Article.objects.filter(article_type=pk).order_by('-created')
    return render(request, 'category.html', context)
