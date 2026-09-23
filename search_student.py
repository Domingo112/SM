import os
import sqlite3
import flet as ft
def ViewStudents(page: ft.Page):
    page.views.append(
        ft.View(
            route="/search"
        )
    )
    page.clean()
    page.window.width=330
    page.window.height=700
    page.bgcolor = "#F5F8FF"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.appbar = ft.AppBar(
        bgcolor="#1565D8",
        leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", on_click=lambda e: page.navigate("/staff_dashboard")),
        title=ft.Text("View Students", color="white", size=16, weight="bold"),
        actions=[ft.IconButton(icon=ft.Icons.SEARCH, icon_color="white")],
    )
    name=ft.Text(" ")
    result=ft.Column(spacing=8,scroll=ft.ScrollMode.AUTO)
    # Single Student Row
    def student_item(name, klass,score):
        def delete(e,deleteid=score):
            DB_NAME=os.path.join(os.path.dirname(__file__),"student_management.db") 
            conn=sqlite3.connect(DB_NAME)
            c=conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")
            c.execute("delete from users where id = ?",(deleteid,))
            conn.commit()
            conn.close()
            userview(search_box)
            page.update() 
            print(f"deleted{deleteid}")   
        def clicking(e,the_id=score):
            page.session.store.set("id",the_id)
            page.navigate("/details")
            
        
        
        return ft.Container(
            bgcolor="white",
            padding=2,
            border_radius=10,
            margin=ft.Margin.only(bottom=8),
            on_click=lambda e: print(f"Clicked {name}"),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        spacing=1,
                        controls=[
                            ft.CircleAvatar(
                                radius=18,
                                bgcolor="#DBEAFE",
                                content=ft.Icon(ft.Icons.PERSON, color="#1565D8", size=18)
                            ),
                            ft.Column(
                                spacing=1,
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(name, size=12, weight="bold", color="black"),
                                    ft.Row(spacing=6, controls=[
                                        ft.Text(klass, size=10, color="#6B7280"),
                                        ft.Text("·", size=10, color="#6B7280"),
                                        ft.Text(str(score), size=10, color="#6B7280"),
                                        ft.Container(
                                            
                                            border_radius=10,
                                            padding=ft.Padding.only(left=8, right=8, top=2, bottom=2),
                                            content=ft.Text( size=8,  weight="bold")
                                        )
                                    ])
                                ]
                            )
                        ]
                    ),
                    ft.IconButton(ft.Icons.DELETE,icon_color="red",on_click=delete),
                    ft.IconButton(ft.Icons.CHEVRON_RIGHT,on_click=clicking)
                ]
            )
        )
    
    search_box =  ft.TextField(
                        hint_text="Search students...",
                        hint_style=ft.TextStyle(size=12, color="#9CA3AF"),
                        border_color="transparent",
                        bgcolor="transparent",
                        content_padding=8,
                        text_size=12,
                        expand=True,
                        border_width=0,
                        on_change= lambda e:userview(search_box)
                    )
    
        
      
    def userview(search):
        search_item=search.value
        like=f"%{search_item}%"
        DB_NAME=os.path.join(os.path.dirname(__file__),"student_management.db") 
        conn=sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        c=conn.cursor()
        c.execute("select * from users where fullname like ? or Dept like ?",(like,like,))
        items=c.fetchall()
        result.controls.clear()
        
        
        for item in items:
            if not item:
                result.controls.append(ft.Text("Search Not found",size=15,color="black"))
            else:
                
                
                hmm=student_item(item["fullname"],item["Dept"],item['id'])
                
                result.controls.append(hmm)
              
                       
            
            
            
        
    page.add(
        
        ft.Container(
            padding=12,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
        bgcolor="#F3F4F6",
        border_radius=10,
        padding=ft.Padding.only(left=12, right=12),
        margin=ft.Margin.only(bottom=10),
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.SEARCH, size=18, color="#6B7280"),
               search_box
            ]
        )
    ),
                    
                    result,
                    ft.Container(height=30)
                ]
            )
        )
    )
    userview(search_box)
    page.update()
 