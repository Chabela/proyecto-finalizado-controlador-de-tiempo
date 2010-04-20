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

class time:
	
    def __init__(self):
        
        self.gladefile="tiempo.glade"
        self.conjuntos=gtk.glade.XML(self.gladefile)
        self.ventanaIngreso=self.conjuntos.get_widget("VentanaPrincipal")
        self.ventanaAviso=self.conjuntos.get_widget("ventanaaviso")
        self.diccionario={"on_BotonEnvio_clicked":self.on_BotonEnvio_clicked,
                          "on_botonconteo_clicked":self.on_botonconteo_clicked}
        self.conjuntos.signal_autoconnect(self.diccionario)
        self.ingresoTiempo=self.conjuntos.get_widget("EntradaDeTiempo")
        self.etiquetaconteo=self.conjuntos.get_widget("etiquetaconteo")
        
    def on_BotonEnvio_clicked(self,widget):
        self.ventanaIngreso.destroy()
        import time
        tiempo=self.ingresoTiempo.get_text()
        self.tiempo=int(tiempo)
        while gtk.events_pending():
            gtk.main_iteration()
            time.sleep(1)
            print self.tiempo
            self.tiempo-=1
            if self.tiempo==5:
                self.aviso()
        panta.p()
        
    def aviso(self):
        self.ventanaAviso.show()
        import time
        b=6
        while gtk.events_pending():
            gtk.main_iteration()
            time.sleep(1)
            b-=1
            self.etiquetaconteo.set_text(str(b))
            print b
            if b==-1:
                self.etiquetaconteo.set_text("GOOD BYE")
                time.sleep(1)
                break
            else:
                pass

            
        print "GOOD BYE"

    def on_BotonAdmin_clicked(self,widget):
        self.ventanaSuspension.destroy()
        
    def on_botonconteo_clicked(self,widget):
        self.ventanaAviso.destroy()
if __name__=="__main__":
    timetime=time()
    gtk.main()
