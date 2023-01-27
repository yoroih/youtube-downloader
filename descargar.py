from pytube import YouTube, Playlist
from tkinter import *
from tkinter.ttk import *

def descargar():
    link = videos.get()
    video = YouTube(link)
    
    #TITULO
    titulo1 = video.title
    titulo = "NOMBRE: {}".format(titulo1) 
    titulolabel = Label(ventana, text=titulo)
    titulolabel.grid(row=4, column=2) 

    #DURACIÓN
    duracion = video.length
    horas = duracion // 3600
    minutos = (duracion % 3600) // 60
    segundos = duracion % 60
    time_format = "DURACIÓN: {:.0f}h:{:.0f}m:{}s".format(horas, minutos, segundos)
    durven = Label(ventana, text=time_format)
    durven.grid(row=5, column=2)

    # Crear la barra de progreso
    ventana.update()
    
    # Descargar el archivo
    descarga = video.streams.get_highest_resolution()
    #descarga.download()
    print("**DESCARGA FINALIZADA**\n{}\n{}".format(titulo, time_format))
    print("***********************\n")

def descargarplaylist():
    linkplaylist = videos.get()
    videoplaylist = Playlist(linkplaylist)

    #NOMBRE DE PLAYLIST
    nombreplaylist = videoplaylist.title
    nombreplaylist = "NOMBRE DE PLAYLIST: {}".format(nombreplaylist)
    labelnombreplaylist = Label(ventana, text=nombreplaylist)
    labelnombreplaylist.grid(row=4, column=2) 

    ventana.update()

    #obtener nombres de videos por terminal
    for listavideos in videoplaylist.video_urls:
         print(listavideos)

    for descargarvideos in videoplaylist.videos:
        descargarvideos.streams.get_highest_resolution().download()

#https://www.youtube.com/watch?v=JDcvtKsSfxg

#VENTANA GENERAL
ventana = Tk()
ventana.config(bd=15)
ventana.title("Youtube Downloader")

ventana.grid_columnconfigure(2, pad=100)
ventana.grid_rowconfigure([1,3,5], pad=20)

#ENTRADA DE TEXTO
videos = Entry(ventana)
videos.grid(row=1, column=0)

#BARRA SUPERIOR
menubar = Menu(ventana)
ventana.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Info", menu = helpmenu )
menubar.add_command(label="Salir", command=ventana.destroy)

#IMAGEN
imagen = PhotoImage(file="img/youd.png")
foto = Label(ventana, image=imagen)
foto.grid(row=1, column=2)

#barra de descarga
#progressbar = Progressbar(ventana, length=200, maximum=100, mode="determinate")
#progressbar.grid(row=4, column=0)

#INFO
info = Label(ventana, text="INFORMACIÓN: ")
info.grid(row=3, column=2)

#INSTRUCCIONES

pegarlinkl = Label(ventana, text="PEGAR LINK")
pegarlinkl.grid(row=0, column=0)

instrucciones = Label(ventana, text="Para un video")
instrucciones.grid(row=3, column=0)

instrucciones2 = Label(ventana, text="Para Playlist")
instrucciones2.grid(row=5, column=0)

#BOTONES
boton = Button(ventana, text="DESCARGAR", command=descargar)
boton.grid(row=4, column=0)

botonplaylist = Button(ventana, text="DESCARGAR PLAYLIST", command=descargarplaylist)
botonplaylist.grid(row=6, column=0)

ventana.mainloop()

#revisar DearPyGUI y FLET para cambiar el GUI