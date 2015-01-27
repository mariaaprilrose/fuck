from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from operator import attrgetter
from blog.forms import BlogForm
from blog.models import Blog
from profile.models import UserProfile

def index(request):
    # return HttpResponse('Why, hello there. :)')
    if request.user.is_authenticated():
        the_user = get_object_or_404(UserProfile, user=request.user)
    else:
        the_user = request.user

    blog_list = Blog.objects.all()
    blog_list = sorted(blog_list, key=attrgetter('date_published'), reverse=True)
    blog_posts = blog_list[:10]
    # blog_posts = []
    
    if blog_posts:
        main_post = blog_posts.pop(0)
    else:
        main_post = None

    context = {
        'the_user': the_user,
        'main_post': main_post,
        'blog_posts': blog_posts,
        'recent_posts': blog_list[:5],
    }

    return render(request, 'blog/index.html', context)

@user_passes_test(lambda u: u.is_staff)
def new_blog(request):
    if request.method == 'GET':
        form = BlogForm()
    else:
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = Blog(title=request.POST.get('title'))

            if 'picture' in request.FILES:
                blog.picture = request.FILES['picture']

            blog.content = request.POST.get('content')
            blog.save()
            return HttpResponseRedirect(request.GET['next'])
        else:
            return HttpResponse(
                request.POST.get('content')
            )

    if request.user.is_authenticated():
        the_user = get_object_or_404(UserProfile, user=request.user)
    else:
        the_user = request.user

    context = {
        'the_user': the_user,
        'form': form,
    }

    return render(request, 'blog/new.html', context)

def post(request, post_title):
    if request.user.is_authenticated():
        the_user = get_object_or_404(UserProfile, user=request.user)
    else:
        the_user = request.user

    title = post_title.replace('_', ' ')
    post = get_object_or_404(Blog, title=title)

    blog_list = Blog.objects.all()
    blog_list = sorted(blog_list, key=attrgetter('date_published'), reverse=True)
    recent_posts = blog_list[:5]

    context = {
        'the_user': the_user,
        'post': post,
        'recent_posts': recent_posts,
    }

    return render(request, 'blog/post.html', context)
