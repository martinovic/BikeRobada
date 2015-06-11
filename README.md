# BikeRobada

BikeRobada es una app compuesta de 2 partes, Android y Django, permite hacer denuncias de robos de bicicletas y saber por medio de una app android si la bicicleta que compramos es robada o no.

El componente WEB esta desarrollado en Python usando el framework DJANGO. La parte Android esta preparada para ser corrido en KitKat, se comunican a la base de datos, en esta oprtunidad Postgresql, por medio de una muy pequeña app de REST.

La app REST esta separada de DJANGO para poder dar independencia de servidores (por ahora).

