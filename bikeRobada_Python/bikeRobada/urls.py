from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from smarturls import surl
from django.conf.urls import patterns, url, include

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bikeRobada.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #Pagina principal
    surl('/', 'bikeRobada.views.home', name='home'),

    #url(r'^denuncias/', include('bicicletas.urls')),
    surl('/denuncias/index/', 'bicicletas.views.index'),
    surl('/denuncias/append_denuncias/', 'bicicletas.views.append_denuncias'),
    surl('/denuncias/verifica_denuncias/', 'bicicletas.views.verifica_denuncias'),
    surl('/denuncias/comfirma_denuncias/', 'bicicletas.views.comfirma_denuncias'),
    surl('/denuncias/save_denuncias/', 'bicicletas.views.save_denuncias'),
    surl('/denuncias/view_denuncia/', 'bicicletas.views.view_denuncia'),
    surl('/denuncias/busquedas_index/', 'bicicletas.views.busquedas_index'),
    surl('/denuncias/viewEvent/', 'bicicletas.views.viewEvent'),
    surl('/denuncias/informacion/', 'bicicletas.views.informacion'),
    surl('/denuncias/consejos/', 'bicicletas.views.consejos_index'),
    surl('/denuncias/test/', 'bicicletas.views.testForms'),
    surl('/recuperada/index/', 'bicicletas.views.recuperada_index'),
    url(r'^recuperada/baja/(?P<correo>[a-zA-Z.@_]+)/(?P<verificacion>\w+)',
        'bicicletas.views.baja_recuperada',
        name="ver"),
    surl('/recuperada/aviso_recuperada/', 'bicicletas.views.aviso_recuperada'),
    surl('/contacto/index/', 'bicicletas.views.contacto_index'),
    surl('/participantes/index/', 'participantes.views.index'),
)
