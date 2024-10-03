from django.urls import path
from . import views

urlpatterns = [
    path('<int:question_index>/', views.quiz_view, name='quiz'),
    path('results/', views.quiz_results_view, name='quiz_results'),
    path('reset/', views.reset_quiz, name='reset_quiz'),  # Adicione esta linha
]