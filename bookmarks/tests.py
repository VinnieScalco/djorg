from django.test import TestCase
from .models import Bookmark

# Create your tests here.
class BookmarkTestCase(TestCase):
    def setUp(self):
        Bookmark.objects.create(name="Noteless bookmark", 
                                url="http://www.bookmarkless-in-seattle.com")
        Bookmark.objects.create(name="More note-worthy bookmark",
                                notes="This bookmark is worth writing a note about!",
                                url="http://www.note-this.com")
        pass

    def test_retrieving_valid_bookmark(self):
        """Test that a stored bookmark has correct values."""
        noteless_bookmark = Bookmark.objects.get(name="Noteless bookmark")
        self.assertEqual(noteless_bookmark.name, "Noteless bookmark")
        self.assertEqual(noteless_bookmark.url, "http://www.bookmarkless-in-seattle.com")
        self.assertEqual(noteless_bookmark.notes, "")
        noted_bookmark = Bookmark.objects.get(name="More note-worthy bookmark")
        self.assertEqual(noted_bookmark.name, "More note-worthy bookmark")
        self.assertEqual(noted_bookmark.url, "http://www.note-this.com")
        self.assertEqual(noted_bookmark.notes, "This bookmark is worth writing a note about!")

    def test_invalid_bookmarks(self):
        """Ensure database enforces validity/constraints on Bookmarks."""
        Bookmark.objects.create(name="Bookmark with invalid url",
                                url="245bhnj4lbnjk34t")