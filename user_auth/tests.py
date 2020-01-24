from django.test import TestCase
from photos.models import Photos,Album
# Create your tests here.

class ModelTestCase(TestCase):

    def test_valid_caption(self):
        photo=Photos.objects.create(label="Photo1",like=5,caption="This a test photo")
        self.assertTrue(photo.valid_caption())

    def test_valid_like(self):
        photo=Photos.objects.create(label="Photo1",like=5,caption="This a test photo")
        self.assertTrue(photo.valid_like())
    
    def test_valid_caption(self):
        photo=Photos.objects.create(label="Photo1",like=5,caption="This a test photo")
        self.assertTrue(photo.valid_caption())
    
    
    def test_count_photos(self):
        photo=Photos.objects.create(label="Photo1",like=5,caption="This a test photo")
        album=Album.objects.create(photo)
        self.assertEqual(album.count_photos(),1)