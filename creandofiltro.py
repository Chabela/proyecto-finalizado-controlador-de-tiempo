import panta
import sys
import os
import time
try:
    import pygtk
    require('2.0')
except:
    pass
try:
    import gtk
    from gtk import glade
    
except:
    print "no tienes el modulo instalado"
    time.sleep(2)
    sys.exit(1)

def ventanaaviso(tiempo):
    ventana=gtk.Window(gtk.WINDOW_TOPLEVEL)
    ventana.resize(200,200)
    fijo=gtk.Fixed()
    etiqueta=gtk.Label(tiempo)
    etiqueta.show()
    boton=gtk.Button()
    boton.show()
    fijo.add(boton)
    ventana.add(fijo)
    ventana.show()
    print "ya"
    
ventanaaviso(2)
