from django.shortcuts import redirect, render, reverse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from users.models import Pornstar
from videos.models import Video
from core.models import StaticImage


# Create your views here.
class HomeView(View):
    def get(self, request):
        header = StaticImage.objects.get(name="Header Wide")
        logo = StaticImage.objects.get(name="Logo main")
        return render(request, 'home.html', context={"videos": Video.objects.filter(is_3d=True), "header": header, "logo": logo})


class ThreeDVideosView(View):
    def get(self, request):
        header = StaticImage.objects.get(name="Header Wide")
        logo = StaticImage.objects.get(name="Logo main")
        return render(request, '3d_videos.html', context={"videos": Video.objects.filter(is_3d=True), "header": header, "logo": logo})


class TwoDVideosView(View):
    def get(self, request):
        header = StaticImage.objects.get(name="Header Wide")
        logo = StaticImage.objects.get(name="Logo main")
        return render(request, '2d_videos.html', context={"videos": Video.objects.filter(is_3d=False), "header": header, "logo": logo})


class SignupView(View):
    def get(self, request):
        header = StaticImage.objects.get(name="Header Wide")
        logo = StaticImage.objects.get(name="Logo main")

        exists = request.GET.get('exists')
        return render(request, 'signup.html', context={"exists": exists, "header": header, "logo": logo})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email and password:
            try:
                user = User.objects.get(email=email)
                return redirect(reverse('signup') + '?exists=true')

            except User.DoesNotExist:
                username = email.split('@')[0]
                user = User.objects.create_user(email=email, username=username)
                user.set_password(password)
                user.save()

        return redirect('home')


class LoginView(View):
    def get(self, request):
        header = StaticImage.objects.get(name="Header Wide")
        logo = StaticImage.objects.get(name="Logo main")

        return render(request, 'login.html', context={"header": header, "logo": logo})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, email=email, password=password)

            if user:
                login(request, user)
                return redirect('home') # Redirect to a success page.
            else:
                return redirect(reverse('login') + '?exists=true') # Redirect to a failure page.

        except User.DoesNotExist:
            return redirect(reverse('login') + '?exists=false')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class GirlsListView(View):
    def get(self, request):
        header = StaticImage.objects.get(name="Header Wide")
        logo = StaticImage.objects.get(name="Logo main")

        pornstars = Pornstar.objects.all()

        return render(request, 'girls.html', context={"header": header, "logo": logo, "pornstars": pornstars})


class PornstarView(View):
    def get(self, request, pornstar_id):
        header = StaticImage.objects.get(name="Header Wide")
        logo = StaticImage.objects.get(name="Logo main")

        pornstar = Pornstar.objects.get(id=pornstar_id)
        videos = Video.objects.filter(pornstars=pornstar)
        return render(request, 'pornstar.html', context={"pornstar": pornstar, "header": header, "logo": logo, "videos": videos})
