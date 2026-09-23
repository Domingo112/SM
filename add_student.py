import os
import sqlite3
import flet as ft
def AddStudent(page: ft.Page):
    page.views.append(
        ft.View(
            route="/add"
        )
    )
    page.clean()
    page.bgcolor = "#F5F8FF"
    page.window.width=330
    page.window.height=700
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.appbar = ft.AppBar(
        bgcolor="#1565D8",
        leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", on_click=lambda e: page.navigate("/staff_dashboard")),
        title=ft.Text("Add Student", color="white", size=16, weight="bold"),
        actions=[ft.IconButton(icon=ft.Icons.SEARCH, icon_color="white")],
    )
    domain=(".com",".org")
    msg1=ft.Text("",color="green",weight="bold")
    msg2=ft.Text("",color="red")
    button=ft.Button(
                        "add_Student",
                        icon=ft.Icons.PERSON_ADD,
                        bgcolor="#1565D8",
                        color="white",
                        width=page.window.width,
                        height=46,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=22)),
                        on_click=lambda e: addstudent(Full_Name,Registration_Number,Gender,Accesscode,Email,department)
                    )
    department=ft.TextField(hint_text="Department", prefix_icon=ft.Icons.SCHOOL)
    Email=ft.TextField(hint_text="Email Address", prefix_icon=ft.Icons.MAIL_LOCK)
    Accesscode=ft.TextField(hint_text="Accesscode", prefix_icon=ft.Icons.KEY)
    Gender= ft.Dropdown(
                width=230,
                hint_text="Select gender",
                hint_style=ft.TextStyle(size=12, color="black"),
                border_radius=10,
                border_color="#E5E7EB",
                bgcolor="black",
                content_padding=12,
                text_size=13,
                options=[ft.dropdown.Option("Male"), ft.dropdown.Option("Female")]
                            )
    Registration_Number= ft.TextField(hint_text="Enter registration number", prefix_icon=ft.Icons.PERSON_OUTLINE)
    Full_Name=ft.TextField(hint_text="Enter student's full name", prefix_icon=ft.Icons.PERSON_OUTLINE)
    def addstudent(name,regno,gen,acc,mail,dept):
        username=name.value
        user_reg=regno.value
        user_gen=gen.value
        user_acc=acc.value
        user_mail=mail.value.lower().strip()
        user_dept=dept.value
        msg=ft.Text("")
        msg.value
        if not username :
            msg2.value = "fill in student Fullname"
        elif not user_dept:
            msg2.value = "fill in student Department"    
        elif not user_reg:
            msg2.value="fill in student Regno"   
        elif not user_gen:
            msg2.value="fill in student gender"
        elif  not user_acc:
            msg2.value="fill in student accesscode"
        elif not user_mail:
            msg2.value="fill in student Email"
        elif not user_reg.isdigit():
            msg2.value="Reg number must be a number"
        elif not "@" in user_mail:
            msg.value="invalid Email"
        elif not user_mail.endswith(domain):
            msg2.value="Invalid Email" 
        elif ";" in user_mail:
                msg.value="Invalid email"
        elif len(user_acc)< 6:
            msg2.value("Access should be more than 6")        
        else:
            print("valid")
            try: 
                DB_NAME=os.path.join(os.path.dirname(__file__),"student_management.db") 
                conn=sqlite3.connect(DB_NAME)
                c=conn.cursor()
                c.execute("insert into users(fullname,email,reg_no,gender,Accesscode,Dept) values(?,?,?,?,?,?)",(username,user_mail,user_reg,user_gen,user_acc,user_dept,))
                msg1.value="Registration successful"
                conn.commit()
                           
            except Exception as e:
                print(f"error{e}")
            finally:
                conn.close()         
                                              
                
    def input_field(hint, icon=None):
        return ft.TextField(
            hint_text=hint,
            hint_style=ft.TextStyle(size=12, color="#9CA3AF"),
            prefix_icon=icon,
            border_radius=10,
            border_color="#E5E7EB",
            bgcolor="white",
            content_padding=12,
            text_size=13,
        )
    def dropdown_field(hint, options):
        return ft.Dropdown(
            hint_text=hint,
            hint_style=ft.TextStyle(size=12, color="#9CA3AF"),
            border_radius=10,
            border_color="#E5E7EB",
            bgcolor="white",
            content_padding=12,
            text_size=13,
            options=[ft.dropdown.Option(o) for o in options],
        )
    page.add(
        ft.Container(
            padding=14,
            content=ft.Column(
                spacing=14,
                controls=[
                    
                    ft.Column(spacing=4, controls=[
                        ft.Row(spacing=6, controls=[ft.Icon(ft.Icons.PERSON, size=16, color="#374151"), ft.Text("Full Name", size=12, weight="bold",color="black")]),
                        Full_Name
                    ]),
                    #put mail textfield here
                    ft.Column(spacing=4, controls=[
                        ft.Row(spacing=6, controls=[ft.Icon(ft.Icons.MAIL, size=16, color="black"), ft.Text("Email Address", size=12, weight="bold",color="black")]),
                        Email
                    ]),
                    ft.Column(spacing=4, controls=[
                        ft.Row(spacing=6, controls=[ft.Icon(ft.Icons.BADGE, size=16, color="#374151"), ft.Text("Registration Number", size=12, weight="bold",color="black")]),
                        Registration_Number
                    ]),
                     ft.Column(spacing=4, controls=[
                        ft.Row(spacing=6, controls=[ft.Icon(ft.Icons.WC, size=16, color="#374151"), ft.Text("Gender", size=12, weight="bold",color="black")]),
                       Gender
                    ]),
                    ft.Column(spacing=4, controls=[
                        ft.Row(spacing=6, controls=[ft.Icon(ft.Icons.SCHOOL, size=16, color="#374151"), ft.Text("Department", size=12, weight="bold",color="black")]),
                        department
                        ]),
                    ft.Column(spacing=4, controls=[
                        ft.Row(spacing=6, controls=[ft.Icon(ft.Icons.LOCK, size=16, color="black"), ft.Text("Access Code", size=12, weight="bold",color="black")]),
                        Accesscode
                    ]),msg2,msg1,
                    ft.Container(height=10),
                    
                    button,
                    ft.Container(height=30)
                ]
            )
        )
    )
    page.update()
    