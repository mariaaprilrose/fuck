import datetime, os
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import FormView
from authactions.forms import ContactForm, ImageUploadForm
from profile.models import UserProfile

def login_view(request):
    if not request.user.is_authenticated():
        context = {}
        if request.method == 'POST':
            username = request.POST.get('username', False)
            password = request.POST.get('password', False)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(request.GET['next'])
                    else:
                        return redirect('auth:home')
                else:
                    context = {'error_message': 'Your account has been disabled.'}
                    return render(request, 'authactions/login.html', context)
            else:
                context = {'error_message': 'Invalid username or password.'}
                return render(request, 'authactions/login.html', context)
        else:
            return render(request, 'authactions/login.html', context)
    else:
        raise Http404

def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        # return render(request, 'authactions/logout.html')
        if 'next' in request.GET:
            return HttpResponseRedirect(request.GET['next'])
        else:
            return redirect('auth:home')
    else:
        raise Http404

def signup_view(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            retype_password = request.POST.get('retype_password')

            # errors
            try:
                User.objects.get(username=username)
                return render(request, 'authactions/signup.html',
                              {'error_message': 'Username is already taken!'})
            except User.DoesNotExist:
                pass

            try:
                User.objects.get(email=email)
                return render(request, 'authactions/signup.html',
                              {'error_message': 'Email is already taken! Try another one.'})
            except User.DoesNotExist:
                pass

            if len(password) < 7:
                return render(request, 'authactions/signup.html',
                              {'error_message': 'Password is too short!'})

            if password != retype_password:
                return render(request, 'authactions/signup.html',
                              {'error_message': 'Passwords do not match!'})


            user = User.objects.create_user(
                username, # request.POST.get('username'),
                email, # request.POST.get('email'),
                password, # request.POST.get('password'),
            )
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            user_profile = UserProfile(user=user)
            user_profile.best_song_ever = request.POST.get('best_song_ever')
            user_profile.location = request.POST.get('state') + ", " + request.POST.get('country')
            user_profile.bio = request.POST.get('bio')

            music_interests = request.POST.getlist('music_interests')
            mi_placeholder = ''
            for mi in music_interests:
                 mi_placeholder += mi + ', '
            other_music_interests = request.POST.get('other_music_interests')
            if other_music_interests:
                mi_placeholder += other_music_interests
            user_profile.music_interests = mi_placeholder

            music_genres = request.POST.getlist('music_genres')
            mg_placeholder = ''
            for mg in music_genres:
                mg_placeholder += mg + ', '
            other_music_genres = request.POST.get('other_music_genres')
            if other_music_genres:
                mg_placeholder += other_music_genres
            user_profile.music_genres = mg_placeholder

            user_profile.save()

            # automatically logs in user
            _user = authenticate(username=username, password=password)
            login(request, _user)
            return redirect('profile:index', user.username) #redirects to profile page
        return render(request, 'authactions/signup.html')
    else:
        raise Http404

def home(request):
    context = {}
    if request.user.is_authenticated():
        user_profile = get_object_or_404(UserProfile, user=request.user)
        context = {'the_user': user_profile}
    return render(request, 'authactions/home.html', context)

def page404(request):
    raise Http404

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            now = datetime.datetime.now()
            date = '{0}-{1}-{2}'.format(now.year, now.month, now.day)
            time = now.isoformat()

            if not os.path.exists(settings.CONTACT_MESSAGES):
                os.makedirs(settings.CONTACT_MESSAGES)

            filename = settings.CONTACT_MESSAGES + date
            data = form.cleaned_data
            
            f = open(filename, 'a')
            f.write(time + '\n')
            f.write('Name: "' + data['name'] + '"\n')
            f.write('Phone: "' + str(data['phone']) + '"\n')
            f.write('Email: "' + data['email'] + '"\n')
            f.write('Message: "' + data['message'] + '"\n')
            f.write('\n')
            f.close()

            #if request.POST.get('subscribe_to_posts') == 'on':
                # add user email to mailing list (make a mailing list model?)
            return HttpResponseRedirect(request.GET['next'])
    else:
        raise Http404