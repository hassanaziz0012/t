from django.urls import path
from users import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('3d-videos/', views.ThreeDVideosView.as_view(), name='3d-videos'),
    path('2d-videos/', views.TwoDVideosView.as_view(), name='free-videos'),
    path('girls/list', views.GirlsListView.as_view(), name="girls-list"),
    path('girls/<int:pornstar_id>', views.PornstarView.as_view(), name='pornstar'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
