from django.test import TestCase
from django.urls import reverse
from ..views import relatorio_filtro, relatorio


class RelatorioTestCase(TestCase):
    
    def test_view_url_relatorio_existe(self):
        response = self.client.get(reverse('relatorio'))
        self.assertEquals(response.status_code, 200)


    
    
    def test_view_url_filtro_existe(self):
        response = self.client.get(reverse('filtro'))
        self.assertEquals(response.status_code, 200)



    def test_view_filtro_med(self):
        response = self.client.get(reverse('filtro')+'?med=TALISON')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['consulta_list'] == 2))


    
    def test_view_filtro_data(self):
        response = self.client.get(reverse('filtro')+'?start_date=2018-06-10&end_date=2018-06-10')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['consulta_list'] == 7))


    
    def test_view_filtro_med_data(self):
        response = self.client.get(reverse('filtro')+'?med=TALISON&start_date=2018-05-09&end_date=2018-07-10')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['consulta_list'] == 1))

    
