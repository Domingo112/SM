
import flet as ft
def email(page:ft.Page):
    msg=ft.Text("",color="red")
    button=ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", on_click=lambda e: page.navigate("/register"))
    domain=(".com",".org")
    def email(usermail):
        Mail=usermail.value.lower().strip()
        if not "@" in Mail:
            msg.value="Invalid email"
            Email.border_color="red"
        elif not Mail:
            msg.value="Fill in your email"
            Email.border_color="red"
        elif ";" in Mail:
            msg.value="Invalid email"
            Email.border_color="red"
        elif not Mail.endswith(domain):
            msg.value="Invalid email"
            Email.border_color="red"
        else:
            
            my_dict=page.session.store.get("my_list")
            my_dict.append(Mail)
            page.session.store.set("my_dict",my_dict)
            page.navigate("/fullinfo")
    Email=ft.TextField(label="Email",hint_text="email@gmail.com",border_radius=5,prefix_icon=ft.Icons.MAIL_LOCK,bgcolor="color")
    page.views.append(
            ft.View(
                route="/email_register",
                controls=[
                    button,
                   msg,
                    ft.Container(
                        content=ft.Column(
                            controls=Email,
                        ),
                        padding=20
                    ),
                    ft.Container(
                        ft.IconButton(ft.Icon(ft.icons.Icons.ARROW_CIRCLE_RIGHT,color="white",size=28), bgcolor="#2A7FFF",on_click=lambda e :email(Email)),
                        alignment=ft.Alignment.CENTER
                    )
                ]
            )
        )
    page.window.width=330
    page.window.height=700
    page.title="Register"
    page.bgcolor="#0A3D9B"