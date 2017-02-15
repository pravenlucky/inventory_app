from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import MyRegistrationForm, EditProfileForm


def register_view(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory/registered')

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    args['user'] = request.user
    return render_to_response('register.html', args)


def registered_view(request):
    return render_to_response('registered.html', {'user': request.user})


def login_view(request):
    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    return render_to_response('login.html', c)



def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/inventory/logged_in')
    else:
        return HttpResponseRedirect('/inventory/invalid')


def logged_in_view(request):
    name = request.user.username
    return render_to_response('logged_in.html', {'name': name, 'user': request.user})


def logout_view(request):
    auth.logout(request)
    return render_to_response('logout.html')


def invalid_view():
    return render_to_response('invalid.html')


def edit_profile(request):
    user = request.user
    form = EditProfileForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return HttpResponseRedirect('/posts/')
    d = {}
    d.update(csrf(request))
    d['form'] = EditProfileForm()
    d['user'] = request.user
    return render_to_response("edit_profile.html", d)
