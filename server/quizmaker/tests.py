from django.test import TestCase
from .models import User, Quiz, Question, Score

# Create your tests here.

class UserTestCase(TestCase):
  def test_user_created(self):
    obj = User.objects.create(username='username', email='username@example.com', password='1234')
    self.assertEqual(obj.id, 1)

# class QuizTestCase(TestCase):
#   def test_quiz_created(self):
#     obj = Quiz.objects.create(title='Title') # author!
#     self.assertEqual(obj.id, 1)