from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.recipe = Recipe.objects.create(
            title='Test Recipe', description='Test description', ingredients='Test ingredients', instructions='Test instructions', user=self.user
        )

    def test_recipe_creation(self):
        recipe = Recipe.objects.get(id=self.recipe.id)
        self.assertEqual(recipe.title, 'Test Recipe')

