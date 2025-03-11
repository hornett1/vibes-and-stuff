from django.test import TestCase
from .models import Cassette

class CassetteUploadTestCase(TestCase):
    def setUp(self, user):
        try:
            Cassette.objects.create(title='Kind Of Blue', author='Miles Davis', uploader=user)
        except:
            self.fail('Cassette creation failed')