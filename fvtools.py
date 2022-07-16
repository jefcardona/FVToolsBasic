from ast import Delete
from cProfile import label
from cgitb import lookup, text
from faulthandler import disable
from lib2to3.pgen2.token import LBRACE
from msilib.schema import File
from multiprocessing import connection
from multiprocessing.sharedctypes import Value
from multiprocessing.spawn import import_main_path
from numbers import Real
from sqlite3.dbapi2 import Cursor, connect
#from matplotlib import pyplot as plt
import string
from struct import pack
from textwrap import wrap
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Frame, Button
from tkinter import messagebox
from tkinter import filedialog
import tkinter
from tkinter.tix import COLUMN
from tkinter.ttk import *
import sqlite3
from turtle import bgcolor, onclick, width
from typing import ItemsView
from tkinter.messagebox import *
from tkinter import scrolledtext 
from unittest import TestCase
from webbrowser import get
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from numpy import insert
import pandas as pd
from tkinter import Menu
import sys
import time 
from time import strftime
from setuptools import Command
from typing import ItemsView
import os
from datetime import datetime
import threading

class FVTools():
    
    #Se crea la ventana de login o de inicio de sesión
    #Permisos de acceso Administrador, Comercial, tecnico.

    BDPpal = "bd_FVT.db"

    def __init__(self, loginPpal):
        global usuario_in
        global contrasenia_in

        #Líneas de propiedades de la ventana login
        self.ven_login=loginPpal 
        self.ven_login.title("FVTools - inicio de sesión") #Nombre de la ventana.
        self.ven_login.geometry("350x300") #Dimensión de la ventana
        self.ven_login.resizable(width=False, height=False) #Para evitar que el usuario cambie el tamaño de la ventana.
        self.ven_login.iconbitmap("Icono.ico") #Para relacionar el ícono.

        usuario_label = Label(self.ven_login, text="Nombre de usuario: ").place(x=10, y=170)
        self.usuario_in = Entry(self.ven_login, width="30") #Entrada nombre de usuario.
        self.usuario_in.pack() #Método pack() para posicionamiento de los widgets.
        self.usuario_in.place(x=130, y=170) #Ubicación dentro de la ventana del nombre de usuario.
        self.usuario_in.focus() #Método focus() para que el puntero se ubique en el Entry nom. usuario

        contrasenia_label = Label(self.ven_login, text="Contraseña: ").place(x=10, y=200)
        self.contrasenia_in = Entry(self.ven_login, width="30", show="*") #Método show para reemplazar *
        self.contrasenia_in.pack() #Método pack() para posicionamiento de los widgets.
        self.contrasenia_in.place(x=130, y=200) #Ubicación dentro de la ventana del nombre de contraseña.

        inicioSesion_boton = Button(self.ven_login, text="Ingresar", command=self.login)
        inicioSesion_boton.pack()#Método pack() para posicionamiento de los widgets.
        inicioSesion_boton.place(x=150, y=240)#Ubicación dentro de la ventana del botón ingresar.

    #Función para interactuar con la base de datos BDPpal
    """Función para establece conexión a la base de datos. Su función principal ayuda a cargar la información de las tablas de BDPpal
    #a las tablas de la interfaz."""
    def inicio_consulta(self, consulta, parametros = ()):
        with sqlite3.connect(self.BDPpal) as conexion:
            cursor1 = conexion.cursor() # "cursor" permite recorrer filas de una tabla. Tiene tres formas búsqueda, insercción y actualización.
            resultado = cursor1.execute(consulta, parametros)
            conexion.commit()
        
        return(resultado)
    
    #Función para que solo se puedan ingresar números enteros.
    def solonumero(self, text):
        return text.isdecimal() #Para número entero isdecimal().
    
    #Función para conexión a BD y validar el usuario del Login
    def login(self):
        #db = sqlite3.connect("E:/03-Programas_ESP/01_FV_Tools_Basic/bd_FVT.db")# PORTÁTIL
        db = sqlite3.connect("bd_FVT.db")# TORRE
        conexion = db.cursor()

        usuario_data = self.usuario_in.get()    
        contrasenia_data = self.contrasenia_in.get()

        conexion.execute("SELECT * FROM gest_usuarios WHERE nom_usuario=? AND contrasenia=?", (usuario_data, contrasenia_data))

        if conexion.fetchall(): #Método fetchall: devuelve todas las filas como una lista de tuplas.
            self.usuario_in.delete(0, END) #Para borrar los datos cuando se inicie sesión.
            self.contrasenia_in.delete(0, END) #Para borrar los datos cuando se inicie sesión.
            self.ven_login.destroy()
            self.login=self.ven_menu()
        else:
            showerror(title="ERROR", message="ERROR, usuario y/o contraseña incorrectos")

    def ven_menu(self):
        self.menuPpal=Tk()
        self.menuPpal.title("Menú principal FVTools")
        self.menuPpal.geometry("300x320")
        self.menuPpal.resizable(width=False, height=False)
        self.menuPpal.iconbitmap("Icono.ico") #Para relacionar el ícono.

        #Botón para ingreso a prediseño.
        prediseño_boton = ttk.Button(self.menuPpal, text="Prediseño", command=self.ven_prediseño)
        prediseño_boton.pack()
        prediseño_boton.place(x=10, y=40, width=120, height=30)

        #Botón para ingreso a diseño
        diseño_boton = ttk.Button(self.menuPpal, text="Diseño", command=self.ven_diseñoPpal)
        diseño_boton.pack()
        diseño_boton.place(x=10, y=80, width=120, height=30)

        #Botón para ingreso a base de datos.
        baseDatos_boton = ttk.Button(self.menuPpal, text="Base de datos", command=self.ven_baseDatos)
        baseDatos_boton.pack()
        baseDatos_boton.place(x=10, y=120, width=120, height=30)

        #Botón para ingreso a gestión de usuarios.
        gesUsuario_boton = ttk.Button(self.menuPpal, text="Gestión usuarios")
        gesUsuario_boton.pack()
        gesUsuario_boton.place(x=10, y=160, width=120, height=30)

        #Botón para ingreso a indicadores.
        inidicadores_boton = ttk.Button(self.menuPpal, text="Indicadores")
        inidicadores_boton.pack()
        inidicadores_boton.place(x=10, y=200, width=120, height=30)

        #Botón para salir.
        salir_boton = ttk.Button(self.menuPpal, text="Salir", command=self.menuPpal.destroy)
        salir_boton.pack()
        salir_boton.place(x=10, y=240, width=120, height=30)

        self.menuPpal.mainloop()

    def ven_prediseño(self):
        self.prediseño = Tk()
        self.prediseño.title("Prediseño o historial de diseño")
        self.prediseño.geometry("1100x500")
        self.prediseño.resizable(width=False, height=False)
        self.prediseño.iconbitmap("Icono.ico")

        #Tabla del historial de diseño que ayudan a los prediseños.
        self.tabla_diseño = ttk.Treeview(self.prediseño, height=15, columns=("#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8","#9"))
        self.tabla_diseño.pack()
        self.tabla_diseño.place(x=10, y=10)
        self.tabla_diseño.column("#0", width=50)
        self.tabla_diseño.heading("#0", text="ID", anchor=CENTER)
        self.tabla_diseño.column("#1", width=100)
        self.tabla_diseño.heading("#1", text="Marca panel", anchor=CENTER)
        self.tabla_diseño.column("#2", width=100)
        self.tabla_diseño.heading("#2", text="Potencia panel (Wp)", anchor=CENTER)
        self.tabla_diseño.column("#3", width=100)
        self.tabla_diseño.heading("#3", text="Tensión Voc (V)", anchor=CENTER)
        self.tabla_diseño.column("#4", width=100)
        self.tabla_diseño.heading("#4", text="Corriente Isc (A)", anchor=CENTER)
        self.tabla_diseño.column("#5", width=100)
        self.tabla_diseño.heading("#5", text="Marca inversor", anchor=CENTER)
        self.tabla_diseño.column("#6", width=100)
        self.tabla_diseño.heading("#6", text="Potencia inversor (kW)", anchor=CENTER)
        self.tabla_diseño.column("#7", width=100)
        self.tabla_diseño.heading("#7", text="Potencia máx. inversor (kWp)", anchor=CENTER)
        self.tabla_diseño.column("#8", width=100)
        self.tabla_diseño.heading("#8", text="Corriente inversor (A)", anchor=CENTER)
        self.tabla_diseño.column("#9", width=100)
        self.tabla_diseño.heading("#9", text="Tensión máx. inversor (V)", anchor=CENTER)
        self.tabla_diseño.column("#10", width=100)
        self.tabla_diseño.heading("#10", text="Potencia diseñada", anchor=CENTER)

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.cargar_tab_diseño()

        self.prediseño.mainloop()
    
    def cargar_tab_diseño(self):
        grabar = self.tabla_diseño.get_children()
        for elementos in grabar:
            self.tabla_diseño.delete(elementos)

        consulta = "SELECT * FROM bd_diseño ORDER BY id DESC"
        bd_filas = self.inicio_consulta(consulta)
        for fila in bd_filas:
            self.tabla_diseño.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10]))

    """------------------------Código de prueba (eliminar al final) INICIO--------------------------"""
    def ven_diseño(self):
        self.diseño = Tk()
        self.diseño.title("Diseño de proyectos FV")
        self.diseño.geometry("400x600")
        self.diseño.resizable(width=False, height=False)
        self.diseño.iconbitmap("Icono.ico")

        #Digitar la marca de los paneles y datos técnicos asociados.
        marca_panel = Label(self.diseño, text="Marca de los paneles FV: ").place(x=10, y=20)
        self.panel_in = Entry(self.diseño, width="20")
        self.panel_in.pack()
        self.panel_in.place(x=220, y=20)

        pot_max = Label(self.diseño, text="Potencia máxima: ").place(x=10, y=50)
        self.pot_in = Entry(self.diseño, validate="key", validatecommand=(self.diseño.register(self.solonumero), "%S"), width="20")   
        self.pot_in.pack()
        self.pot_in.place(x=220, y=50)  

        voc = Label(self.diseño, text="Tensión de circuito abierto (Voc): ").place(x=10, y=80)
        self.voc_in = Entry(self.diseño, validate="key", validatecommand=(self.diseño.register(self.solonumero), "%S"), width="20")
        self.voc_in.pack()
        self.voc_in.place(x=220, y=80) 

        isc = Label(self.diseño, text="Corriente de cortocircuito (Isc): ").place(x=10, y=110)
        self.isc_in = Entry(self.diseño, validate="key", validatecommand=(self.diseño.register(self.solonumero), "%S"), width="20")
        self.isc_in.pack()
        self.isc_in.place(x=220, y=110)

        #Digitar la marca del inversor y datos técnicos asocioados.
        marca_inversor = Label(self.diseño, text="Ingresar la marca del inversor: ").place(x=10, y=150)
        self.inversor_in = Entry(self.diseño, width="20")
        self.inversor_in.pack()
        self.inversor_in.place(x=220, y=150)

        pot_inversor = Label(self.diseño, text="Potencia nominal del inversor kW: ").place(x=10, y=180)
        self.potInv_in = Entry(self.diseño, validate="key", validatecommand=(self.diseño.register(self.solonumero), "%S"), width="20")
        self.potInv_in.pack()
        self.potInv_in.place(x=220, y=180)

        potMax_inversor = Label(self.diseño, text="Potencia máxima del inversor kWp: ").place(x=10, y=210)
        self.potMax_in = Entry(self.diseño, validate="key", validatecommand=(self.diseño.register(self.solonumero), "%S"), width="20")
        self.potMax_in.pack()
        self.potMax_in.place(x=220, y=210)

        corr_inversor = Label(self.diseño, text="Corriente máxima inversor (a):").place(x=10, y=240)
        self.iMaxInv = Entry(self.diseño, validate="key", validatecommand=(self.diseño.register(self.solonumero), "%S"), width="20")
        self.iMaxInv.pack()
        self.iMaxInv.place(x=220, y=240)

        vot_inversor = Label(self.diseño, text="Tensión máxima inversor (V):").place(x=10, y=270)
        self.vMaxInv = Entry(self.diseño, validate="key", validatecommand=(self.diseño.register(self.solonumero), "%S"), width="20")
        self.vMaxInv.pack()
        self.vMaxInv.place(x=220, y=270)

        #Zona para determinar el cálculo para el generador FV
        Label(self.diseño, text="Configuración del sistema FV").place(x=100, y=310)

        cad_serie = Label(self.diseño, text="Cadenas en serie:").place(x=10, y=340)
        self.serie_in = Entry(self.diseño, validate="key", validatecommand=(self.diseño.register(self.solonumero), "%S"), width="20")
        self.serie_in.pack()
        self.serie_in.place(x=220, y=340)

        cad_paralelo = Label(self.diseño, text="Cadenas en paralelo:").place(x=10, y=370)
        self.paralelo_in = Entry(self.diseño, validate="key", validatecommand=(self.diseño.register(self.solonumero), "%S"), width="20")
        self.paralelo_in.pack()
        self.paralelo_in.place(x=220, y=370)

        #Botón calcular.
        calcular_boton = ttk.Button(self.diseño, text="Calcular", width="15", command=self.calculoGeneradorFV)
        calcular_boton.pack()
        calcular_boton.place(x=100, y=410)

        #Botón guardar
        guardar_boton = ttk.Button(self.diseño, text="Guardar", width="25", command=self.agregar_diseño)
        guardar_boton.pack()
        guardar_boton.place(x=100, y=450)

        """------------------------Código de prueba (eliminar al final) FIN--------------------------"""

    #----------------VENTANA: Diseño de proyecto principal ------------------------------------------
    def ven_diseñoPpal(self):
        self.diseñoPpal = Tk()
        self.diseñoPpal.title("Diseño de proyectos FV")
        self.diseñoPpal.geometry("520x620")
        self.diseñoPpal.resizable(width=False, height=False)
        self.diseñoPpal.iconbitmap("Icono.ico")
        
        #Menú de la ventana diseño principal
        menubarDiseñoPpal = Menu(self.diseñoPpal)
        self.diseñoPpal.config(menu=menubarDiseñoPpal)
        #Opciones Submenú de la ventana diseño principal
        #Submenú archivo
        menuArchivo = Menu(menubarDiseñoPpal, tearoff=0)
        menuArchivo.add_command(label="Nuevo", command=self.nuevo_proyecto)
        menuArchivo.add_command(label="Cargar")
        menuArchivo.add_command(label="Guardar", command=self.crear_proyecto)
        menuArchivo.add_command(label="Importar", command=self.abrir_archivo)
        menuArchivo.add_command(label="Exportar", command=self.exportar_proyecto)
        menuArchivo.add_separator()
        menuArchivo.add_command(label="Salir", command=self.diseñoPpal.destroy)
        #Submenú editar
        menuEditar = Menu(menubarDiseñoPpal, tearoff=0)
        menuEditar.add_command(label="Deshacer", accelerator="Ctrl+Z")
        menuEditar.add_command(label="Rehacer", accelerator= "Ctrl+Y")
        #Submenú ayuda
        menuAyuda = Menu(menubarDiseñoPpal, tearoff=0)
        #Subemenú de la ventana diseño principal
        menubarDiseñoPpal.add_cascade(label="Archivo", menu=menuArchivo)
        menubarDiseñoPpal.add_cascade(label="Editar", menu=menuEditar)
        menubarDiseñoPpal.add_cascade(label="Ayuda", menu=menuAyuda)

        #Datos generales
        seccion1 = Label(self.diseñoPpal, text="Datos generales del proyecto").place(x=200, y=10)

        #Nombre del proyecto
        proyecto_label = Label(self.diseñoPpal, text="Nombre del proyecto:").place(x=10, y=30)
        self.proy_in = StringVar()
        self.proy_in = Entry(self.diseñoPpal, width="60")
        self.proy_in.pack()
        self.proy_in.place(x=130, y=30)

        #Consecutivo del proyecto
        consecutivo_label = Label(self.diseñoPpal, text="Consecutivo:").place(x=10, y=60)
        self.consec_in = Entry(self.diseñoPpal, width="20")
        self.consec_in.pack()
        self.consec_in.place(x=120, y=60)


        #**********Código para la selección del departamento**********
        departamento_label = Label(self.diseñoPpal, text="Departamento:").place(x=10, y=90)
        self.departamento_in = Combobox(self.diseñoPpal, width="30", justify=CENTER) #@departamento_in: texto en la tabla bd_departamento
        consulta = "SELECT * FROM bd_departamentos ORDER BY id DESC" #consulta a la base de datos BDPpal para importar la información de la tabla bd_departamentos
        db_filas = self.inicio_consulta(consulta)
        listaDepart =[]
        codDep = []
        for fila in db_filas:
            listaDepart = [fila[1]]+listaDepart
            codDep = [fila[2]] + codDep 
        self.departamento_in["values"] = listaDepart
        self.departamento_in.pack
        self.departamento_in.place(x=120, y=90)
        
        #*********Código para la selección del municipio

        municipio_label = Label(self.diseñoPpal,text="Municipio:").place(x=10, y=120)
        self.municipio_in = Combobox(self.diseñoPpal, width="30", justify=CENTER) #@municipio_in: texto en la tabla bd_municipios
        consulta2 ="SELECT * FROM bd_municipios ORDER BY id_municipio DESC" #consulta a la base de datos BDPpal para importar la información de la tabla bd_municipios
        db_filas2 = self.inicio_consulta(consulta2)
        lisMunic = []
        for fila2 in db_filas2:
            lisMunic = [fila2[1]]+lisMunic
        self.municipio_in["values"] = lisMunic
        self.municipio_in.pack
        self.municipio_in.place(x=120, y=120)
        
        #Latitud
        latitud_label = Label(self.diseñoPpal, text="Latitud").place(x=10, y=150)
        self.latitud_in = DoubleVar()
        self.latitud_in = Entry(self.diseñoPpal, width="30")
        self.latitud_in.pack()
        self.latitud_in.place(x=120, y=150)

        #Longitud
        longitud_label = Label(self.diseñoPpal, text="Longitud").place(x=10, y=180)
        self.longitud_in = Entry(self.diseñoPpal, width="30")
        self.longitud_in.pack()
        self.longitud_in.place(x=120, y=180)

        #Nombre del comercial o usuario asignado para presentar el proyecto al cliente
        comercial_label = Label(self.diseñoPpal, text="Nombre del comercial:").place(x=10, y=210)
        self.comercial_in = Combobox(self.diseñoPpal, width="30", justify=CENTER) #@comercial_in: texto en la tabla gest_usuarios.
        consulta3 = "SELECT * FROM gest_usuarios ORDER BY id DESC" #consulta a la base de datos BDPpal para importar la información de la tabla gest_usuarios
        db_filas3 = self.inicio_consulta(consulta3)
        lisUsuarios = []
        for fila3 in db_filas3:
            lisUsuarios = [fila3[1]+" "+fila3[2]]+lisUsuarios
        self.comercial_in["values"] = lisUsuarios
        self.comercial_in.pack
        self.comercial_in.place(x=160, y=210)

        #Dirección del proyecto
        direccion_label = Label(self.diseñoPpal, text="Dirección según la factura:").place(x=10, y=240)
        self.dir_in = Entry(self.diseñoPpal, width="50")
        self.dir_in.pack
        self.dir_in.place(x=160, y=240)

        #Nombre del cliente
        nombreCliente_label = Label(self.diseñoPpal, text="Nombre del cliente:").place(x=10, y=270)
        self.nomCliente_in = Entry(self.diseñoPpal, width="40")
        self.nomCliente_in.pack
        self.nomCliente_in.place(x=120, y=270)

        #Contacto
        contactoCliente_label = Label(self.diseñoPpal, text="Contacto:").place(x=10, y=300)
        self.contacto_in = Entry(self.diseñoPpal, width="20")
        self.contacto_in.pack
        self.contacto_in.place(x=120, y=300)

        #Operador de energía
        operadorRed_label = Label(self.diseñoPpal, text="Operador de red:").place(x=10, y=330)
        self.operador_in = Entry(self.diseñoPpal, width="30")
        self.operador_in.pack
        self.operador_in.place(x=120, y=330)

        #Comercializador
        comercializador_label = Label(self.diseñoPpal, text="Comercializador").place(x=10, y=360)
        self.comercializador_in = Entry(self.diseñoPpal, width="30")
        self.comercializador_in.pack
        self.comercializador_in.place(x=120, y=360)

        #Sistema requerido
        sistemaFV_label = Label(self.diseñoPpal, text="Sistema a diseñar").place(x=10, y=390)
        self.sistemaFV_in = Combobox(self.diseñoPpal, width="15") #@sistemaFV_in: texto de la tabla bd_proyectos
        self.sistemaFV_in["values"] = ["ON GRID", "OFF GRID", "Hibrido"]
        self.sistemaFV_in.set("ON GRID") #Valor por defecto "ON GRID"
        self.sistemaFV_in.place(x=120, y=390)

        #**********Código para botones

        #Botón crear proyecto
        crearProyect_boton = ttk.Button(self.diseñoPpal, text="Crear proyecto", width="30", command=self.crear_proyecto)
        crearProyect_boton.pack
        crearProyect_boton.place(x=200, y=430)

        #Botones selección de tipo de diseño (ON-GRID; OFF-GRID; Hibrido) 
        menuDiseño_label = Label(self.diseñoPpal, text="Opciones de diseño").place(x=200, y=460)
        #Botón diseño ON GRID
        sisOngrid_boton = ttk.Button(self.diseñoPpal, text="ON GRID", width="20", command=self.ven_disONGRID) #command=self.val_OnGrid
        sisOngrid_boton.pack()
        sisOngrid_boton.place(x=10, y=490)

        #Botón diseño OFF GRID
        sisOffgrid_boton = ttk.Button(self.diseñoPpal, text="OFF GRID", width="20", command=self.val_OffGrid)
        sisOffgrid_boton.pack()
        sisOffgrid_boton.place(x=190, y=490)

        #Botón diseño Hibrido
        sisHibrido_boton = ttk.Button(self.diseñoPpal, text="Hibrido", width="20", command=self.val_Hibrido)
        sisHibrido_boton.pack()
        sisHibrido_boton.place(x=370, y=490)

        self.diseñoPpal.mainloop() #Fin de la ventana diseño principal
    
    def nuevo_proyecto(self): #Este código deja en blanco todos los campos de la ventana ven_diseñoPpal
        self.proy_in.delete(0, END) #1
        self.consec_in.delete(0, END) #2
        self.departamento_in.delete(0, END) #3
        self.municipio_in.delete(0, END) #4
        self.latitud_in.delete(0, END) #5
        self.longitud_in.delete(0, END) #6
        self.comercial_in.delete(0, END) #7
        self.dir_in.delete(0, END) #8
        self.nomCliente_in.delete(0, END) #9
        self.contacto_in.delete(0, END) #10
        self.operador_in.delete(0, END) #11
        self.comercializador_in.delete(0, END) #12
    
    def abrir_archivo(self): #Este código permite abrir archivo exportado en el interfaz ven_diseñoPpal
        abrirArchivo =filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo", defaultextension=".txt", filetypes=[("Todos los archivos","*.*")])
        importProyecto = open(abrirArchivo, "r")
        contenidoProy = importProyecto.read()
        importProyecto.close()
        print(contenidoProy)
        self.proy_in.insert(0, contenidoProy[0])
        self.consec_in.insert(0, contenidoProy[1])
        
        #importProyecto.read(1,self.proy_in.insert())
    
    def exportar_proyecto(self): #Este código permite exportar el archivo del proyecto en la ruta elegida
        if self.validar_campos_diseno():
            nomProyecto =(self.consec_in.get()+"-"+self.proy_in.get()) #Nombre del archivo por defecto
            expoArchivo = filedialog.asksaveasfilename(title="Importar proyecto", initialfile=(nomProyecto), defaultextension=".txt", 
            filetypes=[("txt","*.txt")])
            fechaProy = datetime.now()
            expoProyecto = open(expoArchivo, 'w')
            print(expoProyecto)
            expoProyecto.write(self.proy_in.get())
            expoProyecto.write("\t")
            expoProyecto.write(self.consec_in.get())
            expoProyecto.write("\t")
            expoProyecto.write("\n" + self.departamento_in.get())
            expoProyecto.write("\n" + self.municipio_in.get())
            expoProyecto.write("\n" + self.latitud_in.get())
            expoProyecto.write("\n" + self.longitud_in.get())
            expoProyecto.write("\n" + self.comercial_in.get())
            expoProyecto.write("\n" + self.dir_in.get())
            expoProyecto.write("\n" + self.nomCliente_in.get())
            expoProyecto.write("\n" + self.contacto_in.get())
            expoProyecto.write("\n" + self.operador_in.get())
            expoProyecto.write("\n" + self.comercializador_in.get())
            expoProyecto.write("\n" + self.sistemaFV_in.get())
            showinfo(title="Exportación de proyecto", message="Se ha exportado el proyecto correctamente.")
        else:
            showerror(title="ERROR", message="Debes llenar todos lo campo")
            
        
    def crear_proyecto(self): #Este código permite guardar el proyecto en la base de datos interna del programa
        if self.validar_campos_diseno():
            consulta1 = "INSERT INTO bd_proyectos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" 
            parametros = (self.proy_in.get(), self.consec_in.get(), self.departamento_in.get(), self.municipio_in.get(), self.latitud_in.get(),
            self.longitud_in.get(), self.comercial_in.get(), self.dir_in.get(), self.nomCliente_in.get(), self.contacto_in.get(), self.operador_in.get(),
            self.comercializador_in.get(), self.sistemaFV_in.get(), datetime.now())
            self.inicio_consulta(consulta1, parametros)
            showinfo(title="Ingreso de datos del proyecto FVTools", message="Se ha guardado y creado el proyecto correctamente.")
            self.proy_in.delete(0, END) #1
            self.consec_in.delete(0, END) #2
            self.departamento_in.delete(0, END) #3
            self.municipio_in.delete(0, END) #4
            self.latitud_in.delete(0, END) #5
            self.longitud_in.delete(0, END) #6
            self.comercial_in.delete(0, END) #7
            self.dir_in.delete(0, END) #8
            self.nomCliente_in.delete(0, END) #9
            self.contacto_in.delete(0, END) #10
            self.operador_in.delete(0, END) #11
            self.comercializador_in.delete(0, END) #12
            self.sistemaFV_in.delete(0, END) #13
        else:
            showerror(title="ERROR", message="Debes de llenar todos los campos")
        #selDep = self.departamento_in.get()
        #messagebox.showinfo("El departamento es","El departamento es:" + selDep)

    def validar_campos_diseno(self): #Se valida que todos los cmapos de la ventana ven_diseñoPpal se encuentre diligenciado, es decir, sin campos vacíos
        return len(self.proy_in.get()) != 0 and len(self.consec_in.get()) != 0 and len(self.departamento_in.get()) != 0 and len(self.municipio_in.get()) != 0 and len(
            self.latitud_in.get()) != 0 and len(self.longitud_in.get())!= 0 and len(self.comercial_in.get()) !=0 and len(self.dir_in.get()) !=0 and len(
                self.nomCliente_in.get()) !=0 and len(self.contacto_in.get()) !=0 and len(self.operador_in.get()) !=0 and len(self.comercializador_in.get()) !=0 and len(
                    self.sistemaFV_in.get()) !=0

    def calculoGeneradorFV(self):
        if self.validar_campos_diseno():
            self.calc_potenciaPico = float(self.pot_in.get())*float(self.serie_in.get())*float(self.paralelo_in.get())/1000
            print(self.calc_potenciaPico)
            self.calc_tensionMax = float(self.serie_in.get())*float(self.voc_in.get())
            print("La tensión es:", self.calc_tensionMax)
            if self.calc_potenciaPico > float(self.potMax_in.get()):
                showerror(title="ERROR", message="La potencia pico de los paneles supera la capacidad admisible por el inversor.")
            if self.calc_tensionMax > float(self.vMaxInv.get()):
                showerror(title="ERROR", message="La tensión de la configuración del arreglo en serie de los paneles supera la tensión máxima admisible del inversor.")
            else:
                showinfo(title="Resultado", message="El diseño es ideal.")
        else:
            showerror(title="ERROR", message="Debes llenar todos lo campo")
    
    def agregar_diseño(self):
        if self.validar_campos_diseno():
            consulta0 = "INSERT INTO bd_diseño VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            parametros = (self.panel_in.get(), self.pot_in.get(), self.voc_in.get(), self.isc_in.get(), self.inversor_in.get(), self.potInv_in.get(), self.potMax_in.get(), self.iMaxInv.get(), self.vMaxInv.get(), self.calc_potenciaPico)
            self.inicio_consulta(consulta0, parametros)
            showinfo(title="Ingreso de diseño FVTools", message="Se ha guardado el diseño en la base de datos correctamente.")
            self.panel_in.delete(0,END)
            self.pot_in.delete(0,END)
            self.voc_in.delete(0,END)
            self.isc_in.delete(0,END)
            self.inversor_in.delete(0,END)
            self.potInv_in.delete(0,END)
            self.potMax_in.delete(0,END)
            self.iMaxInv.delete(0,END)
            self.vMaxInv.delete(0,END)
        else:
            showerror(title="ERROR", message="Debes de llenar todos los campos.") 

    def val_OnGrid(self): #Función solo para ingreso a diseños de proyectos ON GRID.
        if self.validar_campos_diseno(): #Se valida que todos los cmapos estén diligenciados
            if self.sistemaFV_in.get() == "ON GRID": #Se valida que corresponda el proyecto con el sistema a diseñar
                sistemaON = messagebox.askyesno(title="Tipo de sistema a diseñar", message="El sistema a diseñar es un sistema ON GRID, deseas continuar?")
                if sistemaON == True:
                    self.ven_disONGRID()
            else:
                showerror(title="Error de selección de sistema", message="El tipo de diseño seleccionado no corresponde al sistema FV del proyecto.")
        else:
            showerror(title="Error, de diligenciamiento", message="Debe de llenar todos los campos")    

    def val_OffGrid(self): #Función solo para ingreso a diseños de proyectos ON GRID.
        if self.validar_campos_diseno(): #Se valida que todos los cmapos estén diligenciados
            if self.sistemaFV_in.get() == "OFF GRID":#Se valida que corresponda el proyecto con el sistema a diseñar
                sistemaOFF = messagebox.askyesno(title="Tipo de sistema a diseñar", message="El sistema a diseñar es un sistema OFF GRID, deseas continuar?")
                if sistemaOFF == True:
                    self.ven_disOFFGRID()
            else:
                showerror(title="Error de selección de sistema", message="El tipo de diseño seleccionado no corresponde al sistema FV del proyecto.")
        else:
            showerror(title="Error, de diligenciamiento", message="Debe de llenar todos los campos") 
    
    def val_Hibrido(self): #Función solo para ingreso a diseños de proyectos ON GRID.
        if self.validar_campos_diseno(): #Se valida que todos los cmapos estén diligenciados
            if self.sistemaFV_in.get() == "Hibrido":#Se valida que corresponda el proyecto con el sistema a diseñar
                sistemaHi = messagebox.askyesno(title="Tipo de sistema a diseñar", message="El sistema a diseñar es un sistema Hibrido, deseas continuar?")
                if sistemaHi == True:
                    self.ven_disHibrido()
            else:
                showerror(title="Error de selección de sistema", message="El tipo de diseño seleccionado no corresponde al sistema FV del proyecto.")
        else:
            showerror(title="Error, de diligenciamiento", message="Debe de llenar todos los campos") 

    #------------------------------------------ Ventana: Diseño ON GRID ----------------------------------
    def ven_disONGRID(self):
        self.disOngrid = Tk()
        self.disOngrid.title("Diseño de proyecto con sistema ON-GRID FVTools")
        self.disOngrid.geometry("1250x800")
        self.disOngrid.resizable(width=False, height=False)
        self.disOngrid.iconbitmap("Icono.ico") #Para relacionar el ícono.

        #Encabezado
        encaOG_label = Label(self.disOngrid, text="Interfaz para diseño de sistema FV On Grid del proyecto: "+self.consec_in.get()+" "+self.proy_in.get()).place(x=400, y=10)

        #1---->Consumos de energía
        consumo_label = Label(self.disOngrid, text="1. Consumo mensual del cliente mensual").place(x=10, y=30)
        eactiva_label = Label(self.disOngrid, text="kWh/mes", foreground="blue").place(x=110,y=60)
        ereactiva_label = Label(self.disOngrid, text="kVARh/mes", foreground="red").place(x=250, y=60)
        #Enero
        ene_label = Label(self.disOngrid, text="Enero").place(x=10, y=90)
        self.ene_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.ene_in.insert(0, 0)
        self.ene_in.pack()
        self.ene_in.place(x=80, y=90)

        self.ener_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.ener_in.insert(0, 0)
        self.ener_in.pack()
        self.ener_in.place(x=220, y=90)

        #Febrero
        feb_label = Label(self.disOngrid, text="Frebrero").place(x=10, y=120)    
        self.feb_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.feb_in.insert(0, 0)
        self.feb_in.pack()
        self.feb_in.place(x=80, y=120)

        self.febr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.febr_in.insert(0, 0)
        self.febr_in.pack()
        self.febr_in.place(x=220, y=120)

        #Marzo
        mar_label = Label(self.disOngrid, text="Marzo").place(x=10, y=150)
        self.mar_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.mar_in.insert(0, 0)
        self.mar_in.pack()
        self.mar_in.place(x=80, y=150)

        self.marr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.marr_in.insert(0, 0)
        self.marr_in.pack()
        self.marr_in.place(x=220, y=150)

        #Abril
        abr_label = Label(self.disOngrid, text="Abril").place(x=10, y=180)
        self.abr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.abr_in.insert(0, 0)
        self.abr_in.pack()
        self.abr_in.place(x=80, y=180)

        self.abrr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.abrr_in.insert(0, 0)
        self.abrr_in.pack()
        self.abrr_in.place(x=220, y=180)

        #Mayo
        may_label = Label(self.disOngrid, text="Mayo").place(x=10, y=210)
        self.may_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.may_in.insert(0, 0)
        self.may_in.pack()
        self.may_in.place(x=80, y=210)

        self.mayr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.mayr_in.insert(0, 0)
        self.mayr_in.pack()
        self.mayr_in.place(x=220, y=210)

        #Junio
        jun_label = Label(self.disOngrid, text="Junio").place(x=10, y=240)
        self.jun_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.jun_in.insert(0, 0)
        self.jun_in.pack()
        self.jun_in.place(x=80, y=240)

        self.junr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.junr_in.insert(0, 0)
        self.junr_in.pack()
        self.junr_in.place(x=220, y=240)

        #Julio
        jul_label = Label(self.disOngrid, text="Julio").place(x=10, y=270)
        self.jul_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.jul_in.insert(0, 0)
        self.jul_in.pack()
        self.jul_in.place(x=80, y=270)

        self.julr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.julr_in.insert(0, 0)
        self.julr_in.pack()
        self.julr_in.place(x=220, y=270)

        #Agosto
        ago_label = Label(self.disOngrid, text="Agosto").place(x=10, y=300)
        self.ago_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.ago_in.insert(0, 0)
        self.ago_in.pack()
        self.ago_in.place(x=80, y=300)

        self.agor_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.agor_in.insert(0, 0)
        self.agor_in.pack()
        self.agor_in.place(x=220, y=300)

        #Septiembre
        sep_label = Label(self.disOngrid, text="Septiembre").place(x=10, y=330)
        self.sep_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.sep_in.insert(0, 0)
        self.sep_in.pack()
        self.sep_in.place(x=80, y=330)

        self.sepr_in =Entry(self.disOngrid, width="20", justify=CENTER)
        self.sepr_in.insert(0, 0)
        self.sepr_in.pack()
        self.sepr_in.place(x=220, y=330)
        #Octubre
        oct_label = Label(self.disOngrid, text="Octubre").place(x=10, y=360)
        self.oct_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.oct_in.insert(0, 0)
        self.oct_in.pack()
        self.oct_in.place(x=80, y=360)

        self.octr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.octr_in.insert(0, 0)
        self.octr_in.pack()
        self.octr_in.place(x=220, y=360)

        #Noviembre
        nov_label = Label(self.disOngrid, text="Noviembre").place(x=10, y=390)
        self.nov_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.nov_in.insert(0, 0)
        self.nov_in.pack()
        self.nov_in.place(x=80, y=390)

        self.novr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.novr_in.insert(0, 0)
        self.novr_in.pack()
        self.novr_in.place(x=220, y=390)

        #Diciembre
        dic_label = Label(self.disOngrid, text="Diciembre").place(x=10, y=420)
        self.dic_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.dic_in.insert(0, 0)
        self.dic_in.pack()
        self.dic_in.place(x=80, y=420)

        self.dicr_in = Entry(self.disOngrid, width="20", justify=CENTER)
        self.dicr_in.insert(0, 0)
        self.dicr_in.pack()
        self.dicr_in.place(x=220, y=420)

        #Botón para el cálculo de promedio de energía Activa y Reactiva
        calPromedio_boton = Button(self.disOngrid, text="Calcular promedio", width="20", command=self.promConsumo)
        calPromedio_boton.pack()
        calPromedio_boton.place(x=150, y=450)


        #1.1---> Describir el consumo del cliente.
        desConsumo_label = Label(self.disOngrid, text="1.1. Describa el comportamiento del consumo del cliente:").place(x=10, y=540)
        descConsumo_scrol = scrolledtext.ScrolledText(self.disOngrid, width="40")
        descConsumo_scrol.pack()
        descConsumo_scrol.place(x=10, y=570, height=200)

        #2---> Condiciones eléctricas
        condiElect_label = Label(self.disOngrid, text="2. Condiciones eléctricas").place(x=400, y=30)

        #Sistema eléctrico
        sisElectrico_label = Label(self.disOngrid, text="Sistema:").place(x=400, y=60)
        self.sisElecPoy_in = Combobox(self.disOngrid, width="20")
        self.sisElecPoy_in["values"] = ["Monofásico (2F+1N)", "Trifásico (3F+1N)"]
        self.sisElecPoy_in.set("Trifásico (3F+1N)")
        self.sisElecPoy_in.place(x=500, y=60)

        #Tension nominal del cliente
        tenNomC = Label(self.disOngrid, text="Tensión nom. [V]:").place(x=400, y=90)
        self.tenNomC_in = Combobox(self.disOngrid, width="20")
        self.tenNomC_in["values"] = [208, 220, 440]
        self.tenNomC_in.set(220)
        self.tenNomC_in.place(x=500, y=90)

        #Tipo de  carga del cliente 
        """Se debe ajustar con una base de datos que permita ajustar el combobox"""
        tipoCarga_label = Label(self.disOngrid, text="Tipo de carga:").place(x=400,y=120)
        self.tipoCarga_in = Combobox(self.disOngrid, width="20")
        self.tipoCarga_in["values"] = ["Supermercado", "EDS", "Ofinica", "Ganaderia", "Centro educativo", "Panadería", "Restaurante", "Hotel"]
        self.tipoCarga_in.set("Supermercado")
        self.tipoCarga_in.place(x=500, y=120)

        #Seleccionar marca de paneles FV, se toma el dato de bd_panel
        marcaPanel_label = Label(self.disOngrid, text="Marca de paneles").place(x=400, y=150)
        self.marcapanel_sel = Combobox(self.disOngrid, width="30", justify=CENTER) #@marcaPanel_sel: text de la tabla bd_ongrid
        self.marcaPanelSelect()
        self.marcapanel_sel.pack()
        self.marcapanel_sel.place(x=500, y=150)

        #Seleccionar la referencia del panel FV seleccionado de self.marcaPanel_sel , de la tabla bd_panel
        refPanel_label = Label(self.disOngrid, text="Referencia:").place(x=400, y=180)
        self.refPanel_sel = Combobox(self.disOngrid, width="30", justify=CENTER)
        self.refPanel_sel.pack()
        self.refPanel_sel.place(x=500, y=180)

        #Botón inversores
        self.inversores_boton = Button(self.disOngrid, text="Inversores", width="20", command=self.ven_disinversores)
        self.inversores_boton.pack()
        self.inversores_boton.place(x=500, y=400)

        self.disOngrid.mainloop()
    
    def marcaPanelSelect(self):
        consulta1 = "SELECT * FROM bd_panel ORDER BY id DESC" #Consulta a la base de datos BDPpal para importar la información de la tabla bd_panel
        db_filas = self.inicio_consulta(consulta1)
        listaPanel = []
        listaPanel2 = []
        contador = 0
        contador2 = 0
        for fila in db_filas:
            listaPanel = listaPanel + [fila[2]]
            contador = contador+1
        for n in range(contador):
            if listaPanel[n] != listaPanel[contador2]:
                listaPanel2 = listaPanel2+[listaPanel[n]]
                contador2 = contador2+1

        self.marcapanel_sel["values"] = listaPanel2
        self.marcapanel_sel.bind("<<ComboboxSelected>>", self.refPanelSelect)
        return()
    
    def refPanelSelect(self, event):
        #consulta1 = "SELECT * FROM bd_panel ORDER BY id DESC" #Consulta a la base de datos BDPpal para importar la información de la tabla bd_panel
        #db_filas = self.inicio_consulta(consulta1)
        #listarefPanel = []
        panelSel = self.marcapanel_sel.get()
        print(panelSel)
        return()
    
    def ven_disinversores(self):
        self.inversoresdim = Tk()
        self.inversoresdim.geometry("700x500")
        self.inversoresdim.title("Dimensionamiento inversores FVTools")
        self.inversoresdim.resizable(width=False, height=False)
        self.inversoresdim.iconbitmap("Icono.ico") #Para relacionar 
        #Se incluye panel para pestañas
        self.inversoresdim_nb = Notebook(self.inversoresdim)
        self.inversoresdim_nb.pack(fill="both", expand=True)
        #Creación de las pestañas (inversor 1 hasta inversor 10)
        inversor1 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor1, text="Inversor 1")
        inversor2 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor2, text="Inversor 2")
        inversor3 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor3, text="Inversor 3")
        inversor4 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor4, text="Inversor 4")
        inversor5 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor5, text="Inversor 5")
        inversor6 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor6, text="Inversor 6")
        inversor7 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor7, text="Inversor 7")
        inversor8 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor8, text="Inversor 8")
        inversor9 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor9, text="Inversor 9")
        inversor10 = ttk.Frame(self.inversoresdim_nb)
        self.inversoresdim_nb.add(inversor10, text="Inversor 10")

    

    def promConsumo(self):
        activa =[self.ene_in.get(),self.feb_in.get(),self.mar_in.get(),self.abr_in.get(),self.may_in.get(),self.jun_in.get(),self.jul_in.get(),self.ago_in.get(),
        self.sep_in.get(),self.oct_in.get(),self.nov_in.get(),self.dic_in.get()]
        meses = 12
        sumActiva = 0
        mesActiva = 0
        for n in range (meses):
            numActiva = float(activa[n])
            sumActiva = sumActiva+numActiva
            if numActiva > 0:
                mesActiva = mesActiva + 1
        if mesActiva == 0:
            mesActiva=1
        self.promActiva = sumActiva/mesActiva
        self.promActiva_texto = Label(self.disOngrid, text="El promedio de energía activa mensual es de {} kWh/mes".format(self.promActiva), foreground="blue").place(x=10, y=480)

        
        reactiva =[self.ener_in.get(),self.febr_in.get(),self.marr_in.get(),self.abrr_in.get(),self.mayr_in.get(),self.junr_in.get(),self.julr_in.get(),self.agor_in.get(),
        self.sepr_in.get(),self.octr_in.get(),self.novr_in.get(),self.dicr_in.get()]
        sumReactiva = 0
        mesReactiva = 0
        for n in range(meses):
            numReactiva = float(reactiva[n])
            sumReactiva = sumReactiva + numReactiva
            if numReactiva > 0:
                mesReactiva = mesReactiva + 1
        if mesReactiva == 0:
            mesReactiva=1
        self.promReactiva = sumReactiva/mesReactiva
        self.promReactiva = sumReactiva/mesReactiva
        self.promReactiva_texto = Label(self.disOngrid, text="El promedio de energía reactiva mensual es de {} kVARh/mes".format(self.promReactiva), foreground="red").place(x=10, y=500)

    #------------------------------------------ Ventana: Diseño OFF GRID ----------------------------------
    def ven_disOFFGRID(self):
        self.disOffgrid = Tk()
        self.disOffgrid.title("Diseño de proyecto con sistema OFF-GRID FVTools")
        self.disOffgrid.geometry("1250x650")
        self.disOffgrid.resizable(width=False, height=False)
        self.disOffgrid.iconbitmap("Icono.ico") #Para relacionar icono

        self.disOffgrid.mainloop()

    #------------------------------------------ Ventana: Diseño Hibrido ----------------------------------
    def ven_disHibrido(self):
        self.disHibrido = Tk()
        self.disHibrido.title("Diseño de proyecto con sistema Híbrido FVTools")
        self.disHibrido.geometry("1250x650")
        self.disHibrido.resizable(width=False, height=False)
        self.disHibrido.iconbitmap("Icono.ico") #Para relacionar el ícono.

        self.disHibrido.mainloop()
    
    #-----------------------------------Ventana Base de datos-----------------------------------------
    def ven_baseDatos(self):
        self.baseDatos = Tk()
        self.baseDatos.title("Base de datos FVTools")
        self.baseDatos.geometry("300x300")
        self.baseDatos.resizable(width=False, height=False)
        self.baseDatos.iconbitmap("Icono.ico") #Para relacionar el ícono.

        #Boton modulos FV
        panel_boton = ttk.Button(self.baseDatos, text="Panel FV", width="15", command=self.ven_panelesFV)
        panel_boton.pack()
        panel_boton.place(x=10, y=40)

        #Boton inversores
        inversor_boton = ttk.Button(self.baseDatos, text="Inversores", width="15", command=self.ven_inversores)
        inversor_boton.pack()
        inversor_boton.place(x=10, y=80)

        #Boton materiales
        material_boton = ttk.Button(self.baseDatos, text="Materiales", width="15", command=self.ven_materiales)
        material_boton.pack()
        material_boton.place(x=10, y=120)

        #Botón mano de obra
        mo_boton = ttk.Button(self.baseDatos, text="Mano de obra", width="15")
        mo_boton.pack()
        mo_boton.place(x=10, y=160)

        #Botón observaciones
        obs_boton = ttk.Button(self.baseDatos, text="Observaciones", width="15")
        obs_boton.pack()
        obs_boton.place(x=10, y=200)

        self.baseDatos.mainloop()

    #---------------------- Ventana: BD de los paneles FV ----------------------------------------------------
    def ven_panelesFV(self):
        self.panelFV = Tk()
        self.panelFV.title("BD paneles Fotovoltaicos FVTools")
        self.panelFV.geometry("1250x650")
        self.panelFV.resizable(width=False, height=False)
        self.panelFV.iconbitmap("Icono.ico") #Para relaiconar el ìcono.

        #Código de entrada del Panel FV.
        codPanel_label = Label(self.panelFV, text="Código del producto: ").place(x=10, y=30)
        self.codPanel_in = Entry(self.panelFV, width="20") #@codPanel_in: es un texto en la tabla bd_panel.
        self.codPanel_in.pack()
        self.codPanel_in.focus()
        self.codPanel_in.place(x=140, y=30)

        #Descripción de entrada del panel
        descPanel = Label(self.panelFV, text="Descripción:").place(x=10, y=60)
        self.descPanel_in = Entry(self.panelFV, width="70") #@descPanel_in: es un texto en la tabla bd_panel.
        self.descPanel_in.pack()
        self.descPanel_in.place(x=140, y=60)

        #Unidad de entrada del panel
        unidadPanel_label = Label(self.panelFV, text="Unidad: ").place(x=10, y=90)
        self.unidadPanel_in = Combobox(self.panelFV, width="10") #@unidadPanel_in: es un texto en la tabla bd_panel.
        self.unidadPanel_in["values"] = ["Und.", "m", "ml", "kg", "Global", "Galón"]
        self.unidadPanel_in.set("Und.") #El valor de "Und." predeterminado
        self.unidadPanel_in.place(x=140, y=90)

        #Precio unitario de entrada del panel
        precioUnitPanel_label = Label(self.panelFV, text="Precio unitario: ").place(x=10, y=120) #@precioUnitPanel_in: valor numérico entero tabla bd_panel
        self.precioUnitPanel_in = Entry(self.panelFV, validate = "key", validatecommand=(self.panelFV.register(self.solonumero), "%S"), width="20")
        #@precioUnitPanel_in: es un entero en la tabla bd_panel.
        self.precioUnitPanel_in.pack()
        self.precioUnitPanel_in.place(x=140, y=120)

        #Observaciones de entrada del panel
        obsPanel_label = Label(self.panelFV, text="Observaciones: ").place(x=10, y=150)
        self.obs_panel_in = Entry(self.panelFV, width="60") #@obs_panel: es un texto en la tabla bd_panel.
        self.obs_panel_in.pack
        self.obs_panel_in.place(x=140, y=150)

        #Marca de entrada del panel
        marcaPanel_label = Label(self.panelFV, text="Marca:").place(x=570, y= 30)
        self.marcaPanel_in = Entry(self.panelFV, width="20") #@marcaPanel: Texto de la tabla bd_panel
        self.marcaPanel_in.pack()
        self.marcaPanel_in.place(x=750, y=30)

        #Referencia de entrada del panel
        refPanel_label = Label(self.panelFV, text="Referencia:").place(x=900, y=30)
        self.rePanel_in = Entry(self.panelFV, width="20") #@rePanel: Texto de la tabla bd_panel
        self.rePanel_in.pack()
        self.rePanel_in.place(x=1100, y=30)

        #Potencia máx. de entrada del panel
        potMaxPanel_label = Label(self.panelFV, text="Potencia máxima [Wp]:").place(x=570, y=60) #@potMaxPanel: Valor numérico de la tabla bd_panel
        self.potMaxPanel_in = Entry(self.panelFV, validate="key", validatecommand=(self.panelFV.register(self.solonumero), "%S"), width="20")
        self.potMaxPanel_in.pack()
        self.potMaxPanel_in.place(x=750, y=60)

        #Tensión máx. de entrada del panel
        tensioMaxPanel_label = Label(self.panelFV, text="Tensión máx. potencia [Vmp]:").place(x=900, y=60)
        self.tensionMaxPanel_in = Entry(self.panelFV, width="20")
        self.tensionMaxPanel_in.pack()
        self.tensionMaxPanel_in.place(x=1100, y=60)

        #Corriente máx. de entrada del panel
        corMaxPanel_label = Label(self.panelFV, text="Corriente máx. potencia [Imp]:").place(x=570, y=90)
        self.corMaxPanel_in = Entry(self.panelFV, width="20")
        self.corMaxPanel_in.pack()
        self.corMaxPanel_in.place(x=750, y=90)

        #Tensión de Cto. abierto de entrada del panel
        tenAbiertoPanel_label = Label(self.panelFV, text="Tensión circuito abierto [Voc]:").place(x=900, y=90)
        self.tenAbiertoPanel_in = Entry(self.panelFV, width="20")
        self.tenAbiertoPanel_in.pack()
        self.tenAbiertoPanel_in.place(x=1100, y=90)

        #Corriente corto entrada del panel
        corCortoPanel_label = Label(self.panelFV, text="Corriente corto circuito [Isc]:").place(x=570, y=120)
        self.corCortoPanel_in = Entry(self.panelFV, width="20")
        self.corCortoPanel_in.pack()
        self.corCortoPanel_in.place(x=750, y=120)

        #Eficiencia entrada del panel
        eficianciaPanel_label = Label(self.panelFV, text="Eficiencia [%]:").place(x=900, y=120)
        self.eficianciaPanel_in = Entry(self.panelFV, width="20")
        self.eficianciaPanel_in.pack()
        self.eficianciaPanel_in.place(x=1100, y=120)

        #Tolerancia Potencia nominal entrada del panel
        tolPotencia_label = Label(self.panelFV, text="Tolerancia P. nominal [W(0~)]:").place(x=570, y=150)
        self.tolPanel_in = Entry(self.panelFV, width="20")
        self.tolPanel_in.pack()
        self.tolPanel_in.place(x=750, y=150)

        #Peso de entrada panel.
        pesoPanel_label = Label(self.panelFV, text="Peso [kg]:").place(x=900, y=150)
        self.pesoPanel_in = Entry(self.panelFV, width="20")
        self.pesoPanel_in.pack()
        self.pesoPanel_in.place(x=1100, y=150)

        #Altura de entrada panel.
        altPanel_label = Label(self.panelFV, text="Altura panel [m]:").place(x=570, y=180)
        self.altPanel_in = Entry(self.panelFV, width="20")
        self.altPanel_in.pack()
        self.altPanel_in.place(x=750, y=180)

        #Ancho de entrada del panel.
        anchoPanel_label = Label(self.panelFV, text="Ancho panel [m]:").place(x=900, y=180)
        self.anchoPanel_in = Entry(self.panelFV, width="20")
        self.anchoPanel_in.pack()
        self.anchoPanel_in.place(x=1100, y=180)

        #Espesor de entrada del panel
        espesorPanel_label = Label(self.panelFV, text="Espesor panel [m]:").place(x=570, y=210)
        self.espPanel_in = Entry(self.panelFV, width="20")
        self.espPanel_in.pack()
        self.espPanel_in.place(x=750, y=210)

        #Área célula de entrada del panel.
        areaCelula_label = Label(self.panelFV, text="Área de la célula [Cm2]:").place(x=900, y=210)
        self.areaCelula_in = Entry(self.panelFV, width="20")
        self.areaCelula_in.pack()
        self.areaCelula_in.place(x=1100, y=210)

        #-----------------------------------------------------------------
        #Configuración de los botones agregar, editar, buscar y eliminar.
        #Botón agregar panel.
        agregar_prod = Button(self.panelFV, text="Agregar", width="15", command=self.agregar_panel)
        agregar_prod.pack()
        agregar_prod.place(x=40, y=250)

        #Botón editar panel
        editarprod_boton = Button(self.panelFV, text="Editar", width="15")
        editarprod_boton.pack()
        editarprod_boton.place(x=250, y=250)

        #Botón eliminar panel
        eliminarProd_boton = Button(self.panelFV, text="Eliminar", width="15", command=self.eliminar_panel)
        eliminarProd_boton.pack()
        eliminarProd_boton.place(x=460, y=250)

        #-------------------------------------------------------------------------------
        #Tabla de paneles ingresados a la base de datos bd_FVT a la tabla bd_panel
        self.tabla_paneles = ttk.Treeview(self.panelFV, height=15, columns=("#0","#1","#2","#3","#4","#5","#6","#7","#8","#9","#10","#11"))
        self.tabla_paneles.pack()
        self.tabla_paneles.place(x=10, y=290)
        self.tabla_paneles.column("#0", width=50)#Ancho de la columna ID.
        self.tabla_paneles.heading("#0", text="ID", anchor=CENTER)
        self.tabla_paneles.column("#1", width=100)#Ancho de la columna código.
        self.tabla_paneles.heading("#1", text="Código", anchor=CENTER)
        self.tabla_paneles.column("#2", width=150)#Ancho de la columna Marca.
        self.tabla_paneles.heading("#2", text="Marca", anchor=CENTER)
        self.tabla_paneles.column("#3", width=120)#Ancho de la columna Referencia.
        self.tabla_paneles.heading("#3", text="Referencia", anchor=CENTER)
        self.tabla_paneles.column("#4", width=80)#Ancho de la columna potencia.
        self.tabla_paneles.heading("#4", text="Potencia [Wp]", anchor=CENTER)
        self.tabla_paneles.column("#5", width=70)#Ancho de la columna Vmp.
        self.tabla_paneles.heading("#5", text="Vmp [V]", anchor=CENTER)
        self.tabla_paneles.column("#6", width=70)#Ancho de la columna Imp.
        self.tabla_paneles.heading("#6", text="Imp [A]", anchor=CENTER)
        self.tabla_paneles.column("#7", width=70)#Ancho de la columna Voc.
        self.tabla_paneles.heading("#7", text="Voc [V]", anchor=CENTER)
        self.tabla_paneles.column("#8", width=70)#Ancho de la columna Isc.
        self.tabla_paneles.heading("#8", text="Isc [A]", anchor=CENTER)
        self.tabla_paneles.column("#9", width=70)#Ancho de la columna Ancho.
        self.tabla_paneles.heading("#9", text="Alto [m]", anchor=CENTER)
        self.tabla_paneles.column("#10", width=70)#Ancho de la columna Alto.
        self.tabla_paneles.heading("#10", text="Ancho [m]", anchor=CENTER)
        self.tabla_paneles.column("#11", width=70)#Ancho de la columna Eficiencia.
        self.tabla_paneles.heading("#11", text="Eficiencia [%]", anchor=CENTER)
        self.tabla_paneles.column("#12", width=80)#Ancho de la columna Precio.
        self.tabla_paneles.heading("#12", text="Precio [$]", anchor=CENTER)

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        self.cargar_tab_panel()

        self.panelFV.mainloop()#Fin de la ventana paneles.
    #-------- INICIO INTERVECNION DE CÓDIGO --------

    def cargar_tab_panel(self):
        grabar = self.tabla_paneles.get_children()
        for elementos in grabar:
            self.tabla_paneles.delete(elementos)
        
        #Consulta a la base de datos BDPpal para importar la información de la tabla bd_panel
        consulta = "SELECT * FROM bd_panel ORDER BY id DESC"
        db_filas = self.inicio_consulta(consulta)
        for fila in db_filas: #Genera una lista para desplazarse en las diferentes posiciones de la bd_panel
            self.tabla_paneles.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12], fila[16], fila[17],
            fila[13], fila[5]))
    
    def validar_cam_panel(self): #Código para validar que todos los campos estén diligenciados
        return len(self.codPanel_in.get()) !=0 and len(self.descPanel_in.get()) != 0 and len(self.unidadPanel_in.get()) != 0 and(self.unidadPanel_in.get()) != 0 and len(
            self.precioUnitPanel_in.get()) !=0 and len(self.obs_panel_in.get()) !=0 and len(self.marcaPanel_in.get()) !=0 and len(self.rePanel_in.get()) !=0 and len(
                self.potMaxPanel_in.get()) !=0 and len(self.tensionMaxPanel_in.get()) !=0 and len(self.corMaxPanel_in.get()) !=0 and len(
                    self.tenAbiertoPanel_in.get()) !=0 and len(self.corCortoPanel_in.get()) !=0 and len(self.eficianciaPanel_in.get()) !=0 and len(
                        self.tolPanel_in.get()) !=0 and len(self.pesoPanel_in.get()) !=0 and len(self.altPanel_in.get()) !=0 and len(
                            self.anchoPanel_in.get()) !=0 and len(self.espPanel_in.get()) !=0 and len(self.areaCelula_in.get()) !=0

    def agregar_panel(self): #Función para agregar un panel nuevo
        if self.validar_cam_panel():
            consulta1 = "INSERT INTO bd_panel VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            parametros = (self.codPanel_in.get(), self.marcaPanel_in.get(), self.descPanel_in.get(), self.unidadPanel_in.get(), self.precioUnitPanel_in.get(),
            self.obs_panel_in.get(), self.rePanel_in.get(), self.potMaxPanel_in.get(), self.tensionMaxPanel_in.get(), self.corMaxPanel_in.get(),
            self.tenAbiertoPanel_in.get(), self.corCortoPanel_in.get(), self.eficianciaPanel_in.get(), self.tolPanel_in.get(), self.pesoPanel_in.get(),
            self.altPanel_in.get(), self.anchoPanel_in.get(), self.espPanel_in.get(), self.areaCelula_in.get())
            self.inicio_consulta(consulta1, parametros)
            showinfo(title="Ingreso de paneles FVTools", message="Se ha ingresado el panel correctamente.")
            self.codPanel_in.delete(0, END)
            self.marcaPanel_in.delete(0, END)
            self.descPanel_in.delete(0, END)
            self.unidadPanel_in.delete(0, END)
            self.precioUnitPanel_in.delete(0, END)
            self.obs_panel_in.delete(0, END)
            self.rePanel_in.delete(0, END)
            self.potMaxPanel_in.delete(0, END)
            self.tensionMaxPanel_in.delete(0, END)
            self.corMaxPanel_in.delete(0, END)
            self.tenAbiertoPanel_in.delete(0, END)
            self.corCortoPanel_in.delete(0, END)
            self.eficianciaPanel_in.delete(0, END)
            self.tolPanel_in.delete(0, END)
            self.pesoPanel_in.delete(0, END)
            self.altPanel_in.delete(0, END)
            self.anchoPanel_in.delete(0, END)
            self.espPanel_in.delete(0, END)
            self.areaCelula_in.delete(0, END)
        else:
            showerror(title="ERROR", message="Debes llenar todos los campos.")
        
        self.cargar_tab_panel()

    def eliminar_panel(self): #Función para eliminal un panel
        #Se pregunta si realmente se quiere eliminar el código.
        realEliminar = askquestion(title="Eliminar Panel FV", message="Deseas eliminar el panel seleccionado?")#Código para confirmar la acción de eliminación.

        if realEliminar == "yes":
            try:
                self.tabla_paneles.item(self.tabla_paneles.selection())
            except IndexError as e:
                showerror(title="ERROR", message="Por favor seleccionar el panel a eliminar.")
                return
            parametros2= self.tabla_paneles.item(self.tabla_paneles.selection())["values"][0]
            consulta2 = "DELETE FROM bd_panel WHERE codigo=?"
            print(parametros2)
            print(consulta2, parametros2)
            self.inicio_consulta(consulta2, (parametros2, ))
            self.cargar_tab_panel()
            showinfo(title="Eliminar código", message="El código ha sido eliminado.")
    
    #-------- FIN INTERVECNION DE CÓDIGO --------

    #------------------------------------------ Ventana: BD de los inversores --------------------------------------------------------------------------------------------
    def ven_inversores(self):
        self.inversor = Tk()
        self.inversor.title("BD inversores FVTools")
        self.inversor.geometry("1250x750")
        self.inversor.resizable(width=False, height=False)
        self.inversor.iconbitmap("Icono.ico") #Para relacionar el ícono.

        #Código de los inversores FV
        codInversor_label = Label(self.inversor, text="Código del producto: ").place(x=10, y=30)
        self.codInversor_in = Entry(self.inversor, width="20") #codPanel_in: texto en la tabla bd_inversor
        self.codInversor_in.pack()
        self.codInversor_in.focus()
        self.codInversor_in.place(x=145, y=30)

        #Marca del inversor
        marcaInversor:label = Label(self.inversor, text="Marca: ").place(x=10, y=60)
        self.marInversor_in = Entry(self.inversor, width="20") #@marcaInversor_in: texto en la tabla bd_inversor
        self.marInversor_in.pack()
        self.marInversor_in.place(x=145, y= 60)

        #Referencia inversor
        refInversor_label = Label(self.inversor, text="Referencia: ").place(x=10, y=90)
        self.refInversor_in = Entry(self.inversor, width="20") #@refInversor_in: texto en la tabla bd_inversor
        self.refInversor_in.pack()
        self.refInversor_in.place(x=145, y=90)

        #Potencia máxima de entrada del inversor
        potMaxInv_label = Label(self.inversor, text="Potencia máx. entrada [kWp]: ").place(x=10, y =120)
        self.potMaxInv_in = Entry(self.inversor, width="20") #@potMaxInv_in: float en la tabla bd_inversor 
        self.potMaxInv_in.pack()
        self.potMaxInv_in.place(x=145, y=120)

        #Voltaje máximo a la entrada del inversor
        volMaxInv_label = Label(self.inversor, text="Voltaje máx. entrada [Vdc]: ").place(x=10, y=150)
        self.volMaxInv_in = Entry(self.inversor, width="20") #@volMaxInv: float en la tabla bd_inversor
        self.volMaxInv_in.pack()
        self.volMaxInv_in.place(x=145, y=150)

        #Voltaje nominal DC
        volNomDC_label = Label(self.inversor, text="Voltaje nominal [Vdc]: ").place(x=10, y=180)
        self.volNomDC_in = Entry(self.inversor, width="20") #@volNomDC_in: float en la tabla bd_inversor
        self.volNomDC_in.pack()
        self.volNomDC_in.place(x=145, y=180)

        #Voltaje de arranque
        volInicio_label = Label(self.inversor, text="Voltaje de arranque [Vdc]: ").place(x=10, y=210)
        self.volInicio_in = Entry(self.inversor, width="20") #@volInicio_in: float en la tabla bd_inversor
        self.volInicio_in.pack()
        self.volInicio_in.place(x=145, y=210)

        #Voltaje mínimo en el MPPT
        volMinMPPT_label = Label(self.inversor, text="Voltaje mín. MPPT [Vdc]: ").place(x=10, y=240)
        self.volMinMPPT_in = Entry(self.inversor, width="20") #@volMinMPPT_in: float en la tabla bd_inversor
        self.volMinMPPT_in.pack()
        self.volMinMPPT_in.place(x=145, y=240)

        #Voltaje máximo en el MPPT
        volMaxMPPT_label = Label(self.inversor, text="Voltaje máx. MPPT [Vdc]: ").place(x=10, y=270)
        self.volMaxMPPT_in = Entry(self.inversor, width="20")
        self.volMaxMPPT_in.pack()
        self.volMaxMPPT_in.place(x=145, y=270)

        #Corriente máxima de entrada del inversor
        iMaxIn_label = Label(self.inversor, text="Corriente máx. entrada [Adc]: ").place(x=300, y=30)
        self.iMaxInv_in = Entry(self.inversor, width="20") #@iMaxInv: float en la tabla bd_inversor
        self.iMaxInv_in.pack()
        self.iMaxInv_in.place(x=470, y=30)

        #Corriente máxima de cortocircuito del inversor
        iscInv_label = Label(self.inversor, text="I. máx. cortocircuito [Adc]: ").place(x=300, y=60)
        self.iscInv_in = Entry(self.inversor, width="20") #@iscInv_in: float en la tabla bd_inversor
        self.iscInv_in.pack()
        self.iscInv_in.place(x=470, y=60)

        #Número de MPPT
        numMPPT_label = Label(self.inversor, text="Número de MPPT: ").place(x=300, y=90)
        self.numMPPT_in = Entry(self.inversor, width="20") #@numMPPT_in: entero en la tabla bd_inversor
        self.numMPPT_in.pack()
        self.numMPPT_in.place(x=470, y=90)

        #Número de entradas
        numEntradas_label = Label(self.inversor, text="Número de entradas: ").place(x=300, y=120)
        self.numEntradas_in = Entry(self.inversor, width="20") #@numEntrada_in: entero en la tabla bd_inversor
        self.numEntradas_in.pack()
        self.numEntradas_in.place(x=470, y=120)

        #Potencia máxima de salida
        potSalidaInv_label = Label(self.inversor, text="Pot. nominal [kW]: ").place(x=620, y=30)
        self.potNomInv_in = Entry(self.inversor, width="20") #@potSalidaInv_in: float en la tabla bd_inversor
        self.potNomInv_in.pack()
        self.potNomInv_in.place(x=790, y=30)

        #Frecuencia
        frecInv_label = Label(self.inversor, text="Frecuencia [Hz]: ").place(x=620, y=60)
        self.frecInv_in = Entry(self.inversor, width="20") #@frecInv_in: entero en la tabla bd_inversor
        self.frecInv_in.pack()
        self.frecInv_in.place(x=790, y=60)

        #Sistema eléctrico de operación del inversor
        sistemaElect_label = Label(self.inversor, text="Sistema de operación: ").place(x=620, y=90)
        self.sisElect_in = Combobox(self.inversor, width="17") #@sisElect_in: texto en la tabla bd_inversor
        self.sisElect_in["values"] = ["Monofásico", "Trifásico"]
        self.sisElect_in.set("Trifásico") #El valor "Trifásico" predeterminado
        self.sisElect_in.place(x=790, y=90)

        #Tensión AC de operación

        tenInvAC_label = Label(self.inversor, text="Tensión de operación: ").place(x=620, y=120)
        self.tenInvAC_in = Entry(self.inversor, width="20") #@tenInvAC_in: Entero en la tabla bd_inversor
        self.tenInvAC_in.pack()
        self.tenInvAC_in.place(x=790, y=120)
        
        #Corriente máxima de salida
        imaxInvAC_label = Label(self.inversor, text="Corriente máx. salida [A]: ").place(x=620, y=150)
        self.imaxInvAC_in = Entry(self.inversor, width="20") #@imaxInvAC: float en la tabla bd_inversor
        self.imaxInvAC_in.pack()
        self.imaxInvAC_in.place(x=790, y=150)

        #Factor de potencia
        FPInv_label = Label(self.inversor, text="Factor de potencia: ").place(x=620, y=180)
        self.FPInv_in = Entry(self.inversor, width="20") #@FPInv_in: float en la tabla bd_inversor
        self.FPInv_in.pack()
        self.FPInv_in.place(x=790, y=180)

        #Eficiencia
        efiInv_label = Label(self.inversor, text="Eficiencia [%]: ").place(x=620, y=210)
        self.efiInv_in = Entry(self.inversor, width="20") #@efiInv_in: float en la tabla bd_inversor
        self.efiInv_in.pack()
        self.efiInv_in.place(x=790, y=210)

        #Observaciones
        obsInv_label = Label(self.inversor, text="Observaciones: ").place(x=620, y=240)
        self.obsInv_in = Entry(self.inversor, width="60") #@obsInv_in: texto en la tabla bd_inversor
        self.obsInv_in.pack()
        self.obsInv_in.place(x=790,y=240)

        #Precio
        precioInv_label = Label(self.inversor, text="Precio [$]: ").place(x=620, y=270)
        self.precioInv_in = Entry(self.inversor, width="20") #@precioInv_in: float en la tabla bd_inversor
        self.precioInv_in.pack()
        self.precioInv_in.place(x=790, y=270)

        #Rangos de tensión en AC----------------------------

        rangoAC_label = Label(self.inversor, text="Rango de operación").place(x=930, y=30)

        #Voltaje AC mínimo
        volMinAC_label = Label(self.inversor, text="V. mín. AC [V]:").place(x=930, y=60)
        self.volMinAC_in = Entry(self.inversor, width="20") #@volMinAC_in: float en la tabla bd_inversor
        self.volMinAC_in.pack()
        self.volMinAC_in.place(x=1050, y=60)

        #Voltaje AC máximo
        volMaxAC_label = Label(self.inversor, text="V. máx. AC [V]:").place(x=930, y=90)
        self.volMaxAC_in = Entry(self.inversor, width="20") #@volMaxAC_in: float en la tabla bd_inversor
        self.volMaxAC_in.pack()
        self.volMaxAC_in.place(x=1050, y=90)

        #-----------------------------------------------------------------
        #Configuración de los botones agregar, editar, buscar y eliminar.

        #Botón agregar inversor.
        agregar_inv = Button(self.inversor, text="Agregar", width="15", command=self.agregar_inv)
        agregar_inv.pack()
        agregar_inv.place(x=40, y=300)

        #Botón editar inversor
        editar_inv = Button(self.inversor, text="Editar", width="15")
        editar_inv.pack()
        editar_inv.place(x=300, y=300)

        #Botón eliminar inversor
        eliminar_inv = Button(self.inversor, text="Eliminar", width="15")
        eliminar_inv.pack()
        eliminar_inv.place(x=575, y=300)

        #----------------------------------------------------------------------------------

        #Tabla de inversores ingresados a la base de datos.
        self.tabla_inversor = ttk.Treeview(self.inversor, height="15", columns=("#0","#1","#2","#3","#4","#5","#6","#7","#8","#9","#10","#11","#12","#13","#14"))
        self.tabla_inversor.pack()
        self.tabla_inversor.place(x=40, y=330)
        self.tabla_inversor.column("#0", width=50)#Ancho de la columna ID
        self.tabla_inversor.heading("#0", text="ID", anchor=CENTER)
        self.tabla_inversor.column("#1", width=120)#Ancho de la columna Referencia
        self.tabla_inversor.heading("#1", text="Referencia", anchor=CENTER)
        self.tabla_inversor.column("#2", width=60)#Ancho de la columna pot. máx DC
        self.tabla_inversor.heading("#2", text="P. máx. DC [kW]", anchor=CENTER)
        self.tabla_inversor.column("#3", width=60)#Ancho de la columna voltaje máximo a la entrada del inversor DC
        self.tabla_inversor.heading("#3", text="V. máx. entrada [Vdc]", anchor=CENTER)
        self.tabla_inversor.column("#4", width=60)#Ancho de la columna voltaje mín. en el puerto MPPT
        self.tabla_inversor.heading("#4", text="V. mín. MPPT [Vdc]", anchor=CENTER)
        self.tabla_inversor.column("#5", width=60)#Ancho de la columna voltaje máx. en el puerto MPPT
        self.tabla_inversor.heading("#5", text="V. máx. MPPT [Vdc]", anchor=CENTER)
        self.tabla_inversor.column("#6", width=60)#Ancho de la columna corriente máxima a la entrada del inversor
        self.tabla_inversor.heading("#6", text="I. máx. [A]", anchor=CENTER)
        self.tabla_inversor.column("#7", width=60)#Ancho de la columna corriente de cortocircuito permisible por el inversor
        self.tabla_inversor.heading("#7", text="I. cortocircuito [A]", anchor=CENTER)
        self.tabla_inversor.column("#8", width=60)#Ancho de la columna Nro. de MPPT´s
        self.tabla_inversor.heading("#8", text="Nro. MPPT", anchor=CENTER)
        self.tabla_inversor.column("#9", width=60)#Ancho de la columna Nro. de entradas por MPPT
        self.tabla_inversor.heading("#9", text="Nro. entradas", anchor=CENTER)
        self.tabla_inversor.column("#10", width=100)#Ancho de la columna Sistema eléctrico
        self.tabla_inversor.heading("#10", text="Sistema", anchor=CENTER)
        self.tabla_inversor.column("#11", width=60)#Ancho de la columna Pot. máxima a la salida del inversor
        self.tabla_inversor.heading("#11", text="P. máx a la salida [kW]", anchor=CENTER)
        self.tabla_inversor.column("#12", width=60)#Ancho de la columna voltaje AC nominal del inversor
        self.tabla_inversor.heading("#12", text="V. nominal [V]", anchor=CENTER)
        self.tabla_inversor.column("#13", width=60)#Ancho de la columna corriente AC nominal del inversor
        self.tabla_inversor.heading("#13", text="I. nominal [V]", anchor=CENTER)
        self.tabla_inversor.column("#14", width=60)#Ancho de la columna precio del inversor
        self.tabla_inversor.heading("#14", text="Precio [USD]", anchor=CENTER)
        #self.tabla_inversor.column("#15", width=100)#Ancho de la columna voltaje AC nominal del inversor
        #self.tabla_inversor.heading("#15", text="Observaciones", anchor=CENTER)

        Style = ttk.Style()
        Style.theme_use("default")
        Style.map("Treeview")
        
        self.cargar_tab_inversor()

        self.inversor.mainloop()#Fin de la ventana inversor.

    def cargar_tab_inversor(self):
        grabar = self.tabla_inversor.get_children()
        for elementos in grabar:
            self.tabla_inversor.delete(elementos)

        #Consulta a la base de datos para importar la información de la tabla bd_inversor
        consulta = "SELECT * FROM bd_inversor ORDER BY id DESC"
        db_filas = self.inicio_consulta(consulta)
        for fila in db_filas:
            self.tabla_inversor.insert("", 0, text=fila[0], values=(fila[3], fila[4], fila[5], fila[6], fila[7], fila[10], fila[11], 
            fila[12], fila[13], fila[16], fila[14], fila[17], fila[18], fila[22]))

    def validar_cam_inv(self): #ódigo para validar que todos los campos estén diligenciados
        return len(self.codInversor_in.get()) !=0 and len(self.marInversor_in.get()) !=0 and len(self.refInversor_in.get()) !=0 and len(self.potMaxInv_in.get()) !=0 and  len(
            self.volMaxInv_in.get()) !=0 and len(self.volNomDC_in.get()) !=0 and len(self.volInicio_in.get()) !=0 and len(self.volMinMPPT_in.get()) !=0 and len(
                self.volMaxMPPT_in.get()) !=0 and len(self.iMaxInv_in.get()) !=0 and len(self.iscInv_in.get()) !=0 and len(self.numMPPT_in.get()) !=0 and len(
                    self.numEntradas_in.get()) !=0 and len(self.potNomInv_in.get()) !=0 and len(self.frecInv_in.get()) !=0 and len(self.sisElect_in.get()) and len(
                        self.tenInvAC_in.get()) !=0 and len(self.imaxInvAC_in.get()) !=0 and len(self.FPInv_in.get()) !=0 and len(self.efiInv_in.get()) !=0 and len(
                            self.obsInv_in.get()) !=0 and len(self.precioInv_in.get()) !=0 and len(self.volMinAC_in.get()) !=0 and len(self.volMaxAC_in.get())

    def agregar_inv(self): #Función para agregar n inversor nuevo
        if self.validar_cam_inv():
            consulta1 = "INSERT INTO bd_inversor VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" #24 DATOS
            parametros = (self.codInversor_in.get(), self.marInversor_in.get(), self.refInversor_in.get(), self.potMaxInv_in.get(), self.volMaxInv_in.get(), 
            self.volNomDC_in.get(), self.volInicio_in.get(),self.volMinMPPT_in.get(), self.volMaxMPPT_in.get(), self.iMaxInv_in.get(), self.iscInv_in.get(),
            self.numMPPT_in.get(), self.numEntradas_in.get(), self.potNomInv_in.get(),self.frecInv_in.get(), self.sisElect_in.get(), self.tenInvAC_in.get(),
            self.imaxInvAC_in.get(), self.FPInv_in.get(), self.efiInv_in.get(), self.obsInv_in.get(), self.precioInv_in.get(), self.volMinAC_in.get(),
            self.volMaxAC_in.get())
            self.inicio_consulta(consulta1, parametros)
            showinfo(title="Ingreso de inversores FVTools", message="Se ha agregado el inversor correctamente.")
            self.codInversor_in.delete(0, END) #1
            self.marInversor_in.delete(0, END) #2
            self.refInversor_in.delete(0, END) #3
            self.potMaxInv_in.delete(0, END) #4
            self.volMaxInv_in.delete(0,END) #5
            self.volNomDC_in.delete(0, END) #6
            self.volInicio_in.delete(0, END) #7
            self.volMinMPPT_in.delete(0, END) #8
            self.volMaxMPPT_in.delete(0, END) #9
            self.iMaxInv_in.delete(0, END) #10
            self.iscInv_in.delete(0, END) #11
            self.numMPPT_in.delete(0, END) #12
            self.numEntradas_in.delete(0, END) #13
            self.potNomInv_in.delete(0, END) #14
            self.frecInv_in.delete(0, END) #15
            self.sisElect_in.delete(0, END) #16
            self.tenInvAC_in.delete(0, END) #17
            self.imaxInvAC_in.delete(0, END) #18
            self.FPInv_in.delete(0, END) #19
            self.efiInv_in.delete(0, END) #20
            self.obsInv_in.delete(0, END) #21
            self.precioInv_in.delete(0, END) #22
            self.volMinAC_in.delete(0, END) #23
            self.volMaxAC_in.delete(0, END) #24
        else:
            showerror(title="ERROR", message="Desbes llenar todos los campos.")

        self.cargar_tab_inversor()

    def ven_materiales(self):
        self.materiales = Tk()
        self.materiales.title("BD materiales FVTools")
        self.materiales.geometry("1250x650")
        self.materiales.resizable(width=False, height=False)
        self.materiales.iconbitmap("Icono.ico") #Para relacionar el ícono.

        #Código de entrada
        codigo_label = Label(self.materiales, text="Código de producto:").place(x=10, y=30)
        self.codigo_in = Entry(self.materiales, width="20") #@codigo_in: es un texto en la tabla bd_materiales.
        self.codigo_in.pack()
        self.codigo_in.focus()
        self.codigo_in.place(x=140, y=30)      

        #Descripción de entrada
        descrip_label = Label(self.materiales, text="Descripción: ").place(x=10, y=60)
        self.descrip_in = Entry(self.materiales, width="70") #@descrip_in: es un texto en la tabla bd_materiales.
        self.descrip_in.pack()
        self.descrip_in.place(x=140, y=60)

        #Unidad de entrada
        unidad_label = Label(self.materiales, text="Unidad: ").place(x=10, y=90)
        self.unidad_in = Combobox(self.materiales, width="10") #@unida_in: es un texto en la tabla bd_materiales.
        self.unidad_in["values"] = ["Und.", "m", "ml", "kg", "Global", "Galón"]
        self.unidad_in.set("Und.") #El valor de "Und." predeterminado
        self.unidad_in.place(x=140, y=90)

        #Precio unitario de entrada
        precio_unit_label = Label(self.materiales, text="Precio unitario: ").place(x=10, y=120)
        self.precio_unit_in = Entry(self.materiales, validate = "key", validatecommand=(self.materiales.register(self.solonumero), "%S"), width="20")
        #@precio_unit_in: es un entero en la tabla bd_materiales.
        self.precio_unit_in.pack()
        self.precio_unit_in.place(x=140, y=120)

        #Observaciones de entrada
        obs_label = Label(self.materiales, text="Observaciones: ").place(x=10, y=150)
        #self.obs_text = scrolledtext.ScrolledText(self.materiales, width="50", height="5") #@obs_text: es un texto en la tabla bd_materiales.
        self.obs_text = Entry(self.materiales, width="60")
        self.obs_text.pack
        self.obs_text.place(x=140, y=150)

        #-----------------------------------------------------------------
        #Configuración de los botones agregar, editar, buscar y eliminar.
        #Botón agregar producto.
        agregar_prod = Button(self.materiales, text="Agregar", width="15", command=self.agregar_producto)
        agregar_prod.pack()
        agregar_prod.place(x=40, y=250)

        #Botón editar producto
        editarprod_boton = Button(self.materiales, text="Editar", width="15", command=self.ven_edit_materiales)
        editarprod_boton.pack()
        editarprod_boton.place(x=300, y=250)

        #Botón eliminar producto
        eliminarProd_boton = Button(self.materiales, text="Eliminar", width="15", command=self.eliminar_producto)
        eliminarProd_boton.pack()
        eliminarProd_boton.place(x=575, y=250)

        #--------------------------------------------------------------------

        #Tabla de materiales ingresados a la base de datos.
        self.tabla_materiales = ttk.Treeview(self.materiales, height=15, columns=("#0", "#1", "#2", "#3", "#4"))
        self.tabla_materiales.pack()
        self.tabla_materiales.place(x=40, y=290)
        self.tabla_materiales.column("#0", width=50)#Ancho de la columna ID.
        self.tabla_materiales.heading("#0", text="ID", anchor=CENTER)
        self.tabla_materiales.column("#1", width=100)#Ancho de la columna código.
        self.tabla_materiales.heading("#1", text="Código", anchor=CENTER)
        self.tabla_materiales.column("#2", width=300)#Ancho de la columna código.
        self.tabla_materiales.heading("#2", text="Producto", anchor=CENTER)
        self.tabla_materiales.column("#3", width=100)
        self.tabla_materiales.heading("#3", text="Unidad", anchor=CENTER)
        self.tabla_materiales.column("#4", width=100)
        self.tabla_materiales.heading("#4", text="V. unitario", anchor=CENTER)
        self.tabla_materiales.column("#5", width=520)#Ancho de la columna Observaciones.
        self.tabla_materiales.heading("#5", text="Observaciones", anchor=CENTER)

        #scroll_tabla = Scrollbar(self.tabla_materiales, orient=VERTICAL)
        #scroll_tabla.pack(side=RIGHT, fill=Y)
        #self.tabla_materiales.config(yscrollcommand=scroll_tabla.set)
        #scroll_tabla.config(command=self.tabla_materiales.yview)

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        self.cargar_tab_materiales()

        self.materiales.mainloop()#Fin de la ventana materiales.
    
    def cargar_tab_materiales(self):
        grabar = self.tabla_materiales.get_children()
        for elementos in grabar:
            self.tabla_materiales.delete(elementos)

        #Consulta a la base de datos para importar la información de la tabla bd_materiales
        consulta = "SELECT * FROM bd_materiales ORDER BY id DESC "
        db_filas = self.inicio_consulta(consulta)
        for fila in db_filas:
            self.tabla_materiales.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5]))

    def validar_campos(self): #El "return" devuelve un True o False si existen datos ingresados o no.
        return len(self.codigo_in.get()) != 0 and len(self.descrip_in.get()) != 0 and len(self.unidad_in.get()) != 0 and len(self.precio_unit_in.get()) != 0

    def agregar_producto(self):
        if self.validar_campos():
            consulta1 = "INSERT INTO bd_materiales VALUES(NULL, ?, ?, ?, ?, ?)"
            parametros = (self.codigo_in.get(), self.descrip_in.get(), self.unidad_in.get(), self.precio_unit_in.get(), self.obs_text.get())
            self.inicio_consulta(consulta1, parametros)
            showinfo(title="Ingreso de materiales FVTools", message="Se ha ingresado el material correctamente.")
            self.codigo_in.delete(0, END)
            self.descrip_in.delete(0, END)
            self.unidad_in.delete(0, END)
            self.precio_unit_in.delete(0, END)
            self.obs_text.delete(0, END)
        else:
            showerror(title="ERROR", message="Debes llenar todos los campos.")
        
        self.cargar_tab_materiales()
    
    def eliminar_producto(self):
        #Se pregunta si realmente se quiere eliminar el código.
        realEliminar = askquestion(title="Eliminar código", message="Deseas eliminar el código seleccionado?")#Código para confirmar la acción de eliminación.

        if realEliminar == "yes":
            try:
                self.tabla_materiales.item(self.tabla_materiales.selection())
            except IndexError as e:
                showerror(title="ERROR", message="Por favor seleccionar el código a eliminar.")
                return
            parametros2= self.tabla_materiales.item(self.tabla_materiales.selection())["values"][0]
            consulta2 = "DELETE FROM bd_materiales WHERE codigo=?"
            print(parametros2)
            print(consulta2, parametros2)
            self.inicio_consulta(consulta2, (parametros2, ))
            self.cargar_tab_materiales()
            showinfo(title="Eliminar código", message="El código ha sido eliminado.")
    
    def ven_edit_materiales(self):
        self.edit_materiales = Tk()
        self.edit_materiales.title("Edición de materiales.")
        self.edit_materiales.geometry("600x300")
        self.edit_materiales.resizable(width=False, height=False)
        self.edit_materiales.iconbitmap("Icono.ico")

        try:
            self.tabla_materiales.item(self.tabla_materiales.selection())
        except IndexError as e:
            showerror(title="ERROR", message="Debes seleccionar algún item o material.")
            return
        #Código actual.
        self.codigo_actual = self.tabla_materiales.item(self.tabla_materiales.selection())["values"][0]
        self.codigoEntry = StringVar(self.edit_materiales, value=self.codigo_actual)
        Label(self.edit_materiales, text="Código actual:").place(x=10, y=10)
        self.codigo_actual_in = Entry(self.edit_materiales, textvariable=self.codigoEntry, width="20")#@codigo_actual_in: es un texto de la tabla bd_mateiales.
        self.codigo_actual_in.pack()
        self.codigo_actual_in.place(x=140, y=10)

        #descripción actual.
        self.desc_actual = self.tabla_materiales.item(self.tabla_materiales.selection())["values"][1]
        self.descEntry = StringVar(self.edit_materiales, value=self.desc_actual)
        Label(self.edit_materiales, text="Descripción actual:").place(x=10, y=40)
        self.desc_actual_in = Entry(self.edit_materiales, textvariable=self.descEntry, width="70")
        self.desc_actual_in.pack()
        self.desc_actual_in.place(x=140, y=40)

        #Unidad actual
        self.unidad_actual = self.tabla_materiales.item(self.tabla_materiales.selection())["values"][2]
        Label(self.edit_materiales, text="Unidad actual").place(x=10, y=70)
        self.unidad_actual_in = Combobox(self.edit_materiales, width="10")
        self.unidad_actual_in["values"] = [self.unidad_actual, "Und.", "m", "ml", "kg", "Global"]
        self.unidad_actual_in.set(self.unidad_actual)
        self.unidad_actual_in.place(x=140, y=70)

        #Precio actual
        self.precio_actual = self.tabla_materiales.item(self.tabla_materiales.selection())["values"][3]
        self.precioEntry = StringVar(self.edit_materiales, value=self.precio_actual)
        Label(self.edit_materiales, text="Precio actual:").place(x=10, y=100)
        self.precio_act_in = Entry(self.edit_materiales, textvariable=self.precioEntry, width="20")
        self.precio_act_in.pack()
        self.precio_act_in.place(x=140, y=100)

        #Obs actual
        self.obs_actual = self.tabla_materiales.item(self.tabla_materiales.selection())["values"][4]
        self.obsEntry = StringVar(self.edit_materiales, value=self.obs_actual)
        Label(self.edit_materiales, text="Observación actual:").place(x=10, y=130)
        self.obs_act_in = Entry(self.edit_materiales, textvariable=self.obsEntry, width="70")
        self.obs_act_in.pack()
        self.obs_act_in.place(x=140, y=130)

        #Botón guardar cambios
        guardaCambios = Button(self.edit_materiales, text="Guardar ", width="15", command=lambda: self.guardar_edi_materiales(self.codigo_actual_in.get(), 
        self.codigo_actual, self.desc_actual_in.get(), self.desc_actual, self.unidad_actual_in.get(), self.unidad_actual, 
        self.precio_act_in.get(), self.precio_actual, self.obs_act_in.get(), self.obs_actual))
        guardaCambios.pack()
        guardaCambios.place(x=140, y=170)

    def guardar_edi_materiales(self, codigo_nuevo, codigo_anterior, desc_nueva, desc_anterior, unidad_nueva, unidad_anterior, precio_nuevo, precio_anterior, obs_nueva, obs_anterior):
        consulta3 = "UPDATE bd_materiales SET codigo=?, descripcion=?, unidad=?, precio_unitario=?, observaciones=? WHERE codigo=? AND descripcion=? AND unidad=? AND precio_unitario=? AND observaciones=?"
        parametros3 = (codigo_nuevo, desc_nueva, unidad_nueva, precio_nuevo, obs_nueva, codigo_anterior, desc_anterior, unidad_anterior, precio_anterior, obs_anterior)
        self.inicio_consulta(consulta3, parametros3)
        showinfo(title="Edición de productos", message="Se ha actualizado el producto: "+ desc_nueva +" correctamente.")
        self.cargar_tab_materiales()

if __name__ == "__main__":
    loginPpal = Tk()
    aplicacion = FVTools(loginPpal)
    loginPpal.mainloop()
