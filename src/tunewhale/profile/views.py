from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from authactions.forms import ImageUploadForm
from profile.models import UserProfile

def index(request, user_username):
    error_message = ''
    success_message = ''
    some_user = get_object_or_404(User, username=user_username)
    some_user_profile = get_object_or_404(UserProfile, user=some_user)
    if request.user.is_authenticated():
        the_user = get_object_or_404(UserProfile, user=request.user)

        try:
            the_user.following.get(username=some_user.username)
            is_following = True # is the_user a follower of some_user
        except User.DoesNotExist:
            is_following = False

        if request.method == 'GET':
            form = ImageUploadForm()
        else:
            form = ImageUploadForm(request.FILES)
            if form.is_valid():
                if 'avatar' not in request.FILES and 'cover' not in request.FILES:
                    error_message = 'No image detected.'
                else:
                    if 'avatar' in request.FILES:
                        the_user.avatar = request.FILES['avatar']
                    if 'cover' in request.FILES:
                        the_user.cover = request.FILES['cover']
                    the_user.save()
                    success_message = 'Upload successful.'
            else:
                error_message = 'Upload failed.'
        some_user = get_object_or_404(User, username=user_username)
        some_user_profile = get_object_or_404(UserProfile, user=some_user)

    else:
        avatar_url = None
        is_following = False
        form = ImageUploadForm()
        the_user = request.user

    su_status = ''    
    if some_user_profile.status.url == settings.BABYWHALE_IMG_PATH:
        su_status = 'Baby Whale'
    elif some_user_profile.status.url == settings.TUNEWHALE_IMG_PATH:
        su_status = 'Tune Whale'
    elif some_user_profile.status.url == settings.KILLERWHALE_IMG_PATH:
        su_status = 'Killer Whale'
    
    su_followers = []
    followers = some_user_profile.followers.all()
    if followers:
        for u in followers:
            user = UserProfile.objects.get(user=u)
            su_followers.append(user)

    context = {
        'is_following': is_following,
        'the_user': the_user,
        'some_user': some_user_profile,
        'su_status': su_status,
        'su_followers': su_followers,
        'month': some_user_profile.date_registered.strftime('%B'),
        'year': some_user_profile.date_registered.year,
        'form': form,
        'error_message': error_message,
        'success_message': success_message,
    }

    return render(request, 'profile/index.html', context)

def follow(request, user_to_follow):
    the_user = get_object_or_404(UserProfile, user=request.user)
    some_user = get_object_or_404(User, username=user_to_follow)
    some_user_profile = get_object_or_404(UserProfile, user=some_user)
    some_user_profile.followers.add(request.user)
    the_user.following.add(some_user)
    return HttpResponseRedirect(request.GET['next'])

def unfollow(request, user_to_unfollow):
    the_user = get_object_or_404(UserProfile, user=request.user)
    some_user = get_object_or_404(User, username=user_to_unfollow)
    some_user_profile = get_object_or_404(UserProfile, user=some_user)
    some_user_profile.followers.remove(request.user)
    the_user.following.remove(some_user)
    return HttpResponseRedirect(request.GET['next'])