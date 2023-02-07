"""
Crearemos un programa en python usando tkinter
- Ventanas
- Menus (Inicio, añadir, información, salir)
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos en SQLite
- Mostrar los datos en una lista
"""

from tkinter import *
from tkinter import ttk
ventana = Tk()
#definir ventana
#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.title("CRUD productos")
ventana.resizable(0, 0)

#pantallas
def home():

    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20,
    )
    home_label.grid(
        row=0,
        column=0
    )
    separador_tabla.grid(row=1)
    products_box.grid(row=2)

    for product in products:

        if len(product) == 3:
            products_box.insert('', 0, text=product[0], values=(product[1]))
            product.append("added")

    #ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()


def add():
    add_frame.grid(row=1)
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=110,
        pady=20,
    )
    add_label.grid(
        row=0,
        column=0,
        columnspan=4
    )
    #campos del formulario
    add_name_label.grid(row=1, column=0, padx=5, pady=5)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(width=30, height=5, padx=15, pady=15)

    add_label_separator.grid(row=4)

    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    # ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

def info():

    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=37,
        pady=20
    )
    info_label.grid(
        row=0,
        column=0
    )

    data_label.grid(
        row=1,
        column=0
    )
    # ocultar otras pantallas
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()

#declarar pantallas
home_label = Label(ventana, text="Inicio")
#products_box = Frame(ventana, width=250)
separador_tabla = Label(ventana)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)


add_label = Label(ventana, text="Añadir producto")
info_label = Label(ventana, text="Información de producto")
data_label = Label(ventana, text="Creado por Rafael Juárez")

#varibales de la aplicación

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c"),
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)
    print(products)
    home()

products = []
name_data = StringVar()
price_data = StringVar()

#cargar formularios
add_frame = Frame(ventana)
add_name_label= Label(add_frame, text="Nombre del producto:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label= Label(add_frame, text="Precio del producto:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label= Label(add_frame, text="Descripción del producto:")
add_description_entry = Text(add_frame)

add_label_separator = Label(add_frame, text="")

boton = Button(add_frame, text="Guardar", command=add_product)

#cargar pantalla de Inicio
home()

#menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio",
                          command=home)
menu_superior.add_command(label="Añadir",
                          command=add)
menu_superior.add_command(label="Información",
                          command=info)
menu_superior.add_command(label="Salir",
                          command=ventana.quit)

ventana.config(menu=menu_superior)
#cargar ventana
ventana.mainloop()