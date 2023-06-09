from tkinter import *
from tkinter import filedialog




def kml_conv(path,coordinates):
    
    #Ciclo for para recorrer la lista, excepciones en lugares de la lista que estan vacios
    i = 0
    for fila in coordinates:

        if fila != "":
            indiv_coord = coordinates[i].split(",")
            if len(indiv_coord) != 1:
                path.write(indiv_coord[1] + "," + indiv_coord[0].strip() + "\n")
            i = i + 1
        else: 
            i = i + 1
    
    #Ciclo for para recorrer la lista, excepciones en lugares de la lista que estan vacios
    csv_path = open(path.name.replace("txt", "csv"), "w")
    i = 0
    for fila in coordinates:

        if fila != "":
            indiv_coord = coordinates[i].split(",")
            if len(indiv_coord) != 1:
                csv_path.write(indiv_coord[1] + "," + indiv_coord[0].strip() + "\n")
            i = i + 1
        else: 
            i = i + 1
    
#Funcion para procesar y guardar archivos
def OpenFile():
    File = filedialog.askopenfilename(title = "Abrir", filetypes=(("Archivo KML", "*.kml"),))
    kml = open(File, "r")
    kml_read = kml.read()

    #Separar por debajo de la etiqueta de coordenadas
    kml_split_up = kml_read.split("<coordinates>")

    #Separar por debajo de la etiqueta de coordenadas
    kml_split_dw = kml_split_up[1].split("</coordinates>")

    #Escoger la parte de las coordenadas
    coordinates = kml_split_dw[0]
    #Separar coordenadas por fila
    coordinates_split_enter = coordinates.split("\n")

    if File != "":
        
        path = filedialog.asksaveasfile(title= "Guardar", mode="w", defaultextension=".txt")
        
        kml_conv(path,coordinates_split_enter)

    path.close()
    

raiz = Tk()
raiz.geometry("400x300")
raiz.wm_title("Coordenadas de archivo KML")
raiz.wm_iconbitmap("./data/icon/mark.ico")
  
Button(raiz, 
    text = "Abrir archivo", 
    command = OpenFile, 
    justify= "center", 
    bg="#ba0834", 
    foreground="black", 
    activebackground="lightgreen", 
    activeforeground="white",
    relief="sunken").pack(side=BOTTOM, fill=X)

canvas = Canvas(raiz, width=256, height=256)
canvas.pack()

img = PhotoImage(file = "./data/img/map.png")

canvas.create_image(0,0, anchor  = NW, image=img)


raiz.mainloop()