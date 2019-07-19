"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_auth.views import LoginView
from app1.views import IndexTemplateView
from app1.views import SignUp
from app1.views import Logout
from app2.views import Greeting
from app3.views import Message
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', IndexTemplateView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/user/signup/', SignUp.as_view(), name='signup'),
    path('api/v1/login/', LoginView.as_view(), name='login'),
    path('api/v1/logout/', Logout.as_view(), name='apilogout'),
    path('api/v1/greeting/', Greeting.as_view(), name='greeting'),
    path('api/v1/message/', Message.as_view(), name='message'),
    path('api/v1/api-token-auth/', obtain_auth_token, name='api_token_auth'), #pass parameter as username and password
    # if user is created it gives the token that we can use for app2 and app3 API
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
