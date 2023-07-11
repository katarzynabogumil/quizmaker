import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import random
from datetime import datetime

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# from django_nextjs.render import render_nextjs_page_sync

from ..models import User, Quiz, Question, Score
from ..serializers import UserSerializer, QuizSerializer


@api_view(["POST"])
@permission_classes([])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def login_API(request, format=None):
    # Attempt to sign user in
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    print(UserSerializer(user).data)
    print(user.user_permissions)

    # Check if authentication successful
    if user is not None:
        login(request, user)

        # user.user_permissions.set(.
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content, status=200)
    else:
        error = {"error": {"message": "Invalid username and/or password."}}
        return Response(error, status=401)


@api_view(["POST"])
@permission_classes([])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def register_API(request, format=None):
    username = request.POST["username"]
    email = request.POST["email"]

    # Ensure password matches confirmation
    password = request.POST["password"]
    confirmation = request.POST["confirmation"]
    if password != confirmation:
        error = {"error": {"message": "Passwords must match."}}
        return Response(error, status=401)

    # Attempt to create new user
    try:
        user = User.objects.create_user(username, email, password)
        user.save()
    except IntegrityError:
        error = {"error": {"message": "Username already taken."}}
        return Response(error, status=401)

    login(request, user)
    content = {
        "user": str(request.user),
        "auth": str(request.auth),
    }
    return Response(content, status=201)


# def login_view(request):
#     if request.method == "POST":
#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(
#                 request,
#                 "quizmaker/login.html",
#                 {"message": "Invalid username and/or password."},
#             )
#     else:
#         return render(request, "quizmaker/login.html")


def logout_API(request):
    logout(request)
    content = {
        "user": str(request.user),
        "auth": str(request.auth),
    }
    return Response(content, status=200)


# def register_API(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             return render(
#                 request, "quizmaker/register.html", {"message": "Passwords must match."}
#             )

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.save()
#         except IntegrityError:
#             return render(
#                 request,
#                 "quizmaker/register.html",
#                 {"message": "Username already taken."},
#             )
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "quizmaker/register.html")
