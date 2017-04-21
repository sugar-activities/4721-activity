#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, semilla
from control import Servicios

class SemillasFactory(object):
    """Using this class to return blocks with a copy of the images
        already loaded. No sense in re-loaded all the images for
        every block every time one is created."""
 
    def __init__(self):
        # load all our block images
        self.dirImagenes = os.path.join("imagenes", "paz")
        
        ancho=50
        imagen=Servicios.cargarImagen("Ico_Semilla.png", self.dirImagenes)
        altoImg = ancho * imagen.get_height() / imagen.get_width()
        
        self.images = {
                       
            0: pygame.transform.smoothscale(Servicios.cargarImagen("Ico_Semilla.png", self.dirImagenes), (ancho, altoImg)),
            1: pygame.transform.smoothscale(Servicios.cargarImagen("Ico_Semilla1.png", self.dirImagenes), (ancho, altoImg)),
            2: pygame.transform.smoothscale(Servicios.cargarImagen("Ico_Semilla2.png", self.dirImagenes), (ancho, altoImg)),
            3: pygame.transform.smoothscale(Servicios.cargarImagen("Ico_Semilla3.png", self.dirImagenes), (ancho, altoImg)),
            4: pygame.transform.smoothscale(Servicios.cargarImagen("Ico_Semilla4.png", self.dirImagenes), (ancho, altoImg)),
            5: pygame.transform.smoothscale(Servicios.cargarImagen("Ico_Semilla5.png", self.dirImagenes), (ancho, altoImg)),
            6: pygame.transform.smoothscale(Servicios.cargarImagen("Ico_Semilla6.png", self.dirImagenes), (ancho, altoImg)),
            7: pygame.transform.smoothscale(Servicios.cargarImagen("Ico_Semilla7.png", self.dirImagenes), (ancho, altoImg)),
            8: pygame.transform.smoothscale(Servicios.cargarImagen("Ico_Semilla8.png", self.dirImagenes), (ancho, altoImg))
        }
 
    def getSemilla(self):
        return semilla.Semilla(self.images)