#LIBRERIAS
from tkinter import ttk
from tkinter import *
from tkinter import messagebox 
import sqlite3
import re

# Desarrollo y configuracion de interfaz grafica

app =Tk()
app.title('"VideoGames Arcadia"')
app.resizable(0, 0)
app.geometry('800x370')
app.config(bg='#8f0018')

#VARIABLES

id=StringVar()
nombre=StringVar()
genero=StringVar()
stock=IntVar()
precio=IntVar()


#conexion base de datos y creacion de tabla
def  conexbd():
    conexion=sqlite3.connect("inventariobd.db")
    cursor1=conexion.cursor()
    try:
        cursor1.execute("""CREATE TABLE inventario(
        id integer PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Genero TEXT NOT NULL,
        Stock real  NOT NULL,
        Precio real NOT NULL)""")
        
        messagebox.showinfo("CONECTADO", "INVENTARIO CREADO")
    except:
        messagebox.showinfo("CONECTADO", "Usted ya esta conectado") 

#ELIMINA BD
def borrarbd():
    conexion=sqlite3.connect("inventariobd.db")
    cursor1=conexion.cursor()
    if messagebox.askyesno(message="¿Desea eliminar el inventario definitivamente?", title= "ADVERTENCIA"):
        cursor1.execute("DROP TABLE inventario")
    else: 
        pass    

#CIERRA LA APP
def cerrar ():
    deus=messagebox.askquestion("Cerrar", "¿Desea cerrar el programa?")   
    if deus == "yes":
     app.destroy() 

#LIMPIA LOS CAMPOS CON DATOS DE LA TALBA
def limpiar():
    id.set("")
    nombre.set("")
    genero.set("")
    stock.set("")
    precio.set("")

# CRUD

def crear():
    conexion = sqlite3.connect("inventariobd.db")
    cursor1 = conexion.cursor()
    try: 
       datos = nombre.get(),genero.get(),stock.get(),precio.get() 
       cursor1.execute("INSERT INTO inventario VALUES (NULL,?,?,?,?)", (datos))
       conexion.commit()
    except:
        messagebox.showwarning("AVISO", "ERROR AL CREAR REGISTRO")
        pass
    limpiar()
    mostrar()

def mostrar ():
    conexion=sqlite3.connect("inventariobd.db")
    cursor1=conexion.cursor()
    registros = pant.get_children()
    for elemento in registros:
        pant.delete(elemento)
    try:
      cursor1.execute("SELECT * FROM inventario")
      for row in cursor1:
          #pant.insert("",0,text=row[0], values=(row[1],row[2],row[3]))
          pant.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4]))  
    except:
      pass 

def editar ():
    conexion= sqlite3.connect("inventariobd.db")
    cursor1=conexion.cursor()
    try: 
       datos= nombre.get(),genero.get(),stock.get(),precio.get() 
       cursor1.execute("UPDATE inventario SET NOMBRE=?, GENERO=?, STOCK=?, PRECIO=? WHERE ID="+id.get(), (datos))
       conexion.commit()
    except:
        messagebox.showwarning("AVISO", "NO SE PUDO EDITAR")
        pass
    limpiar()
    mostrar()
         
def eliminar ():
    conexion = sqlite3.connect("inventariobd.db")
    cursor1 = conexion.cursor()
    try: 
        if messagebox.askyesno(message="¿Desea eliminar los datos?", title="Aviso"):
           datos = id.get()
           cursor1.execute("DELETE FROM inventario WHERE id = ?", (datos,))
           conexion.commit()
    except: 
         messagebox.showwarning("AVISO", "NO SE PUDO ELIMINAR LOS DATOS")
         pass
    limpiar()
    mostrar()    


# CONTROLES EN LA INTERFAZ

barra=Menu(app)
menubd=Menu(barra,tearoff=0)
menubd.add_command(label="Crear Inventario", command=conexbd)
menubd.add_command(label="Eliminar Inventario", command=borrarbd)
menubd.add_command(label="Cerrar", command=cerrar)
barra.add_cascade(label="Inicio", menu=menubd)

ayuda=Menu(barra,tearoff=0)
ayuda.add_command(label="Resetear Campos", command=limpiar)
barra.add_cascade(label="Ayuda",menu=ayuda)

#ETIQUETAS EN LA INTERFAZ 
e1=Entry(app, textvariable=id)

l2=Label(app, text="Nombre")
l2.place(x=50,y=10)
e2=Entry(app, textvariable=nombre, width=50)
e2.place(x=100, y=10)

l3 = Label(app, text="Generos: ")
l3.place(x=50,y=40)
selec1 = ttk.Combobox( app, textvariable=genero , state="readonly", values=[
        
        "Accion",
        "Terror",
        "Baile" ,
        "Fantasia",
        "Simulador",
        "Casual",
    ],
)

selec1.place(x=100, y=40)

l4=Label(app, text="STOCK")
l4.place(x=50,y=70)
e4=Entry(app, textvariable=stock, width=10)
e4.place(x=100, y=70)

l5=Label(app, text="PRECIO")
l5.place(x=50,y=100)
e4=Entry(app, textvariable=precio, width=10)
e4.place(x=100, y=100)

#BOTONES DE EJECUCION

b1=Button(app, text="Crear Registro", command=crear)
b1.place(x=650, y=10)
b2=Button(app, text="Editar Registro", command=editar)
b2.place(x=650, y=40)
b3=Button(app, text="Ver Registro", command=mostrar)
b3.place(x=650, y=70)
b4=Button(app, text="Eliminar Registro",bg="red", command=eliminar)
b4.place(x=650, y=100)

# PANTALLA - TREEVIEW

pant=ttk.Treeview(height=10, columns=('#0','#1','#2','#3','#4'))
pant.place(x=0, y=130)
pant.column('#0',width=100)
pant.heading('#0', text="ID", anchor=CENTER)
pant.heading('#1', text="Nombre", anchor=CENTER)
pant.heading('#2', text="Genero", anchor=CENTER)
pant.column('#3', width=100)
pant.heading('#3', text="STOCK", anchor=CENTER)
pant.heading('#4', text="Precio", anchor=CENTER)

def seleccionar(event):
	item=pant.identify('item',event.x,event.y)
	id.set(pant.item(item,"text"))
	nombre.set(pant.item(item,"values")[0])
	genero.set(pant.item(item,"values")[1])
	stock.set(pant.item(item,"values")[2])
	precio.set(pant.item(item,"values")[3])
    
pant.bind("<Button-1>", seleccionar)

app.config(menu=barra)

app.mainloop()



















    

 
     
    

    
    



