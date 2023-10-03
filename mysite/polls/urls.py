from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # Notice the <> contain placeholders for the URL parameter, which is passed to the view. The view takes the placeholder (e.g. question_id) as a paramter of the function.

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]