from django.urls import path
from myapp.views import blog_view,BlogAPIView,BlogListCreateAPI,BlogListViewUpdateDelete

urlpatterns = [
    path('fbv/', blog_view),
    path('class_based/',BlogAPIView.as_view()),
    path('generics/',BlogListCreateAPI.as_view()),
    path('generics_delete/<int:pk>/',BlogListViewUpdateDelete.as_view())
]
