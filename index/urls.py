from django.urls import path


from index.views import *

urlpatterns = [
    path('', index),

    path('hello/', news),
    path('create/', create),
    path('news/', news),
    path('news/<str:id>', newsInner),
    path('about/', about),

]