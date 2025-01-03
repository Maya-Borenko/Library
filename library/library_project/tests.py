from django.test import TestCase
from library.library_models.models import Book, Like, SavedBook, Recommendation, UserInteraction, UserRegistration, User

class BookModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='12345')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            created_at=2023,
            genre='Test Genre',
            description='Test Description'
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.created_at, 2023)
        self.assertEqual(self.book.genre, 'Test Genre')
        self.assertEqual(self.book.description, 'Test Description')

    def test_like_creation(self):
        like = Like.objects.create(user=self.user, book=self.book)
        self.assertEqual(like.user, self.user)
        self.assertEqual(like.book, self.book)

    def test_saved_book_creation(self):
        saved_book = SavedBook.objects.create(user=self.user, book=self.book)
        self.assertEqual(saved_book.user, self.user)
        self.assertEqual(saved_book.book, self.book)

    def test_recommendation_creation(self):
        recommendation = Recommendation.objects.create(user=self.user, book=self.book)
        self.assertEqual(recommendation.user, self.user)
        self.assertEqual(recommendation.book, self.book)


#Тестирование форм
from library.library_models.forms import LikeForm, SaveBookForm, ChangeUsernameForm, BookSearchForm, RegisterForm, LoginForm

class RegisterFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'username': 'Test username',
            'email': 'email@mail.ru',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123'
        }
        form = RegisterForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': ''
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())

class LoginFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'username': '',
            'password': ''
        }
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

class LikeFormTest(TestCase):
    def test_valid_form(self):
        data = {'book_id': 1}
        form = LikeForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'book_id': ''}
        form = LikeForm(data=data)
        self.assertFalse(form.is_valid())

class SaveBookFormTest(TestCase):
    def test_valid_form(self):
        data = {'book_id': 1}
        form = SaveBookForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'book_id': ''}
        form = SaveBookForm(data=data)
        self.assertFalse(form.is_valid())

class ChangeUsernameFormTest(TestCase):
    def test_valid_form(self):
        data = {'username': 'newusername'}
        form = ChangeUsernameForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'username': ''}
        form = ChangeUsernameForm(data=data)
        self.assertFalse(not(form.is_valid()))

class BookSearchFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'genre': 'Test Genre'
        }
        form = BookSearchForm(data=data)
        self.assertTrue(form.is_valid())



#Тестирование views

from django.test import TestCase, Client
from django.urls import reverse

class BookListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='12345')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            created_at=2023,
            genre='Test Genre',
            description='Test Description'
        )

    def test_book_list_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

class BookDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='12345')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            created_at=2023,
            genre='Test Genre',
            description='Test Description'
        )

    def test_book_detail_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

class LikeBookViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='12345')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            created_at=2023,
            genre='Test Genre',
            description='Test Description'
        )

    def test_like_book_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('like_book', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)

class SaveBookViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='12345')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            created_at=2023,
            genre='Test Genre',
            description='Test Description'
        )

    def test_save_book_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('save_book', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)

class ChangeUsernameViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='12345')

    def test_change_username_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('change_username'), {'username': 'newusername'})
        self.assertEqual(response.status_code, 302)

class RecommendationsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='12345')

    def test_recommendations_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recommendations'))
        self.assertEqual(response.status_code, 302)

#Тестирование рекомендаций

from library.library_controllers.controllers import generate_recommendations

class RecommendationAlgorithmTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='12345')
        self.book1 = Book.objects.create(
            title='Book 1',
            author='Author 1',
            created_at=2023,
            genre='Novel',
            description='Description 1'
        )
        self.book_ans = Book.objects.create(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            description="A tale of the mysterious death of Jay Gatsby and the search for the truth.",
            genre="Novel",
            created_at=1925
        )
        likes = Like.objects.create(
            book_id=self.book1.id,
            user_id=self.user.id
        )

    def test_generate_recommendations(self):
        recommendations = generate_recommendations(self.user)
        self.assertTrue(self.book_ans, list(recommendations))


from library.library_controllers.controllers import (
    get_books, get_book, get_user_interactions, get_liked_books,
    get_recommendation, get_saved_books, create_user_interaction,
    generate_recommendations
)

class BookViewsTestCase(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='12345')

        # Create some books
        self.book1 = Book.objects.create(title='Book 1', genre='Fiction', author='Author 1', created_at=2024)
        self.book2 = Book.objects.create(title='Book 2', genre='Non-Fiction', author='Author 2', created_at=2024)

        # Create likes, recommendations, and saved books
        Like.objects.create(user=self.user, book=self.book1)
        Recommendation.objects.create(user=self.user, book=self.book2)
        SavedBook.objects.create(user=self.user, book=self.book1)

    def test_get_books(self):
        books = get_books()
        self.assertEqual(books.count(), 2)

    def test_get_book(self):
        book = get_book(self.book1.pk)
        self.assertEqual(book, self.book1)

    def test_get_liked_books(self):
        liked_books = get_liked_books(self.user)
        self.assertEqual(len(liked_books), 1)
        self.assertEqual(liked_books[0], self.book1)

    def test_get_recommendation(self):
        recommendations = get_recommendation(self.user)
        self.assertEqual(len(recommendations), 1)
        self.assertEqual(recommendations[0], self.book2)

    def test_get_saved_books(self):
        saved_books = get_saved_books(self.user)
        self.assertEqual(len(saved_books), 1)
        self.assertEqual(saved_books[0], self.book1)

    def test_generate_recommendations(self):
        book3 = Book.objects.create(title='Book 3', genre='Fiction', author='Author 3', created_at=2024)
        book4 = Book.objects.create(title='Book 4', genre='Non-Fiction', author='Author 4', created_at=2024)
        recommendations = generate_recommendations(self.user)
        self.assertEqual(len(list(recommendations)), 1)
        self.assertEqual(recommendations[0], book3)

    def test_generate_recommendations_no_interactions(self):
        # Remove all likes and saved books
        Like.objects.all().delete()
        SavedBook.objects.all().delete()

        recommendations = generate_recommendations(self.user)
        self.assertEqual(len(recommendations), 0)

    def test_generate_recommendations_multiple_books(self):
        # Create more books and interactions
        book3 = Book.objects.create(title='Book 3', genre='Fiction', author='Author 3', created_at=2024)
        book4 = Book.objects.create(title='Book 4', genre='Non-Fiction', author='Author 4', created_at=2024)
        book5 = Book.objects.create(title='Book 5', genre='Non-Fiction', author='Author 5', created_at=2024)
        Like.objects.create(user=self.user, book=book3)
        SavedBook.objects.create(user=self.user, book=book4)
        recommendations = generate_recommendations(self.user)
        self.assertEqual(len(list(recommendations)), 2)
        self.assertIn(self.book2, recommendations)
