"""social_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from tastypie.api import Api
from api.resource.api_authentication import UserResource, UserSignUpResource, UserProfileResource, AuthenticationResource
from api.resource.api_post import PostResource, MyPostResource, UserPostResource

v1_api = Api(api_name='v1')

# Api for User
v1_api.register(UserResource())
v1_api.register(UserSignUpResource())
v1_api.register(AuthenticationResource())
v1_api.register(UserProfileResource())

# Api for Post
v1_api.register(PostResource())
v1_api.register(MyPostResource())
v1_api.register(UserPostResource())

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'api/', include(v1_api.urls))
]
