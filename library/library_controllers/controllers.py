from django.shortcuts import get_object_or_404
from library.library_models.models import Book, UserInteraction, UserRegistration, Like, SavedBook, User, Recommendation
from library.library_models.forms import UserInteractionForm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from library.library_models.models import Book

def get_books():
    return Book.objects.all()

def get_book(pk):
    return get_object_or_404(Book, pk=pk)

def get_user_interactions(user):
    return UserInteraction.objects.filter(user=user.userregistration)

def get_liked_books(user):
    books_id = Like.objects.filter(user=user)
    books = []
    for i in range(len(books_id)):
        books.append(get_book(books_id[i].book_id))
    return books

def get_recommendation(user):
    books_id = Recommendation.objects.filter(user=user)
    books = []
    for i in range(len(books_id)):
        books.append(get_book(books_id[i].book_id))
    return books

def get_saved_books(user):
    books_id = SavedBook.objects.filter(user=user)
    books = []
    for i in range(len(books_id)):
        books.append(get_book(books_id[i].book_id))
    return books

def create_user_interaction(user, book, action):
    form = UserInteractionForm({'action': action})
    if form.is_valid():
        interaction = form.save(commit=False)
        interaction.book = book
        interaction.save()
        return interaction
    return None

def generate_recommendations(user):
    liked_books = Like.objects.filter(user=user).values_list('book', flat=True)
    saved_books = SavedBook.objects.filter(user=user).values_list('book', flat=True)
    interacted_books = set(liked_books).union(set(saved_books))
    genres = Book.objects.filter(id__in=interacted_books).values_list('genre', flat=True)
    authors = Book.objects.filter(id__in=interacted_books).values_list('author', flat=True)
    recommended_books = Book.objects.filter(genre__in=genres).exclude(id__in=interacted_books) | Book.objects.filter(
        author__in=authors).exclude(id__in=interacted_books)
    top_recommendations = recommended_books.distinct()[:10]
    for book in top_recommendations:
        Recommendation.objects.get_or_create(user=user, book=book)

    return top_recommendations