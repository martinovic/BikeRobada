#!/usr/bin/python
# -*- coding: utf-8 -*-
__prj__ = 'BikeRobada'
__version__ = '1.0'
__license__ = ''
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = '2014/06/11'

import web
import json
import datetime
import psycopg2
import sys

urls = (
    '/query/(.*)/(.*)', 'query'
)

app = web.application(urls, globals())


class query:
    '''WEB Service para obtener datos sobre el estado de la bicicleta'''

    ip = "127.0.0.1"
    database = "bikerobada"
    user = "admin"
    password = "123456"

    def GET(self, cuadro, horquilla):
        ''''''
        print(("Iniciando..."))
        print(("Conectando a la base de datos."))
        print(("Ip.........: %s" % self.ip))
        print(("Database...: %s" % self.database))
        print(("=" * 80))
        con = psycopg2.connect(host=self.ip,
            database=self.database,
            user=self.user,
            password=self.password)

        cur = con.cursor()

        if len(cuadro) == 0:
            cuadro = 'none'

        if len(horquilla) == 0:
            horquilla = 'none'

        resultset = {}

        localTime = datetime.datetime.strftime(
            datetime.datetime.now(),
            "%Y%m%d%H%M%S")
        '''
         id
         correo
         marca
         modelo
         anioModelo
         tipo
         colores
         velocidades
         marcaVelocidades
         modeloVelocidades
         nrocuadro
         nrohorquilla
         fechaRobo
         lugarRobo
         lugarDenuncia
         telefonoContacto
         accesorios
         detalle
         recompensa
         activo
         foto
         condicion
        '''
        qry = ("select correo, " +
             "marca, " +
             "modelo, " +
             "aniomodelo, " +
             "tipo, " +
             "colores, " +
             "velocidades, " +
             "marcavelocidades, " +
             "modelovelocidades, " +
             "nrocuadro, " +
             "nrohorquilla, " +
             "fecharobo, " +
             "lugarrobo, " +
             "lugardenuncia, " +
             "telefonocontacto, " +
             "accesorios, " +
             "detalle, " +
             "recompensa, " +
             "activo, " +
             "foto, " +
             "condicion from " +
            "bicicletas_denuncias where " +
            "nrocuadro='" + cuadro + "' " +
            "or nrohorquilla='" + horquilla + "';")
        print(("-" * 80))
        print(("Buscando... cuadro: %s horquilla: %s" % (cuadro, horquilla)))
        cur.execute(qry)
        rows = cur.fetchall()
        mensaje = "OK"
        email = ""

        resultset = '{"resultset": '
        resultset += ('[{"mensaje": "%s", "email": "%s", ' %
                (mensaje, email))
        resultset += ('"localtime": "%s"}]}' % (localTime))

        for row in rows:
            mensaje = "ROBO"
            email = row[0]
            marca = row[1]
            modelo = row[2]
            anioModelo = row[3]
            tipo = row[4]
            colores = row[5]
            velocidades = row[6]
            marcaVelocidades = row[7]
            modeloVelocidades = row[8]
            nrocuadro = row[9]
            nrohorquilla = row[10]
            fechaRobo = datetime.datetime.strftime(row[11], '%Y-%m-%d')
            lugarRobo = row[12]
            lugarDenuncia = row[13]
            telefonoContacto = row[14]
            accesorios = row[15]
            detalle = row[16]
            recompensa = row[17]
            activo = row[18]
            foto = row[19]
            condicion = row[20]
            #print(activo)

            if recompensa is True:
                recompensa = "SI"
            else:
                recompensa = "NO"

            if activo is True:
                activo = "SI"
            else:
                activo = "NO"

            resultset = '{"resultset": '
            resultset += (
                '[{"mensaje": "%s", "email": "%s", "marca": "%s",' %
                (mensaje, email, marca))

            resultset += (
                '"modelo": "%s", "anioModelo": "%s", "tipo": "%s",' %
                (modelo, anioModelo, tipo))

            resultset += (
                '"colores": "%s", "velocidades": "%s", ' %
                (colores, velocidades))

            resultset += (
                '"marcaVelocidades": "%s", "modeloVelocidades": "%s",' %
                (marcaVelocidades, modeloVelocidades))

            resultset += (
                '"nrocuadro": "%s", "nrohorquilla": "%s",' %
                (nrocuadro, nrohorquilla))

            resultset += (
                '"fechaRobo": " %s", "lugarRobo": " %s",' %
                (fechaRobo, lugarRobo))

            resultset += (
                '"lugarDenuncia": "%s", "telefonoContacto": "%s",' %
                (lugarDenuncia, telefonoContacto))

            resultset += (
                '"accesorios": "%s", "detalle": " %s",' %
                (accesorios, detalle))

            resultset += (
                '"recompensa": "%s", "activo": "%s",' %
                (recompensa, activo))

            resultset += (
                '"foto": "%s","condicion": "%s", "localtime": "%s"}]}' %
                (foto, condicion, localTime))
        print(("Resultado:"))
        print((resultset))
        print(("\n\n"))
        return resultset

if __name__ == "__main__":
    app.run()
