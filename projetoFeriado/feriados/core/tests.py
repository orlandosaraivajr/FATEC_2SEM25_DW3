from django.test import TestCase

class RaizTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        self.assertAlmostEqual(self.resp.status_code, 200)
    
    def test_Natal_world(self):
        self.assertContains(self.resp, 'Natal') 
