import flet as ft
from config import config_page_sf

def main(page: ft.Page):
    page.title = "Dropdown"
    page = config_page_sf(page)

    # Función que maneja el cambio en el dropdown y actualiza el color
    def change_dropdown(e):
        selected_color = color_dropdown.content.controls[0].value
        if selected_color:
            lbl_resultado.content.value = f"Has seleccionado: {selected_color}"
        else:
            lbl_resultado.content.value = "No se ha seleccionado un color"
        change_color(selected_color)
        page.update()
        
    # Función para cambiar el color y estilo según el color seleccionado
    def change_color(selected_color):
        if not selected_color:
            lbl_resultado.content.bgcolor = ft.colors.WHITE
            lbl_resultado.content.color = "black"
            lbl_resultado.content.size = 14
            lbl_resultado.content.font_family = "Verdana"
        else:
            # Restaurar los estilos generales
            lbl_resultado.content.color = "white"
            lbl_resultado.content.size = 14
            lbl_resultado.content.font_family = "Verdana"
            
            # Cambiar el fondo basado en la selección
            if selected_color == "Red":
                lbl_resultado.content.bgcolor = ft.colors.RED
            elif selected_color == "Green":
                lbl_resultado.content.bgcolor = ft.colors.GREEN
            elif selected_color == "Blue":
                lbl_resultado.content.bgcolor = ft.colors.BLUE
            elif selected_color == "Yellow":
                lbl_resultado.content.bgcolor = ft.colors.YELLOW
                lbl_resultado.content.color = "black"  # Texto negro para fondo amarillo

    # Contenedor del resultado (texto centrado y estilo por defecto)
    lbl_resultado = ft.Container(
        content=ft.Text(
            value="No se ha seleccionado un color",  # Valor por defecto
            width=230, 
            color="black",
            bgcolor="white", 
            size=14, 
            font_family="Verdana",
            text_align=ft.TextAlign.CENTER  # Alineación del texto centrada
        ),
        alignment=ft.alignment.center,  # Centrar el contenedor en la página
        padding=ft.padding.all(10)  # Padding para darle espacio
    )
    
    # Dropdown de selección de color
    color_dropdown = ft.Container(
        content=ft.Row(
            controls=[
                ft.Dropdown(
                    label="Color",
                    width=150,
                    options=[
                        ft.dropdown.Option("Red"),
                        ft.dropdown.Option("Green"),
                        ft.dropdown.Option("Blue"),
                        ft.dropdown.Option("Yellow"),
                    ],
                    on_change=change_dropdown
                )
            ],
            alignment="center"
        ),
        margin=ft.Margin(left=10, top=20, right=10, bottom=20)
    )
    
    # Botón de cerrar
    btn_close = ft.Container(
        content=ft.ElevatedButton(
            text="Cerrar",
            icon=ft.icons.CLOSE,
            on_click=lambda e: page.window.close(),
            icon_color=ft.colors.WHITE,
            bgcolor=ft.colors.RED_700,
            color=ft.colors.WHITE
        ),
        alignment=ft.alignment.center,
        margin=ft.Margin(left=0, top=20, right=0, bottom=0)
    )

    # Añadir todos los elementos a la página
    page.add(color_dropdown, lbl_resultado, btn_close)

ft.app(target=main)
