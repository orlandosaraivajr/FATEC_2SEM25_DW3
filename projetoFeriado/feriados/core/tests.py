from django.test import TestCase

class RaizTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        self.assertAlmostEqual(self.resp.status_code, 200)
    
    def test_Natal_world(self):
        self.assertContains(self.resp, 'Natal') 


from core.models import FeriadoModel

class FeriadoModelTest(TestCase):
    def setUp(self):
        FeriadoModel.objects.create(nome='Natal',dia=25,mes=12)
    
    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())
    
    def test_data(self):
        f = FeriadoModel.objects.first()
        self.assertEquals(f.nome, 'Natal')
        self.assertEquals(f.dia, 25)
        self.assertEquals(f.mes, 12)