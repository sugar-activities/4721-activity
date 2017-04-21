#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, piedra, os
from control import Servicios, resource

class PiedraFactory(object):
    """Using this class to return blocks with a copy of the images
        already loaded. No sense in re-loaded all the images for
        every block every time one is created."""
 
    def __init__(self):
        # load all our block images
        
        self.dirImagenes = os.path.join("imagenes", "citas")
        resource.set_images_path(self.dirImagenes)
        
        self.images = {
            0: resource.get_image("PlantaAgua-01.png"),
            1: resource.get_image("PlantaAgua_selec.png"),
            2: resource.get_image("PlantaAgua_01selec.png")
        }
 
    def getPiedra(self,x,y,letra,numero):
        return piedra.Piedra(self.images,x,y,letra,numero)