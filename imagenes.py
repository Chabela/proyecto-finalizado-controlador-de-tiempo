import time

tiempo=2
while tiempo<20:
    lista=["imagenes/ubuntu1.jpg","imagenes/ubuntu2.jpg","imagenes/ubuntu3.jpg","imagenes/ubuntu4.jpg","imagenes/ubuntufinal.png"]
    aleatorio=random.randrange(1,len(lista))
    fondex=lista[aleatorio]
    print fondex
    time.sleep(2)
    tiempo+=2
