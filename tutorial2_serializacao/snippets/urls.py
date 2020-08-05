from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Usado para views com funções

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# Usado para views com classes

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('files/', views.file_list, name='file-upload'),
    path('files/<int:pk>/', views.FileDetail.as_view()),
    path('files-content/', views.FilesContentList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
