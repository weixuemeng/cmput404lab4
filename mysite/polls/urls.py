from django.urls import path
from . import views

# http://127.0.0.1:8000/polls/hello
# urlpatterns = [
#   path('hello', views.index, name='index'),
# ]


# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name = "detail"),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

app_name = 'polls'  # good if have multiple Django apps within a project that share similar url patttern 

# Refactoting: Generic Viewurl
# pk : primary key
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('api/questions/', views.get_questions, name='get_questions'),
    path('api/question/<int:pk>', views.update_question, name='update_question'),
]


