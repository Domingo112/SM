import os
import sqlite3
import flet as ft
def ViewStudentDetails(page: ft.Page):
    page.views.append(
        ft.View(
            route="/details"
        )
    )
    page.clean()
    page.bgcolor = "#F5F8FF"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.appbar = ft.AppBar(
        bgcolor="#1565D8",
        leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", on_click=lambda e: page.navigate("/search")),
        title=ft.Text("Search Student", color="white", size=16, weight="bold"),
    )
    volt=ft.Column(spacing=8,scroll=ft.ScrollMode.AUTO)
    text=ft.Text("", size=13, weight="bold", color="black")
    reg=ft.Text("", size=10, color="#6B7280")
    def detail_row(icon, label, value):
        return ft.Container(
            padding=ft.Padding.only(bottom=14),
            content=ft.Row(
                controls=[
                    ft.Row(spacing=8, width=110, controls=[
                        ft.Icon(icon, size=16, color="#6B7280"),
                        ft.Text(label, size=12, color="#6B7280")
                    ]),
                    ft.Text(value, size=12, weight="bold", color="black")
                ]
            )
        )
    def details():
        ide=page.session.store.get("id")
        print(ide)
        DB_NAME=os.path.join(os.path.dirname(__file__),"student_management.db") 
        conn=sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        c=conn.cursor()
        c.execute("select * from users where id=?",(ide,))
        items=c.fetchall()
        volt.controls.clear()
        
        for item in items:
            text.value=item['fullname']
            reg.value=item['reg_no']
            dept=item["Dept"]
            id=item['id']
            page.session.store.set("dept",dept)
            page.session.store.set("id",id)
            
            volt.controls.append(detail_row(ft.icons.Icons.PERSON ,"Name",item["fullname"]))
            volt.controls.append(detail_row(ft.icons.Icons.SCHOOL ,"Dept",item["Dept"]))
            volt.controls.append(detail_row(ft.icons.Icons.PERSON ,"Gender",item["gender"]))
            volt.controls.append(detail_row(ft.icons.Icons.PERSON ,"Email",item["email"]))
            
        page.update()   
           
    page.add(
        ft.Container(
            bgcolor="white",
            border_radius=ft.BorderRadius.only(top_left=20, top_right=20),
            margin=ft.Margin.only(top=10),
            padding=14,
            content=ft.Column(
                spacing=0,
                controls=[

                    ft.Container(
                        bgcolor="white",
                        border=ft.Border.all(1, "#E5E7EB"),
                        border_radius=10,
                        padding=ft.Padding.only(left=12, right=12),
                        content=ft.Row(controls=[
                            
                            
                        ])
                    ),
                    
                    ft.Container(height=14),

                    ft.Container(
                        bgcolor="white",
                        border=ft.Border.all(1, "#E5E7EB"),
                        border_radius=12,
                        padding=12,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Row(spacing=10, controls=[
                                    ft.CircleAvatar(
                                        radius=22,
                                        bgcolor="#DBEAFE",
                                        content=ft.Icon(ft.Icons.PERSON, color="#1565D8", size=22)
                                    ),
                                    ft.Column(spacing=2, controls=[
                                        text,
                                        ft.Row(spacing=6, controls=[
                                            ft.Text("REGNO", size=10, color="#6B7280"),
                                            ft.Text("·", size=10),
                                            reg,
                                           
                                        ])
                                    ])
                                ]),
                                ft.Icon(ft.Icons.CHEVRON_RIGHT, size=18, color="#9CA3AF")
                            ]
                        )
                    ),
                    
                    volt,
                    ft.Container(
                        bgcolor="#1565D8",
                        border_radius=10,
                        padding=ft.Padding.only(top=12, bottom=12),
                        alignment=ft.Alignment.CENTER,
                        on_click=lambda e:page.navigate("/add_score"),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=8,
                            controls=[
                                ft.Icon(ft.Icons.BAR_CHART, size=16, color="white"),
                                ft.Text("Add score", size=13, color="white", weight="bold")
                            ]
                        )
                    ),
                    
                    ft.Container(height=30)
                ]
            )
        )
    )
    details()
    page.window.height=700
    page.window.width=330
    page.update()
 