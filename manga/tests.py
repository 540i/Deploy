from django.test import TestCase
from django.utils import timezone
from user.models import CustomUser
from .models import Genre, Review, Manga

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

        self.genre = Genre.objects.create(name='Action', slug='action')

        self.manga = Manga.objects.create(
            title='Naruto',
            description='A ninja story',
            type='e',
            slug='naruto',
            publication_year=2005,
            image='path/to/image.jpg',
        )
        self.manga.genre.add(self.genre)

        self.review = Review.objects.create(
            text='Great manga!',
            author=self.user,
            post=self.manga,
        )

    def test_genre_str(self):
        self.assertEqual(str(self.genre), 'Action')

    def test_review_str(self):
        self.assertEqual(str(self.review), 'Great manga!')

    def test_manga_str(self):
        self.assertEqual(str(self.manga), 'Naruto')
        