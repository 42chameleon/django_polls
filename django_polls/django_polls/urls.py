"""django_polls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url
from polls.views import PollViewSet, QuestionViewSet, VoteViewSet, UserVoteViewSet
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from .yasg import urlpatterns as doc_urls


router = DefaultRouter()
router.register(r'polls', PollViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'uservotes', UserVoteViewSet, basename='uservote')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^v1/', include((router.urls, 'v1'), namespace='v1')),
]

urlpatterns += doc_urls
