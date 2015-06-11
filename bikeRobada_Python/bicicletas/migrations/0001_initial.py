# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('correo', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('aniomodelo', models.CharField(max_length=4, blank=True)),
                ('tipo', models.CharField(default=b'MTB', max_length=40, choices=[(b'MTB', b'MTB'), (b'CARRETERA', b'CARRETERA'), (b'CICLOCROSS', b'CICLOCROSS'), (b'PASEO', b'PASEO'), (b'INFANTIL', b'INFANTIL'), (b'ANTIGUA', b'ANTIGUA'), (b'TRIAL', b'TRIAL'), (b'FREESTYLE', b'FREESTYLE'), (b'URBANA', b'URBANA'), (b'BMX', b'BMX'), (b'CARGO', b'CARGO'), (b'CUSTOM', b'CUSTOM'), (b'CRUISER', b'CRUISER'), (b'PISTA', b'PISTA'), (b'TANDEM', b'TANDEM'), (b'FIXED', b'FIXED'), (b'PLEGABLE', b'PLEGABLE'), (b'ELECTRICA', b'ELECTRICA')])),
                ('colores', models.CharField(max_length=200)),
                ('velocidades', models.CharField(max_length=100, blank=True)),
                ('marcavelocidades', models.CharField(max_length=100, blank=True)),
                ('modelovelocidades', models.CharField(max_length=100, blank=True)),
                ('nrocuadro', models.CharField(max_length=20, blank=True)),
                ('nrohorquilla', models.CharField(max_length=20, blank=True)),
                ('fecharobo', models.DateField()),
                ('lugarrobo', models.CharField(max_length=200, blank=True)),
                ('lugardenuncia', models.CharField(max_length=200, blank=True)),
                ('telefonocontacto', models.CharField(max_length=200, blank=True)),
                ('accesorios', models.CharField(max_length=200, blank=True)),
                ('detalle', models.CharField(max_length=200, blank=True)),
                ('recompensa', models.BooleanField(default=True)),
                ('activo', models.BooleanField(default=True)),
                ('foto', models.FileField(default=b'static/pic_folder/None/nophoto.gif', upload_to=b'static/pic_folder/')),
                ('condicion', models.CharField(max_length=200, blank=True)),
            ],
        ),
    ]
