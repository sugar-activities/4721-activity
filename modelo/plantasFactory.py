#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, planta
from control import Servicios


class PlantasFactory(object):
    """Using this class to return blocks with a copy of the images
        already loaded. No sense in re-loaded all the images for
        every block every time one is created."""
 
    def __init__(self):
        # load all our block images
        
        self.dirImagenes = os.path.join("imagenes", "paz")
        ancho = 80
        self.image = Servicios.cargarImagen("Ico_Retono.png", self.dirImagenes)
        altoImg = ancho * self.image.get_height() / self.image.get_width()
        self.image = pygame.transform.smoothscale(self.image, (ancho, altoImg))
 
    def getPlanta(self):
        return planta.Planta(self.image)
