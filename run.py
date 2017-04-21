#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-
import pygame
from vista import MenuPrincipal, VentanaPrueba, Karaoke
from modelo import Cursor

ANCHO_VENTANA = 1200
ALTO_VENTANA = 825  # 900 - 75

def main():
    
    pygame.init()
    
    pygame.mixer.init()
    
    screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), 0, 32)
    
    pygame.display.set_caption("Valorar")
    
    clock = pygame.time.Clock()
    
    cursor = Cursor.Cursor()
    
    menu = MenuPrincipal.MenuPrincipal(cursor, screen, clock, ANCHO_VENTANA, ALTO_VENTANA)
    
    #menu = VentanaPrueba.MenuPrincipal(cursor, screen, clock, ANCHO_VENTANA, ALTO_VENTANA)
    
    menu.run()
    
    
    

if __name__ == "__main__":
    main()
