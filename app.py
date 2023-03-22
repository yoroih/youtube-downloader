from tkinter import ttk
from pytube import YouTube, Playlist
from pytube.cli import on_progress
from tkinter import *
from tkinter.ttk import *

def descargar():
    link = videos.get()
    video = YouTube(link, on_progress_callback=on_progress)

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

    #TAMAÑO
    size1 = video.streams.get_highest_resolution().filesize_mb
    size = "TAMAÑO: {:.1f} Mb".format(size1)

    # Crear la barra de progreso
    progreso_barra = ttk.Progressbar(ventana, orient='horizontal', length=200, mode='determinate')
    progreso_barra.grid(row=7, column=2)

    ventana.update()

    # Descargar el archivo
    descarga = video.streams.get_highest_resolution()
    #descarga.download()
    print("**DESCARGA FINALIZADA**\n{}\n{}\n{}".format(titulo, time_format, size))
    print("***********************\n")

#https://www.youtube.com/watch?v=GXD0ySQFxRQ
#10 sec vid
def descargarplaylist():
    linkplaylist = videos.get()
    videoplaylist = Playlist(linkplaylist)

    #NOMBRE DE PLAYLIST
    nombreplaylist = videoplaylist.title
    nombreplaylist = "NOMBRE DE PLAYLIST: {}".format(nombreplaylist)
    labelnombreplaylist = Label(ventana, text=nombreplaylist)
    labelnombreplaylist.grid(row=4, column=2) 

    #UPDATE VENTANA PARA VER EL NOMBRE DE LA PLAYLIS
    ventana.update()

    #USAMOS FUNCIÓN ZIP PARA JUNTAR AMBOS BUCLES
    #EL OBJETIVO ES PODER VER EL NOMBRE DEL VIDEO ANTES DE SU DESCARGA    
    for url, video in zip(videoplaylist.video_urls, videoplaylist.videos):
        #Descargar video
        video.streams.get_highest_resolution().download()

        #nombre en tkinter
        objetovideo = YouTube(url)
        nombrevideo = objetovideo.title
        formatonombrevideo = "Video {} Descargado".format(nombrevideo)
        #nombre en consola
        print("-", formatonombrevideo)
        #ubicacion de nombre en tkinter
        nombrevideolabel = Label(ventana, text=formatonombrevideo)
        nombrevideolabel.grid(row=4, column=2)

        #duracion en tkinter
        duracionvideo = objetovideo.length
        horasvideop = duracionvideo // 3600
        minutosvideop = (duracionvideo % 3600) // 60
        segundosvideop = duracionvideo % 60
        duracionvideo_time_format = "DURACIÓN: {:.0f}h:{:.0f}m:{}s".format(horasvideop, minutosvideop, segundosvideop)
        #duracion en consola
        print("-", duracionvideo_time_format,"\n************")
        #ubicación de duracion en tkinter
        duracionvideolabel = Label(ventana, text=duracionvideo_time_format)
        duracionvideolabel.grid(row=5, column=2)

        ventana.update()

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