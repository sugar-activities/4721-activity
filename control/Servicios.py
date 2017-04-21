#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, sys

def reajustarCoord(coord, anchoAltoVentana, anchoAltoImagen):
    porcentajeReajuste = anchoAltoVentana / float(anchoAltoImagen)
    coordenada = coord * float(porcentajeReajuste)
    return float(coordenada)

def cargarImagen(nombre, dir_imagen, alpha=True):
    '''encontrar la ruta completa de la imagen'''
    ruta = os.path.join(dir_imagen, nombre)
    try:
        imagen = pygame.image.load(ruta)
    except :
        print "Error, no se puede cargar la imagen: ", ruta
        sys.exit(1)
    '''Comprobar si la imagen tiene transparencia (PNG)'''
        
    if alpha == True:
        imagen = imagen.convert_alpha()
    else:
        imagen = imagen.convert()
    
    return imagen
        
def cargarSonido(nombre, dir_sonido):
    ruta = os.path.join(dir_sonido, nombre)
    # Intentar cargar el sonido
    try:
        sonido = pygame.mixer.Sound(ruta)
    except pygame.error, message:
        print "No se pudo cargar el sonido: ", ruta
        sonido = None
    return sonido


