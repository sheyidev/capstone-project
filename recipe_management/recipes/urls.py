# recipes/urls.py
from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView, RatingCreateView, CategoryListView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/<int:recipe_id>/rate/', RatingCreateView.as_view(), name='rate-recipe'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
