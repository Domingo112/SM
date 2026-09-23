import flet as ft
import os
import sqlite3


def loginING(page: ft.Page):
    
    Email = ft.TextField(
        label="Email",
        hint_text="email@gmail.com",
        prefix_icon=ft.Icons.MAIL_OUTLINE_ROUNDED,
        border_radius=14,
        filled=True,
        bgcolor="white",
        border_color="#E5E7EB",
        focused_border_color="#2A7FFF",
        color="black",
        height=52,
        text_size=13,
        label_style=ft.TextStyle(color="grey"),
        cursor_color="#2A7FFF",
    )
    Password = ft.TextField(
        label="Password",
        hint_text="••••••••",
        prefix_icon=ft.Icons.LOCK_OUTLINE_ROUNDED,
        password=True,
        can_reveal_password=True,
        border_radius=14,
        filled=True,
        bgcolor="white",
        border_color="#E5E7EB",
        focused_border_color="#2A7FFF",
        color="black",
        height=52,
        text_size=13,
        label_style=ft.TextStyle(color="grey"),
        cursor_color="#2A7FFF",
    )

    def loginIn(mail, password):
        Mail = mail.value.strip().lower()
        word = password.value
        if Mail == "admin@gmail.com" and word == "admin":
            page.navigate("/staff_dashboard")

        if not Mail:
            Email.border_color = "red"
        elif not word:
            Password.border_color = "red"
        else:

            DB_NAME = os.path.join(os.path.dirname(__file__), "student_management.db")
            conn = sqlite3.connect(DB_NAME)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(
                "Select * from users where email = ? AND Accesscode = ?",
                (
                    Mail,
                    word,
                ),
            )
            details = c.fetchone()
            if details:
                print("login Succesful")
                id = details["id"]
                fullname=details["fullname"]
                regNo=details["reg_no"]
                dept=details["Dept"]
                page.session.store.set("id",id)
                page.session.store.set("fullname",fullname)
                page.session.store.set("reg_no",regNo)
                page.session.store.set("dept",dept)
                page.navigate("/student")
            else:
                print("login Failed")

            conn.commit()

            conn.close()

    def go_signup():
        page.navigate("/register")

    page.views.append(
        ft.View(
            route="/",
            padding=0,
            bgcolor="#0A3D9B",
            scroll=ft.ScrollMode.AUTO,  # <-- SCROLL ADDED
            controls=[
                ft.Container(
                    expand=True,
                    padding=24,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(0, -1),
                        end=ft.Alignment(0, 1),
                        colors=["#0A3D9B", "#0F5CFF"],
                    ),
                    content=ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(height=40),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=3,
                                controls=[
                                    ft.Icon(
                                        ft.Icons.SCHOOL_ROUNDED, color="white", size=28
                                    ),
                                    ft.Text(
                                        "Maglo", size=24, weight="bold", color="white"
                                    ),
                                    ft.Text(
                                        "Uni", size=24, weight="bold", color="#7DB2FF"
                                    ),
                                ],
                            ),
                            ft.Container(height=20),
                            ft.Text(
                                "Welcome Back!", size=22, weight="w700", color="white"
                            ),
                            ft.Text(
                                "Login to continue your journey",
                                size=12,
                                color="#BBD0FF",
                            ),
                            ft.Container(height=30),
                            ft.Container(
                                width=360,
                                bgcolor="white",
                                border_radius=28,
                                padding=24,
                                shadow=ft.BoxShadow(
                                    blur_radius=30,
                                    color=ft.Colors.with_opacity(0.2, "black"),
                                    offset=ft.Offset(0, 10),
                                ),
                                content=ft.Column(
                                    spacing=18,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "Login",
                                            size=16,
                                            weight="bold",
                                            color="black",
                                        ),
                                        Email,
                                        Password,
                                        ft.Container(
                                            alignment=ft.Alignment.CENTER_RIGHT,
                                            content=ft.TextButton(
                                                ft.Text("Forgotten password"),
                                                style=ft.ButtonStyle(
                                                    color="#2A7FFF",
                                                    text_style=ft.TextStyle(
                                                        size=11, weight="bold"
                                                    ),
                                                ),
                                            ),
                                        ),
                                        ft.Container(
                                            width=400,
                                            height=54,
                                            bgcolor="#2A7FFF",
                                            border_radius=14,
                                            shadow=ft.BoxShadow(
                                                blur_radius=15,
                                                color=ft.Colors.with_opacity(
                                                    0.3, "#2A7FFF"
                                                ),
                                            ),
                                            alignment=ft.Alignment.CENTER,
                                            ink=True,
                                            on_click=lambda e: loginIn(Email, Password),
                                            content=ft.Text(
                                                "Login",
                                                size=15,
                                                weight="bold",
                                                color="white",
                                            ),
                                        ),
                                        ft.Container(height=5),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=2,
                                            controls=[
                                                ft.Text(
                                                    "Don't have an account?",
                                                    size=11,
                                                    color="#6B7280",
                                                ),
                                                ft.TextButton(
                                                    ft.Text("sign up"),
                                                    on_click=go_signup,
                                                    style=ft.ButtonStyle(
                                                        color="#2A7FFF",
                                                        text_style=ft.TextStyle(
                                                            size=11, weight="bold"
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                            ft.Container(height=30),
                            ft.Text(
                                "Track • Manage • Excel",
                                size=10,
                                color=ft.Colors.with_opacity(0.6, "white"),
                            ),
                        ],
                    ),
                )
            ],
        )
    )
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 330
    page.window.height = 700
    page.bgcolor = "#0A3D9B"
