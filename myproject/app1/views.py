from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView
from rest_auth.views import LogoutView
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from app1.serializers import UserSerializer


class SignUp(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        AllowAny
    ]
    serializer_class = UserSerializer


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class Logout(LogoutView):
    authentication_classes = (TokenAuthentication,)