from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .forms import RegisterForm, LoginForm, UpdateProfileForm, UpdateUserForm
from .models import Profile


# Create your views here.
@login_required
def profile(request):
    try:
        profile = request.user.profile
        faveSongs = profile.fave_songs.all()
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='/users/profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'faveSongs': faveSongs})


def publicProfile(request, username):
    try:
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user.id)
        faveSongs = profile.fave_songs.all()
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    return render(request, 'public_profile.html', {'faveSongs': faveSongs, 'user':user})


def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect(to='/')
    return super(RegisterView, self).dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super(CustomLoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)


def home(request):
    return render(request, 'home/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='../login')

        return render(request, self.template_name, {'form': form})

def removefaveSong(request, song):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    oldsong = user_profile.fave_songs.get(song_id=song)
    user_profile.fave_songs.remove(oldsong)
    return redirect('/users/profile/')