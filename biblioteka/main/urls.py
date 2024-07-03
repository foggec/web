from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from books import views as books_views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.redirect_to_own_profile, name='redirect_to_own_profile'),
    path('profile/', user_views.redirect_to_own_profile, name='profile'),
    path('profile/<str:username>', user_views.profile, name='profile'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
    path('<int:book_id>', books_views.game_detail, name='books-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('books.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)