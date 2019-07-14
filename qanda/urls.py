from django.urls import path
from .views import (
    QuestionListView,
    QuestionCreateView,
    QuestionDetailView,
    AnswerCreateView,
    AnswerUpdateView,
    AnswerAcceptanceUpdate,
    AboutView,
)

app_name = "qanda"

urlpatterns = [

    path('', QuestionListView.as_view(), name="question-list"),

    path('ask/', QuestionCreateView.as_view(), name="question-ask"),

    path('question/<int:pk>/', QuestionDetailView.as_view(), name="question-detail"),

    path('question/<int:pk>/answer/',
         AnswerCreateView.as_view(), name="answer-create"),

    path('question/<int:question_pk>/answer/update/<int:pk>/',
         AnswerUpdateView.as_view(), name="answer-update"),

    path('answer/update/<int:pk>/',
         AnswerAcceptanceUpdate.as_view(), name="update-answer-acceptance"),

    path('about/', AboutView.as_view(), name='about'),
]
