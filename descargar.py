from pytube import YouTube
from tkinter import *
from tkinter.ttk import *

def descargar():
    link = videos.get()
    vid = YouTube(link)
    
    #TITULO
    titulo1 = vid.title
    titulo = "NOMBRE: {}".format(titulo1) 
    titven = Label(ventana, text=titulo)
    titven.grid(row=2, column=0) 

    #DURACIÓN
    duracion = vid.length
    horas = duracion // 3600
    minutos = (duracion % 3600) // 60
    segundos = duracion % 60
    time_format = "DURACIÓN: {:.0f}h:{:.0f}m:{}s".format(horas, minutos, segundos)
    durven = Label(ventana, text=time_format)
    durven.grid(row=3, column=0)

    # Crear la barra de progreso
    ventana.update()
    
    # Descargar el archivo
    descarga = vid.streams.get_highest_resolution()
    descarga.download()
    print("**DESCARGA FINALIZADA**\n{}\n{}".format(titulo, time_format))
    print("***********************\n")


#https://www.youtube.com/watch?v=JDcvtKsSfxg

#VENTANA GENERAL
ventana = Tk()
ventana.config(bd=15)
ventana.title("Descargar Videos de Youtube")

#ENTRADA DE TEXTO
videos = Entry(ventana)
videos.grid(row=1, column=2)

#BARRA SUPERIOR
menubar = Menu(ventana)
ventana.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Info", menu = helpmenu )
menubar.add_command(label="Salir", command=ventana.destroy)

#IMAGEN
imagen = PhotoImage(file="img/youd.png")
foto = Label(ventana, image=imagen)
foto.grid(row=0, column=0)

#barra de descarga
#progressbar = Progressbar(ventana, length=200, maximum=100, mode="determinate")
#progressbar.grid(row=4, column=0)

#INFO
info = Label(ventana, text="VIDEO: ")
info.grid(row=1, column=0)

#INSTRUCCIONES
instrucciones = Label(ventana, text="Descargar Videos")
instrucciones.grid(row=0, column=2)

#BOTON
boton = Button(ventana, text="DESCARGAR", command=descargar)
boton.grid(row=2, column=2)

ventana.mainloop()