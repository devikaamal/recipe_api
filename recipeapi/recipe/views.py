from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, status

from recipe.models import Recipe

from recipe.serializers import RecipeSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

from recipe.models import Review
from recipe.serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class RecipeDetails(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class ReviewRecipe(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class search(APIView):
    def get(self, request):
        query = self.request.query_params.get('search')
        if query:
            re = Recipe.objects.filter(
                Q(title__icontains=query) | Q(cusine__icontains=query) | Q(meal_type__icontains=query) | Q(
                    ingredients__icontains=query))
            r = RecipeSerializer(re, many=True)
            return Response(r.data)
        else:
            return Response([])


class user_logout(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)





