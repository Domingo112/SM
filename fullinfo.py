
import flet as ft
import sqlite3
import os

def complete_registration(page: ft.Page):
    page.title = "Complete Registration"
    page.window.width = 330
    page.window.height = 700
    msg = ft.Text("", color="red")
    msg3=ft.Text(str(" "),color="red")
    sucess_message=ft.Text(" ",color="#086623",weight="bold",text_align="center")
    space=ft.Text(" ")
    
    button = ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", on_click=lambda e: page.navigate("/register"))
    regno = ft.TextField(
        label="Enter Regno.",
        prefix_icon=ft.Icons.PERSON,
        border_radius=12,
        width=320,
        height=48,
        filled=True,
        
        border_color=ft.Colors.TRANSPARENT
    )
    Accesscode = ft.TextField(
        label="Input access code",
        prefix_icon=ft.Icons.KEY,
        border_radius=12,
        width=320,
        height=48,
        filled=True,
        border_color=ft.Colors.TRANSPARENT,
        password=True,
        can_reveal_password=True
    )
    gender = ft.Dropdown(
        label="Select gender",
        width=300,
        border_radius=12,
        filled=True,
        bgcolor="grey",
        color="white",
        border_color=ft.Colors.TRANSPARENT,
        options=[ft.dropdown.Option("Male"), ft.dropdown.Option("Female")]
    )
    Department = ft.Dropdown(
        label="Select department",
        width=300,
        border_radius=12,
        filled=True,
        bgcolor="grey",
        color="grey",
        border_color=ft.Colors.TRANSPARENT,
        options=[
            ft.dropdown.Option("computer science"),
            ft.dropdown.Option("SLT"),
            ft.dropdown.Option("Electrical Engineering"),
            ft.dropdown.Option("Computer Engineering"),
        ]
    )
    form = ft.Column([
        ft.Icon(ft.Icons.SCHOOL, size=60, color=ft.Colors.WHITE),
        ft.Text("Maglo Uni", size=22, weight="bold", color="white", text_align="center", width=320),
        ft.Text("Track • Manage • Excel", size=12, color="#BBD0FF", text_align="center", width=320),
        ft.Divider(height=10, color="transparent"),
        ft.Divider(height=2, thickness=2, color="#3A6FD1"),
        ft.Divider(height=15, color="transparent"),
        sucess_message,space,
        regno,
        gender,
        Department,
        Accesscode,
        msg3,
        ft.Divider(height=10, color="transparent"),
        
        ft.Row([
            ft.Button(
                "Submit",
                width=90,
                height=20,
                bgcolor="#2A7FFF",
                
                color="white",
                
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)
                ),on_click= lambda e:submit(regno,Accesscode,gender,Department)
            )
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=20, color="transparent"),
        ft.Icon(ft.Icons.MENU_BOOK, color="#88A9E6", size=35),
        ft.Text("Better Tracking. Brighter Futures.", size=11, color="#88A9E6", italic=True, text_align="center", width=320)
    ], spacing=12, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    #putting my database here
    def submit(Reg,acccode,gen,dep):
        Regno=Reg.value
        Acckey=acccode.value
        Gen=gen.value
        Dept=dep.value
        futher_details=page.session.store.get("my_dict")
        if not futher_details:
            futher_details=["Nil","Nil"]
        
        else:    
            futher_details[:2]
            fullname=futher_details[0]
            userMail=futher_details[1]
        
        if not Regno :
            regno.border_color="red"
            msg3.value="Reg no is Empty"
            
        elif not Acckey:
            Accesscode.border_color="red"
            msg3.value="input your AccessCode"
            
        elif not gen:
            gender.border_color="red"
            msg3.value="Pick your gender"
            
        elif not dep:
            Department.border_color="red"
            msg.value="Pick your departmentr"
        elif not Regno.isdigit():
          msg3.value="Reg no should be a number"
        elif len(Acckey) < 6 :
            msg3.value=("put must be > 6")
        else:
            try: 
                DB_NAME=os.path.join(os.path.dirname(__file__),"student_management.db") 
                conn=sqlite3.connect(DB_NAME)
                c=conn.cursor()
                c.execute("insert into users(fullname,email,reg_no,gender,Accesscode,Dept) values(?,?,?,?,?,?)",(fullname,userMail,Regno,Gen,Acckey,Dept,))
                sucess_message.value=" Successful[login]"
                conn.commit()
               
            except Exception as e:
                print(f"error{e}")
            finally:
                conn.close()         
                    
    def load_error():
        list_details=page.session.store.get("my_dict")
        if  list_details == []:
            page.navigate("/")
            
    page.views.append(
        ft.View(
            route="/fullinfo",
            bgcolor="#0A3D9B",
            controls=[
                ft.Container(
                    expand=True,
                    gradient=ft.LinearGradient(
                        
                        
                        colors=["#0A3D9B", "#123A8A"]
                    ),
                    padding=15,
                    content=ft.Column(
                        controls=[
                            ft.Row([button]),
                            form
                        ],
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            ]
        )
    )
    load_error()
    page.update()
   
   
