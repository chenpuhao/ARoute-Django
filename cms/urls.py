# cms/urls.py

from django.contrib.auth import views as auth_views
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from .views import (
    SystemInfoViewSet, CustomPageViewSet,
    TagViewSet, CategoryViewSet, RegisterView, UserUpdateView,
    LoginView, UserDeleteView, UserListView, UserDetailView,
    ArticleCreateView, ArticleRetrieveView, ArticleDetailRetrieveView,
    ArticleUpdateView, ArticleDeleteView,
    CustomPageCreateView, CustomPageListView, CustomPageDetailView,
    CustomPageUpdateView, CustomPageDeleteView,
    TagCreateView, TagListView, TagDetailView, TagUpdateView, TagDeleteView,
    CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView,
    SystemInfoUpdateView, SystemInfoCreateView
)

router = DefaultRouter()
router.register(r'system-info', SystemInfoViewSet)
router.register(r'custom-pages', CustomPageViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
           title="ARoute API",
           default_version='v1',
           description="API for ARoute project",
           terms_of_service="https://www.aroute.cn/terms/",
           contact=openapi.Contact(email="contact@yourapp.com"),
           license=openapi.License(name="BSD License"),
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )
router = DefaultRouter()
router.register(r'system-info', SystemInfoViewSet)
router.register(r'custom-pages', CustomPageViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # 用户相关API
    path('register/', RegisterView.as_view(), name='register'),
    path('update-profile/', UserUpdateView.as_view(), name='update-profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
    path('user-info/', UserDetailView.as_view(), name='user-info'),  # 获取当前登录用户信息
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # 获取特定用户信息

    # 文章相关API
    path('create-article/', ArticleCreateView.as_view(), name='create-article'),
    path('articles/', ArticleRetrieveView.as_view(), name='articles-list'),  # 获取所有文章
    path('article/<int:pk>/', ArticleDetailRetrieveView.as_view(), name='article-detail'),  # 获取单篇文章
    path('update-article/<int:pk>/', ArticleUpdateView.as_view(), name='update-article'),  # 更新文章
    path('delete-article/<int:pk>/', ArticleDeleteView.as_view(), name='delete-article'),  # 删除文章

    # 自定义页面相关API
    path('create-custom-page/', CustomPageCreateView.as_view(), name='create-custom-page'),
    path('custom-pages/', CustomPageListView.as_view(), name='custom-pages-list'),  # 获取所有自定义页面
    path('custom-page/<int:pk>/', CustomPageDetailView.as_view(), name='custom-page-detail'),  # 获取单个自定义页面
    path('update-custom-page/<int:pk>/', CustomPageUpdateView.as_view(), name='update-custom-page'),  # 更新自定义页面
    path('delete-custom-page/<int:pk>/', CustomPageDeleteView.as_view(), name='delete-custom-page'),  # 删除自定义页面

    # 标签相关API
    path('create-tag/', TagCreateView.as_view(), name='create-tag'),
    path('tags/', TagListView.as_view(), name='tags-list'),  # 获取所有标签
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),  # 获取单个标签
    path('update-tag/<int:pk>/', TagUpdateView.as_view(), name='update-tag'),  # 更新标签
    path('delete-tag/<int:pk>/', TagDeleteView.as_view(), name='delete-tag'),  # 删除标签

    # 分类相关API
    path('create-category/', CategoryCreateView.as_view(), name='create-category'),
    path('categories/', CategoryListView.as_view(), name='categories-list'),  # 获取所有分类
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),  # 获取单个分类
    path('update-category/<int:pk>/', CategoryUpdateView.as_view(), name='update-category'),  # 更新分类
    path('delete-category/<int:pk>/', CategoryDeleteView.as_view(), name='delete-category'),  # 删除分类

    # JWT Token 相关
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # 系统信息相关
    path('api/system-info/<int:pk>/update/', SystemInfoUpdateView.as_view(), name='system-info-update'),
    path('api/system-info/create/', SystemInfoCreateView.as_view(), name='system-info-create'),
]
