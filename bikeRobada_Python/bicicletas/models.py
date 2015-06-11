from django.db import models

# Create your models here.


class Denuncias(models.Model):
    '''Tabla de denuncias de robos'''

    TIPOS = (
            ('MTB', 'MTB'),
            ('CARRETERA', 'CARRETERA'),
            ('CICLOCROSS', 'CICLOCROSS'),
            ('PASEO', 'PASEO'),
            ('INFANTIL', 'INFANTIL'),
            ('ANTIGUA', 'ANTIGUA'),
            ('TRIAL', 'TRIAL'),
            ('FREESTYLE', 'FREESTYLE'),
            ('URBANA', 'URBANA'),
            ('BMX', 'BMX'),
            ('CARGO', 'CARGO'),
            ('CUSTOM', 'CUSTOM'),
            ('CRUISER', 'CRUISER'),
            ('PISTA', 'PISTA'),
            ('TANDEM', 'TANDEM'),
            ('FIXED', 'FIXED'),
            ('PLEGABLE', 'PLEGABLE'),
            ('ELECTRICA', 'ELECTRICA')
        )

    correo = models.CharField(max_length=200, blank=False)
    marca = models.CharField(max_length=200, blank=False)
    modelo = models.CharField(max_length=200, blank=False)
    aniomodelo = models.CharField(max_length=4, blank=True)
    tipo = models.CharField(max_length=40, choices=TIPOS, default='MTB')
    colores = models.CharField(max_length=200, blank=False)
    velocidades = models.CharField(max_length=100, blank=True)
    marcavelocidades = models.CharField(max_length=100, blank=True)
    modelovelocidades = models.CharField(max_length=100, blank=True)
    nrocuadro = models.CharField(max_length=20, blank=True)
    nrohorquilla = models.CharField(max_length=20, blank=True)
    fecharobo = models.DateField(auto_now_add=False)
    lugarrobo = models.CharField(max_length=200, blank=True)
    lugardenuncia = models.CharField(max_length=200, blank=True)
    telefonocontacto = models.CharField(max_length=200, blank=True)
    accesorios = models.CharField(max_length=200, blank=True)
    detalle = models.CharField(max_length=200, blank=True)
    recompensa = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)
    foto = models.FileField(upload_to='static/pic_folder/',
                             default='static/pic_folder/None/nophoto.gif')
    condicion = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        '''permite retornar el texto'''
        return self.correo
