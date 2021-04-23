from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post, Group
#from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,
                  'index.html',
                  {'page': page, })