from django.test import TestCase
from medical_study_app.models import Notecard, Notegroup, Client

# Create your tests here.
class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name="BOB", email="BEAR")
        Client.objects.create(name="Play", email="Man")

    def testpeople(self):

        bob = Client.objects.get(name="BOB")
        play = Client.objects.get(name="Play")
        self.assertEqual(bob.email, 'BEAR')
        self.assertEqual(play.email, 'Man')
        
    def testnamepeople(self):

        bob = Client.objects.get(name="BOB")
        play = Client.objects.get(name="Play")
        self.assertEqual(bob.name, 'BOB')
        self.assertEqual(play.name, 'Play')

class TestIfViewsWork(TestCase):
    def testpeople(self):

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

