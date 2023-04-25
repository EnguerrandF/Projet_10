"""soft_desk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers

from authentication.views import CreateUserView
from API.views import ProjetsView, ContributorsView, IssuesView, CommentsView


router = routers.SimpleRouter()

router.register('signup', CreateUserView, basename='signup')
router.register('projets', ProjetsView, basename='projets')

projet_router = routers.NestedDefaultRouter(router, 'projets', lookup='projet')
projet_router.register('user', ContributorsView, basename='user')

issues_router = routers.NestedDefaultRouter(router, 'projets', lookup='projet')
issues_router.register('issues', IssuesView, basename='issues')

comments_router = routers.NestedDefaultRouter(issues_router, 'issues', lookup='issue')
comments_router.register('comments', CommentsView, basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='obtain_tokens'),    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/', include(router.urls)),
    path('api/', include(projet_router.urls)),
    path('api/', include(issues_router.urls)),
    path('api/', include(comments_router.urls)),
]
