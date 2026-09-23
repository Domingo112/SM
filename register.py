
import sqlite3
import flet as ft
import os
def register(page:ft.Page):
    page.views.append(
        ft.View(
            route="/"
        )
    )
    page.window.width=300
    page.window.height=700
    page.title="Register"
    page.bgcolor="#0A3D9B"

    title=ft.Text("Maglo",size=22, weight=ft.FontWeight.BOLD, color="white")
    title2=ft.Text("Uni",size=22, weight=ft.FontWeight.BOLD, color="#7DB2FF")

    Firstname=ft.TextField(label="Fullname",hint_text="e.g Emmanuel",width=160,border_radius=12, filled=True, bgcolor="white", prefix_icon=ft.Icons.PERSON)
    lastname=ft.TextField(label="Surname",hint_text="e.g Eshiet",width=160,border_radius=12, filled=True, bgcolor="white", prefix_icon=ft.Icons.PERSON_OUTLINE)
    my_list = []
    print(my_list)

    def info(name1,name2):
        name=name1.value.strip().capitalize()
        lastname1=name2.value.strip().capitalize()
        if not name :
            Firstname.border_color="red"
        elif not lastname1:
            lastname.border_color="red"
        else:
            users_name=name +" "+lastname1
            my_list.append(users_name)
            hi=my_list
            page.session.store.set("my_list",hi)
            page.navigate("/email_register")
            return hi

    page.add(
        ft.Container(
            expand=True,
            gradient=ft.LinearGradient(begin=ft.Alignment(0,-1), end=ft.Alignment(0,1), colors=["#0A3D9B", "#082E73"]),
            padding=20,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(controls=[title,title2], alignment=ft.MainAxisAlignment.CENTER, spacing=2),
                    ft.Icon(ft.Icons.SCHOOL, size=50, color="white"),
                    ft.Text("Maglo Uni", size=18, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Container(height=15),
                    ft.Container(
                        width=360,
                        bgcolor="white",
                        border_radius=20,
                        padding=20,
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=12,
                            controls=[
                                ft.Text("Registration Form",size=18, weight=ft.FontWeight.BOLD, color="#0A3D9B", text_align="center"),
                                ft.Row(controls=[Firstname,lastname], alignment=ft.MainAxisAlignment.CENTER, spacing=10, wrap=True),
                                ft.Container(
                                    content=ft.IconButton(ft.Icon(ft.icons.Icons.ARROW_CIRCLE_RIGHT,color="white",size=28), bgcolor="#2A7FFF", on_click=lambda e:info(Firstname,lastname)),
                                    width=55, height=55, bgcolor="#2A7FFF", border_radius=27, alignment=ft.Alignment.CENTER
                                ),
                                ft.Container(
                                    content=ft.Text("Already have an account",color="#2A7FFF", weight=ft.FontWeight.BOLD),
                                    on_click=lambda e : page.navigate("/"),
                                    padding=10
                                ),
                            ]
                        )
                    )
                ]
            )
        )
    )
   