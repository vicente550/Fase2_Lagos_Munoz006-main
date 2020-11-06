from django.test import TestCase
from  . models import VideoJuego

class VideoJuegoTestCase(TestCase):

    def setUp(self):
        VideoJuego.objects.create(id ="44fc2b9d-2b04",name="Cloudpunk", departure= '12/12/2020', price= 999 )

    def test_name_max_length(self):
        VideoJuego1 = VideoJuego.objects.get(id="44fc2b9d-2b04")
        max_length = VideoJuego1._meta.get_field('name').max_length
        self.assertEqual(max_length,200)

    def test_name_price(self):
        VideoJuego1 = VideoJuego.objects.get(name="Cloudpunk")
        self.assertEqual(VideoJuego1.VideoJuego.price, 999)