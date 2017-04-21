#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-
import pygame, os, Boton
from control import resource, Servicios

class MensajeInicial(pygame.sprite.Sprite):
    # x y y son las coordenadas donde inicia el texto
    def __init__(self, tamLetra, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.tipo = tipo
        resource.set_images_path(os.path.join("imagenes"))
        if self.tipo == "Tablero":
            self.imagen = Servicios.cargarImagen("Pantalla_Intro.png", "imagenes")
        if self.tipo == "Silencio":
            self.imagen = Servicios.cargarImagen("Pantalla_Silencio.png", "imagenes")
        if self.tipo == "Cita":
            self.imagen = Servicios.cargarImagen("Pantalla_Citas.png", "imagenes")
        if self.tipo == "Canto":
            self.imagen = Servicios.cargarImagen("Pantalla_Karaoke.png", "imagenes")
        if self.tipo == "CuentoAmor" or self.tipo == "CuentoRectitud" or self.tipo == "CuentoPaz" or self.tipo == "CuentoVerdad" or self.tipo == "CuentoNoViolencia":
            self.imagen = Servicios.cargarImagen("Pantalla_Cuento.png", "imagenes")
            
        if self.tipo =="Compartir":
            self.imagen = resource.get_image("Pantalla_Compartir.png")
        if self.tipo =="Compartir2":
            self.imagen = resource.get_image("Pantalla_Compartir.png")
        if self.tipo =="Compartir3":
            self.imagen = resource.get_image("Pantalla_Compartir.png")
        if self.tipo =="Compartir4":
            self.imagen = resource.get_image("Pantalla_Compartir.png")
        
        self.x = 600 - (self.imagen.get_width() / 2)
        self.y = 412 - (self.imagen.get_height() / 2)
        self.xTexto = 61
        self.yTexto = 100
        self.tamLetra = 35
        self.visible = False
        self.transparente = resource.get_image("transparente.png")
        
        imgBtn = resource.get_image("boton_continuar.png")
        imgBtnSelec = resource.get_image("boton_continuar_selec.png")
        self.btn = Boton.Boton(imgBtn, imgBtnSelec, -100, -100)
        self.initFont()
        self.initImage(self.imagen)
        self.interlineado = 0.9


    def initFont(self):
        pygame.font.init()
        rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
        self.font = pygame.font.Font(rutaFuente, self.tamLetra)  # tamaño de la fuente

    def initImage(self, imagen):
        self.image = imagen  # tamaño del campo de texto
        self.rect = self.image.get_rect()
        self.rect.top = 0 ; self.rect.left = 0
        self.rect2 = self.image.get_rect()
        self.rect2.top = self.y ; self.rect2.left = self.x
        
    def setVisible(self, visible):
        self.visible = visible

            
    def update(self, pantalla, cursor):
        if self.visible:
            
            if self.tipo == "Tablero":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render(u"Una gran niebla de tristeza y mal humor", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render(u"ha caído sobre tu planeta. Las personas", True, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render(u"viven muy agresivas, se pelean entre sí", True, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea4 = self.font.render("y arruinan la naturaleza...", True, (0, 0, 0))
                self.image.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea6 = self.font.render("En medio de este mundo gris, los valores", True, (0, 0, 0))
                self.image.blit(linea6, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea7 = self.font.render("han desaparecido...", True, (0, 0, 0))
                self.image.blit(linea7, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea8 = self.font.render(u"Tú has sido elegido para recuperar los", True, (0, 0, 0))
                self.image.blit(linea8, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea9 = self.font.render("valores perdidos. Si los encuentras", True, (0, 0, 0))
                self.image.blit(linea9, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea10 = self.font.render(u"podrás devolverle la alegría a las", True, (0, 0, 0))
                self.image.blit(linea10, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea11 = self.font.render("personas, colorear de vida el planeta", True, (0, 0, 0))
                self.image.blit(linea11, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea12 = self.font.render("y ahuyentar la niebla...", True, (0, 0, 0))
                self.image.blit(linea12, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea14 = self.font.render("Es hora de encontrar el valor perdido...", True, (0, 0, 0))
                self.image.blit(linea14, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "CuentoAmor":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Debes encontrar el valor AMOR. El", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render("silencio te ha contado que lo ha visto", True, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render("en un bosque llamado AMORETO.", True, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea4 = self.font.render("Pero ahora el lugar se encuentra lleno", True, (0, 0, 0))
                self.image.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea5 = self.font.render("de basura.", True, (0, 0, 0))
                self.image.blit(linea5, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea7 = self.font.render("Para hallar al Amor debes convertir a", True, (0, 0, 0))
                self.image.blit(linea7, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea8 = self.font.render("los monstruos de la basura en corazones.", True, (0, 0, 0))
                self.image.blit(linea8, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea9 = self.font.render(u"Sólo lo lograrás si a pesar de su aspecto", True, (0, 0, 0))
                self.image.blit(linea9, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea10 = self.font.render("monstruoso los puedes amar. Si tu amor", True, (0, 0, 0))
                self.image.blit(linea10, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea11 = self.font.render("no es fuerte vuelves a empezar.", True, (0, 0, 0))
                self.image.blit(linea11, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea14 = self.font.render(u"Si lo consigues estarás más cerca de", True, (0, 0, 0))
                self.image.blit(linea14, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea15 = self.font.render("reunir los valores perdidos...", True, (0, 0, 0))
                self.image.blit(linea15, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
            
            if self.tipo == "CuentoRectitud":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Vas de paseo con tus amigos al bosque ", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render("AMORETO. Y al llegar lo encuentras", True, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render(u"lleno de basura.", True, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea6 = self.font.render(u"Es así que decides quedarte a limpiarlo.", True, (0, 0, 0))
                self.image.blit(linea6, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea7 = self.font.render("Recuerda que tienes poco tiempo para ", True, (0, 0, 0))
                self.image.blit(linea7, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea8 = self.font.render(u"lograrlo. Hazlo así: El plástico en la ", True, (0, 0, 0))
                self.image.blit(linea8, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea9 = self.font.render("caneca naranja, el papel en la caneca", True, (0, 0, 0))
                self.image.blit(linea9, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea11 = self.font.render("azul y el vidrio en la caneca verde.", True, (0, 0, 0))
                self.image.blit(linea11, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea12 = self.font.render("Si no lo logras debes iniciar de nuevo,", True, (0, 0, 0))
                self.image.blit(linea12, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea16 = self.font.render(u"y si lo haces estarás muy cerca de", True, (0, 0, 0))
                self.image.blit(linea16, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea17 = self.font.render("recuperar el valor perdido.", True, (0, 0, 0))
                self.image.blit(linea17, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "CuentoPaz":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render(u"Ahora que has limpiado el bosque", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea1 = self.font.render("AMORETO te das cuenta que no hay", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render(u"árboles ni flores.", True, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea4 = self.font.render("Has sido premiado con el don de sembrar.", True, (0, 0, 0))
                self.image.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea5 = self.font.render("Se te han entregado muchas semillas", True, (0, 0, 0))
                self.image.blit(linea5, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea6 = self.font.render(u"que aparecen con un número que debes", True, (0, 0, 0))
                self.image.blit(linea6, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea8 = self.font.render("memorizar.", True, (0, 0, 0))
                self.image.blit(linea8, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea9 = self.font.render(u"Para sembrarlas debes dar click sobre", True, (0, 0, 0))
                self.image.blit(linea9, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea10 = self.font.render(u"el número de cada semilla. Cada vez que", True, (0, 0, 0))
                self.image.blit(linea10, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea11 = self.font.render(u"siembras aparecerán más semillas y", True, (0, 0, 0))
                self.image.blit(linea11, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea12 = self.font.render(u"así podrás llenar el bosque de árboles", True, (0, 0, 0))
                self.image.blit(linea12, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea13 = self.font.render(u"nuevamente.", True, (0, 0, 0))
                self.image.blit(linea13, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "CuentoVerdad":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Una tarde de sol has decidido caminar", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render(u"por el lugar más misterioso del bosque", True, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render(u"AMORETO, el laberinto.", True, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea4 = self.font.render(u"Para salir de allí, tienes que convertir", True, (0, 0, 0))
                self.image.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea5 = self.font.render("las mentiras en verdad. Las estrellas", True, (0, 0, 0))
                self.image.blit(linea5, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea6 = self.font.render(u"grandes de luz te guiarán. Alcánzalas", True, (0, 0, 0))
                self.image.blit(linea6, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea8 = self.font.render(u"todas y a tu familia podrás guiar.", True, (0, 0, 0))
                self.image.blit(linea8, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea12 = self.font.render("Si alguna mentira te alcanza debes", True, (0, 0, 0))
                self.image.blit(linea12, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea13 = self.font.render("volver a empezar.", True, (0, 0, 0))
                self.image.blit(linea13, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "CuentoNoViolencia":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Tu familia te ha elegido para que seas", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render(u"el guía de un viaje al valle de la", True, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render(u"reconciliación. Este es un lugar donde no ", True, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea5 = self.font.render(u"existe la violencia.", True, (0, 0, 0))
                self.image.blit(linea5, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea6 = self.font.render(u"El camino no es fácil, además el mapa", True, (0, 0, 0))
                self.image.blit(linea6, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea7 = self.font.render(u"está hecho pedazos. Depende de ti que", True, (0, 0, 0))
                self.image.blit(linea7, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea8 = self.font.render("puedan llegar. Para lograrlo debes unir", True, (0, 0, 0))
                self.image.blit(linea8, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea9 = self.font.render("las partes hasta armar el mapa.", True, (0, 0, 0))
                self.image.blit(linea9, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea10 = self.font.render(u"De lo contrario tú y tu familia no", True, (0, 0, 0))
                self.image.blit(linea10, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea11 = self.font.render(u"podrán llegar.", True, (0, 0, 0))
                self.image.blit(linea11, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
            
            if self.tipo == "Cita":
                
                # self.setText("Encuentra el camino que contiene la frase secreta, para lograrlo selecciona las piedras pulsándolas con el mouse. Recuerda que el camino debe ir de inicio a fin. Puedes utilizar el botón de limpiar para reiniciar el camino. ¡Buena Suerte!")
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Encuentra el camino que contiene", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render("la frase secreta, para lograrlo", True, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render(u"selecciona las piedras pulsándolas", True, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea4 = self.font.render("con el mouse.", True, (0, 0, 0))
                self.image.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea5 = self.font.render("Ten en cuenta que el camino debe", True, (0, 0, 0))
                self.image.blit(linea5, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea6 = self.font.render("ir de inicio a fin.", True, (0, 0, 0))
                self.image.blit(linea6, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea7 = self.font.render(u"Puedes utilizar el botón de limpiar", True, (0, 0, 0))
                self.image.blit(linea7, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea8 = self.font.render("para reiniciar el camino.", True, (0, 0, 0))
                self.image.blit(linea8, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea9 = self.font.render(u"¡Buena suerte!", True, (0, 0, 0))
                self.image.blit(linea9, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "Canto":
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Ahora debes cantar siguiendo la", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render(u"melodía mostrada en el karaoke.", True, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render(u"Cuando la canción termine presiona", True, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea4 = self.font.render(u"el botón continuar.", True, (0, 0, 0))
                self.image.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "Silencio":
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Guarda silencio mientras observas", True, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render("la mandala que se te muestra en la", True, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render("pantalla. Memoriza los colores...", True, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea4 = self.font.render(u"Después tendrás que colorearla.", True, (0, 0, 0))
                self.image.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo=="Compartir":
                x_pos = self.rect.left + self.xTexto + 229
                y_pos = self.rect.top + self.yTexto + 55
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render(u"Comparte con tus compañeros", True, (0, 0, 0))
                pantalla.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea2 = self.font.render(u"un cuento, una canción o una cita", True, (0, 0, 0))
                pantalla.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                
                self.btn.setCoord(440, y_pos + self.y + 90)
                self.btn.update(pantalla, cursor)
                
            if self.tipo=="Compartir2":
                x_pos = self.rect.left + self.xTexto + 229
                y_pos = self.rect.top + self.yTexto + 55
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render(u"Si quieres compartir con tus compañeros", True, (0, 0, 0))
                pantalla.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea2 = self.font.render(u"no dejes el mensaje sin diligenciar", True, (0, 0, 0))
                pantalla.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                
                self.btn.setCoord(440, y_pos + self.y + 90)
                self.btn.update(pantalla, cursor)
                
            if self.tipo=="Compartir3":
                x_pos = self.rect.left + self.xTexto + 229
                y_pos = self.rect.top + self.yTexto + 55
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Tu mensaje no fue enviado exitosamente. ", True, (0, 0, 0))
                pantalla.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea2 = self.font.render(u"Revisa tu conexión a internet e intenta de", True, (0, 0, 0))
                pantalla.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea3 = self.font.render("nuevo.", True, (0, 0, 0))
                pantalla.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                
                self.btn.setCoord(440, y_pos + self.y + 90)
                self.btn.update(pantalla, cursor)
                
            if self.tipo=="Compartir4":
                x_pos = self.rect.left + self.xTexto + 229
                y_pos = self.rect.top + self.yTexto + 55
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Tu mensaje fue enviado exitosamente. ", True, (0, 0, 0))
                pantalla.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea2 = self.font.render(u"Visita la pagina valorar.somee.com", True, (0, 0, 0))
                pantalla.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea3 = self.font.render(u"y encuentra lo que otros compañeros", True, (0, 0, 0))
                pantalla.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea4 = self.font.render("han compartido", True, (0, 0, 0))
                pantalla.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                
                self.btn.setCoord(440, y_pos + self.y + 90)
                self.btn.update(pantalla, cursor)
                
class MensajeGanaste(pygame.sprite.Sprite):
    # x y y son las coordenadas donde inicia el texto
    def __init__(self, tamLetra, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.tipo = tipo
        resource.set_images_path(os.path.join("imagenes"))
        self.imagen = Servicios.cargarImagen("Pantalla_Ganaste.png", "imagenes")
        self.imagen2 = Servicios.cargarImagen("Pantalla_Ganaste_GR.png", "imagenes")

        self.x = 600 - (self.imagen.get_width() / 2)
        self.y = 412 - (self.imagen.get_height() / 2)
        self.xTexto = 70
        self.yTexto = 95
        self.tamLetra = 30
        self.visible = False
        self.transparente = resource.get_image("transparente.png")
        
        imgBtn = resource.get_image("boton_terminar.png")
        imgBtnSelec = resource.get_image("boton_terminar_selec.png")
        self.btn = Boton.Boton(imgBtn, imgBtnSelec, -100, -100)
        self.initFont()
        self.initImage(self.imagen)
        self.interlineado = 0.9


    def initFont(self):
        pygame.font.init()
        rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
        self.font = pygame.font.Font(rutaFuente, self.tamLetra)  # tamaño de la fuente
        
    def initImage(self, imagen):
        self.image = imagen  # tamaño del campo de texto
        self.rect = self.image.get_rect()
        self.rect.top = 0 ; self.rect.left = 0
        self.rect2 = self.image.get_rect()
        self.rect2.top = self.y ; self.rect2.left = self.x
        
    def setVisible(self, visible):
        self.visible = visible

            
    def update(self, pantalla, cursor):
        if self.visible:
            
            if self.tipo == "Silencio":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea2 = self.font.render("Has coloreado la mandala", False, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render("correctamente.", False, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)

            
            if self.tipo == "JuegoAmor":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea2 = self.font.render("Has logrado atravesar el basurero", False, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render("hasta el otro extremo.", False, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "JuegoRectitud":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea2 = self.font.render("Has logrado recoger y colocar", False, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render("la basura en las canecas correctas.", False, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "JuegoPaz":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea2 = self.font.render("Has logrado sembrar las semillas", False, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render("adecuadamente.", False, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "JuegoVerdad":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea2 = self.font.render("Has logrado recoger todas", False, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render("las monedas.", False, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "JuegoNoViolencia":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea2 = self.font.render("Has logrado solucionar el", False, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                linea3 = self.font.render("rompecabezas.", False, (0, 0, 0))
                self.image.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
            
            if self.tipo=="CitaAmor":
                
                
                self.x = 600 - (self.imagen2.get_width() / 2)
                self.y = 412 - (self.imagen2.get_height() / 2)
                self.xTexto = 70
                self.yTexto = 115
                self.initImage(self.imagen2)
                
                
                x_pos = self.rect.left + self.xTexto + 230
                y_pos = self.rect.top + self.yTexto + 50
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Encontraste la cita:", True, (0, 0, 0))
                pantalla.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea2 = self.font.render("Nadie tiene dominio sobre el", True, (0, 0, 0))
                pantalla.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea3 = self.font.render("amor, pero el amor domina todas", True, (0, 0, 0))
                pantalla.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea4 = self.font.render("las cosas.", True, (0, 0, 0))
                pantalla.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea5 = self.font.render("                     - Jean De La Fontaine", True, (0, 0, 0))
                pantalla.blit(linea5, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1

                
                self.btn.setCoord(425, y_pos + self.y+28)
                self.btn.update(pantalla, cursor)
                
            if self.tipo=="CitaRectitud":
                
                self.x = 600 - (self.imagen2.get_width() / 2)
                self.y = 412 - (self.imagen2.get_height() / 2)
                self.xTexto = 70
                self.yTexto = 115
                self.initImage(self.imagen2)
                
                x_pos = self.rect.left + self.xTexto + 230
                y_pos = self.rect.top + self.yTexto + 50
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Encontraste la cita:", True, (0, 0, 0))
                pantalla.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea2 = self.font.render(u"Si hay rectitud en el corazón,", True, (0, 0, 0))
                pantalla.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea3 = self.font.render(u"habrá belleza en el carácter.", True, (0, 0, 0))
                pantalla.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea4 = self.font.render("                         - Sai Sathya Baba", True, (0, 0, 0))
                pantalla.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                
                self.btn.setCoord(425, y_pos + self.y+28)
                self.btn.update(pantalla, cursor)
                
            if self.tipo=="CitaPaz":
                
                self.x = 600 - (self.imagen2.get_width() / 2)
                self.y = 412 - (self.imagen2.get_height() / 2)
                self.xTexto = 70
                self.yTexto = 115
                self.initImage(self.imagen2)
                
                x_pos = self.rect.left + self.xTexto + 230
                y_pos = self.rect.top + self.yTexto + 50
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Encontraste la cita:", True, (0, 0, 0))
                pantalla.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea2 = self.font.render("No hay camino para la paz, la", True, (0, 0, 0))
                pantalla.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea3 = self.font.render("paz es el camino.", True, (0, 0, 0))
                pantalla.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea4 = self.font.render("                          - Mahatma Gandhi", True, (0, 0, 0))
                pantalla.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                
                self.btn.setCoord(425, y_pos + self.y+28)
                self.btn.update(pantalla, cursor)
                
            if self.tipo=="CitaVerdad":
                
                self.x = 600 - (self.imagen2.get_width() / 2)
                self.y = 412 - (self.imagen2.get_height() / 2)
                self.xTexto = 70
                self.yTexto = 115
                self.initImage(self.imagen2)
                
                x_pos = self.rect.left + self.xTexto + 230
                y_pos = self.rect.top + self.yTexto + 50
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Encontraste la cita:", True, (0, 0, 0))
                pantalla.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea2 = self.font.render("Conocereis la Verdad y la", True, (0, 0, 0))
                pantalla.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea3 = self.font.render(u"Verdad os hará libres.", True, (0, 0, 0))
                pantalla.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea4 = self.font.render(u"                    - Jesús de Nazareth", True, (0, 0, 0))
                pantalla.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                
                self.btn.setCoord(425, y_pos + self.y+28)
                self.btn.update(pantalla, cursor)
                
            if self.tipo=="CitaNoViolencia":
                
                self.x = 600 - (self.imagen2.get_width() / 2)
                self.y = 412 - (self.imagen2.get_height() / 2)
                self.xTexto = 70
                self.yTexto = 115
                self.initImage(self.imagen2)
                
                x_pos = self.rect.left + self.xTexto + 230
                y_pos = self.rect.top + self.yTexto + 50
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render("Encontraste la cita:", True, (0, 0, 0))
                pantalla.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea2 = self.font.render("La persona que se lastima", True, (0, 0, 0))
                pantalla.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea3 = self.font.render(u"a sí misma no podrá evitar", True, (0, 0, 0))
                pantalla.blit(linea3, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                linea4 = self.font.render(u"dañar a otros.", True, (0, 0, 0))
                pantalla.blit(linea4, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                linea5 = self.font.render("                         - Sai Sathya Baba", True, (0, 0, 0))
                pantalla.blit(linea5, (x_pos, y_pos))
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                y_pos += self.tamLetra * 1.1
                
                self.btn.setCoord(425, y_pos + self.y+28)
                self.btn.update(pantalla, cursor)
                
class MensajePerdiste(pygame.sprite.Sprite):
    # x y y son las coordenadas donde inicia el texto
    def __init__(self, tamLetra, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.tipo = tipo
        resource.set_images_path(os.path.join("imagenes"))
        self.imagen = Servicios.cargarImagen("Pantalla_Perdiste.png", "imagenes")

        self.x = 600 - (self.imagen.get_width() / 2)
        self.y = 412 - (self.imagen.get_height() / 2)
        self.xTexto = 70
        self.yTexto = 90
        self.tamLetra = 30
        self.visible = False
        self.transparente = resource.get_image("transparente.png")
        
        imgBtn = resource.get_image("boton_continuar.png")
        imgBtnSelec = resource.get_image("boton_continuar_selec.png")
        self.btn = Boton.Boton(imgBtn, imgBtnSelec, -100, -100)
        self.initFont()
        self.initImage(self.imagen)
        self.interlineado = 0.9


    def initFont(self):
        pygame.font.init()
        rutaFuente = os.path.join("fuentes", "PatrickHand-Regular.ttf")
        self.font = pygame.font.Font(rutaFuente, self.tamLetra)  # tamaño de la fuente

    def initImage(self, imagen):
        self.image = imagen  # tamaño del campo de texto
        self.rect = self.image.get_rect()
        self.rect.top = 0 ; self.rect.left = 0
        self.rect2 = self.image.get_rect()
        self.rect2.top = self.y ; self.rect2.left = self.x
        
    def setVisible(self, visible):
        self.visible = visible

            
    def update(self, pantalla, cursor):
        
        if self.visible:
            
            if self.tipo == "JuegoAmor" or self.tipo == "JuegoVerdad":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render(u"Inténtalo de nuevo.", False, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render("Has sido atrapado por un monstruo.", False, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado/2
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "JuegoRectitud":
                pass
                
            if self.tipo == "JuegoPaz":
                
                x_pos = self.rect.left + self.xTexto
                y_pos = self.rect.top + self.yTexto
                pantalla.blit(self.transparente, (0, 0))
                pantalla.blit(self.image, (self.x, self.y))
                linea1 = self.font.render(u"Inténtalo de nuevo.", False, (0, 0, 0))
                self.image.blit(linea1, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado
                linea2 = self.font.render("El orden que seleccionaste no es el correcto", False, (0, 0, 0))
                self.image.blit(linea2, (x_pos, y_pos))
                y_pos += self.tamLetra * self.interlineado
                y_pos += self.tamLetra * self.interlineado/2
                
                self.btn.setCoord(440, y_pos + self.y)
                self.btn.update(pantalla, cursor)
                
            if self.tipo == "JuegoNoViolencia":
                pass
                