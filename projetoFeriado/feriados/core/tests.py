from django.test import TestCase

class RaizTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        self.assertAlmostEqual(self.resp.status_code, 200)



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


class NaoEhFeriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        self.assertAlmostEqual(self.resp.status_code, 200)
    
    def test_template(self):
        self.assertContains(self.resp, 'Não é Feriado') 


class EhFeriadoTest(TestCase):
    def setUp(self):
        FeriadoModel.objects.create(nome='Dia do TDD',dia=6,mes=10)
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        self.assertAlmostEqual(self.resp.status_code, 200)
    
    

from core.forms import FeriadoForm

class FeriadoFormTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_be_capitalized(self):
        form = FeriadoForm({'nome':'dia de são nunca'})
        form.is_valid()
        self.assertEqual('DIA DE SÃO NUNCA', form.cleaned_data['nome'])
        

from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from core.models import FeriadoModel

class FeriadoAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Cria um usuário e token (caso use autenticação)
        self.user = User.objects.create_user(username='admin', password='123')
        self.client.force_authenticate(user=self.user)
        self.feriado = FeriadoModel.objects.create(nome="Natal", dia=25, mes=12)

    def test_listar_feriados(self):
        url = reverse('feriado_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)