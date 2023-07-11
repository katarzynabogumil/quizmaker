from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("login", login_API, name="login"),
    path("logout", logout_API, name="logout"),
    path("register", register_API, name="register"),
    # TODO change to /api/
    # API Routes
    path("quiz/<int:quiz_id>", quiz, name="quiz"),
    path("score/<str:category>/<int:quiz_id>", score, name="score"),
    path("remove_quiz/<int:quiz_id>", remove_quiz, name="remove_quiz"),
    path("views/<str:category>", quizzes, name="views"),
    path("question/<int:question_id>", question, name="question"),
    path(
        "remove_question/<int:question_id>",
        remove_question,
        name="remove_question",
    ),
]
