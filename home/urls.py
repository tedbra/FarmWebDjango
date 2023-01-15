from django.urls import path
from . import views
from .views import BlogView, ArticleDetailView,HomeView,AddArticleView,AdminPanView
from .views import UpdateArticleView,DeleteArticleView, AddCategoryView,CategoryView
from .views import  LikeView ,AddCommentView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    #path('',views.launch_home, name='home'),
    path('',HomeView.as_view(), name='home'),
    path('blog/',BlogView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add-article/',AddArticleView.as_view(), name='add-article'),
    path('adminPan/',AdminPanView, name='adminPan'),
    path('article/update/<int:pk>',UpdateArticleView.as_view(), name='update-article'),
    path('article/<int:pk>/remove',DeleteArticleView.as_view(), name='delete-article'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('add-category/',AddCategoryView.as_view(), name='add-category'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),  
    path('like/<int:pk>', LikeView, name='like_post'),  
]