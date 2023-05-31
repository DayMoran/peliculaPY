from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from Pelicula import Pelicula

#######################OPERACIONES####################
def borrar_pelicula():
    item = tree.selection()[0]
    tree.delete(item)
    messagebox.showerror("Aviso", "Un registro a sido eliminado.",icon='warning')
    
def btnG_click():
    if txt_titulo.get() == "" or txt_duracion.get() == "" or txt_director.get()=="" or txt_synopsis.get()=="" or txt_anio.get()=="" or txt_precio.get()=="":
        messagebox.showerror("Error", "Todos los campos deben ser completados")
    else:
        mipelicula = Pelicula(txt_titulo.get(), txt_duracion.get(), txt_director.get(), txt_synopsis.get(), txt_anio.get(), txt_precio.get(), "SI" if dis.get() else "NO")
    
        tree.insert("", END, values=(mipelicula.Titulo, mipelicula.Duracion, mipelicula.Director, mipelicula.Synopsis, mipelicula.Anio, mipelicula.Precio, mipelicula.Disponible))
        clear()
    
    

def btnM_click():
    
    if txt_titulo.get() == "" or txt_duracion.get() == "" or txt_director.get()=="" or txt_synopsis.get()=="" or txt_anio.get()=="" or txt_precio.get()=="":
        messagebox.showerror("Error", "Todos los campos deben ser completados")
    else:
        item=tree.selection()[0]
        
        tree.item(item, values=(txt_titulo.get(), txt_duracion.get(), txt_director.get(), txt_synopsis.get(), txt_anio.get(), txt_precio.get(), "SI" if dis.get() else "NO"))
        btnG.config(state=NORMAL)
        btnB.config(state=NORMAL)
        
        tree.config(selectmode=BROWSE)
        btnM.config(state=DISABLED)
        clear()
    pass
def onDoubleClick(event):
    item=tree.selection()[0]
    clear()
    txt_titulo.insert(0, tree.item(item)['values'][0])
    
    txt_duracion.insert(0, tree.item(item)['values'][1])
    txt_director.insert(0, tree.item(item)['values'][2])
    txt_synopsis.insert(0, tree.item(item)['values'][3])
    txt_anio.insert(0, tree.item(item)['values'][4])
    txt_precio.insert(0, tree.item(item)['values'][5])
    
    dis.set(1 if tree.item(item) ['values'][6]=="SI" else 0)
    btnG.config(state=DISABLED)
    btnB.config(state=DISABLED)
    #textid.config(state=DISABLED)
    tree.config(selectmode=NONE)
    btnM.config(state=ACTIVE)
    
    pass

def clear():
        
    txt_titulo.delete(0, END)
    txt_duracion.delete(0, END)
    txt_director.delete(0, END)
    txt_synopsis.delete(0, END)
    txt_anio.delete(0, END)
    txt_precio.delete(0, END)
    dis.set(0)
    pass
def salir():
    ventana.destroy()

######################################################

#######################DISENIO########################

ventana = Tk()
ventana.title("Pelicula APP")
#ventana.geometry("1280x720")
#ventana.resizable(False, False)  # Desactiva la capacidad de cambiar el tamanio de la ventana
color_fondo = "#292728"  # Color de fondo en formato hexadecimal
color_texto="#cff7ff"
ventana.configure(bg=color_fondo)


######################################################

################VARIABLES DE CONTROL##################
dis = IntVar()
######################################################

#####################INSERCION DE CONTROLES###########
labeltitulo=Label(text="TITULO",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labeltitulo.grid(column=0,row=0,padx=10,pady=10,sticky=E)
txt_titulo=Entry()
txt_titulo.grid(column=1,row=0,padx=10,pady=10,sticky=W)

labelduracion=Label(text="DURACION",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelduracion.grid(column=0,row=1,padx=10,pady=10,sticky=E)
txt_duracion=Entry()
txt_duracion.grid(column=1,row=1,padx=10,pady=10,sticky=W)

labeldirector=Label(text="DIRECTOR",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labeldirector.grid(column=0,row=2,padx=10,pady=10,sticky=E)
txt_director=Entry()
txt_director.grid(column=1,row=2,padx=10,pady=10,sticky=W)

labelsynopsis=Label(text="SYNOPSIS",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelsynopsis.grid(column=0,row=3,padx=10,pady=10,sticky=E)
txt_synopsis=Entry()
txt_synopsis.grid(column=1,row=3,padx=10,pady=10,sticky=W)

labelanio=Label(text="AÑO",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelanio.grid(column=0,row=4,padx=10,pady=10,sticky=E)
txt_anio=Entry()
txt_anio.grid(column=1,row=4,padx=10,pady=10,sticky=W)

labelprecio=Label(text="PRECIO",bg=color_fondo, highlightbackground=color_fondo,fg=color_texto)
labelprecio.grid(column=0,row=5,padx=10,pady=10,sticky=E)
txt_precio=Entry()
txt_precio.grid(column=1,row=5,padx=10,pady=10,sticky=W)


disp= Checkbutton(text="DISPONIBLE",variable=dis, highlightbackground=color_fondo)
disp.grid(column=1,row=9,padx=10,pady=10,sticky=W)
#PARTE DEL TREEVIEW
columns = ("titulo","duracion","director","synopsis","anio","precio","disponible")

tree=Treeview(ventana, columns=columns, show="headings")
tree.heading("titulo", text="Título")
tree.heading("duracion", text="Duración")
tree.heading("director", text="Director")
tree.heading("synopsis", text="Synopsis")
tree.heading("anio", text="Año")
tree.heading("precio", text="Precio")
tree.heading("disponible", text="Disponible")
#aqui se agregan mas columnas

tree.grid(column=0,row=10,columnspan=2,padx=80)

tree.column("titulo", width=200)
tree.column("duracion", width=80)
tree.column("director", width=200)
tree.column("synopsis", width=400)
tree.column("anio", width=80)
tree.column("precio", width=80)
tree.column("disponible", width=80)
#treeBind
tree.bind("<Double-1>",onDoubleClick)
#Botones
btnG=Button(text="Guardar",command=btnG_click)
btnG.grid(column=0,row=11, pady=30)

btnM=Button(text="Modificar",command=btnM_click)
btnM.grid(column=1,row=11, pady=30,sticky=W)

btnB=Button(text="Borrar",command=borrar_pelicula)
btnB.grid(column=1,row=11, pady=30)

btnSalir = Button(text="Salir", command=salir)
btnSalir.grid(column=1, row=11, pady=30,padx=20,sticky=E)

######################################################
btnM.config(state=DISABLED)
ventana.mainloop()