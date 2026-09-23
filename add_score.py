import os,sqlite3
import flet as ft
def ViewAddScores(page: ft.Page):
    page.views.append(
        ft.View(
            route="/add_score"
        )
    )
    page.clean()
    page.bgcolor = "#F5F8FF"
    page.padding = 0
    page.appbar = ft.AppBar(
        bgcolor="#1565D8",
        leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", on_click=lambda e: page.navigate("/staff_dashboard")),
        title=ft.Text("Add Scores", color="white", size=16, weight="bold"),
    )
    dept=page.session.store.get("dept")
    ide=page.session.store.get("id")
    msg=ft.Text("",color="red")
    msg2=ft.Text("",color="green",weight="bold")
    firsttext=ft.Text(" ", size=12, color="#111827")
    first_field=ft.TextField( text_size=12, border="none", dense=True, text_align=ft.TextAlign.CENTER)
    secondtext=ft.Text("Biology", size=12, color="#111827")
    second_field=ft.TextField( text_size=12, border="none", dense=True, text_align=ft.TextAlign.CENTER)
    thirdtext=ft.Text("Biology", size=12, color="#111827")
    third_field=ft.TextField( text_size=12, border="none", dense=True, text_align=ft.TextAlign.CENTER)
    fourthtext=ft.Text("Biology", size=12, color="#111827")
    fourth_field=ft.TextField( text_size=12, border="none", dense=True, text_align=ft.TextAlign.CENTER)
    fifthtext=ft.Text("Biology", size=12, color="#111827")
    fifth_field=ft.TextField( text_size=12, border="none", dense=True, text_align=ft.TextAlign.CENTER)
    def info():
       
        print(dept)
        
        if dept == "Computer Engineering":
            print(dept)
            firsttext.value="EGR 111"
            
            secondtext.value="COMEGR 101"
            thirdtext.value ="COMEGR 102"
            fourthtext.value="COMEGR 103"
            fifthtext.value="COMEGR 103"
        if dept == "computer science" :
            firsttext.value="EGR 101" 
            secondtext.value="COM 111"
            thirdtext.value ="COM 112"
            fourthtext.value="COM 113"
            fifthtext.value="COM 114"
        if dept == "SLT":
        
            firsttext.value="SWT 111"
                    
            secondtext.value="SLT 101"
            thirdtext.value ="SLT 102"
            fourthtext.value="SLL 103"
            fifthtext.value="GNS 110"
        if dept == "Electrical Engineering"  :
                    firsttext.value="EGR 111"
                    
                    secondtext.value="EEE 101"
                    thirdtext.value ="EEC 102"
                    fourthtext.value="EEC 103"
                    fifthtext.value="GNS 103"        
               
            
    def score(f,s,t,fo,firth):
        firstti=f.value
        secondti=s.value
        thirdti=t.value
        fourtti=fo.value
        fiftti=firth.value   
        if not firstti :
            msg.value="Fill all score and fill it correctly"
        elif not secondti:
             msg.value="Fill all score and fill it correctly"
        elif not thirdti:
            msg.value="Fill all score and fill it correctly"
        elif not fourtti:
            msg.value="Fill all score and fill it correctly"
        elif not fiftti:
            msg.value="Fill all score and fill it correctly"               
        else:
            try: 
                DB_NAME=os.path.join(os.path.dirname(__file__),"student_management.db") 
                conn=sqlite3.connect(DB_NAME)
                c=conn.cursor()
                c.execute("insert into score(userid,score1,score2,score3,score4,score5) values(?,?,?,?,?,?)",(ide,firstti,secondti,thirdti,fourtti,fiftti,))
                msg2.value=" Scores Uploaded Successful"
                conn.commit()
                         
            except Exception as e:
                          print(f"error{e}")
            finally:
                          conn.close()      
              
        
        
    page.add(
        ft.Container(
            bgcolor="white",
            border_radius=ft.BorderRadius.only(top_left=20, top_right=20),
            margin=ft.Margin.only(top=10),
            padding=16,
            content=ft.Column(spacing=14, controls=[
#USER CARD
                ft.Container(
                    bgcolor="white",
                    border=ft.Border.all(1, "#F1F5F9"),
                    border_radius=12,
                    padding=12,
                    content=ft.Row(spacing=12, controls=[
                        ft.CircleAvatar(
                            radius=24,
                            bgcolor="#DBEAFE",
                            content=ft.Icon(ft.Icons.PERSON, color="#1565D8", size=28)
                        ),
                        ft.Column(spacing=2, controls=[
                            ft.Text("Emmanuel Eshiet", size=14, weight="bold", color="black"),
                            ft.Text("SS2 · 412", size=11, color="#6B7280")
                        ])
                    ])
                ),
                ft.Text("Subject Scores", size=13, weight="bold", color="#111827"),
#Mathematics
                ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                    firsttext,
                    ft.Container(
                        width=85,
                        height=36,
                        border=ft.Border.all(1, "#E5E7EB"),
                        border_radius=8,
                        padding=ft.Padding.only(left=10, right=10),
                        alignment=ft.Alignment.CENTER,
                        content=first_field
                    )
                ]),
#English Language
                ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                    secondtext,
                    ft.Container(
                        width=85, height=36,
                        border=ft.Border.all(1, "#E5E7EB"), border_radius=8,
                        padding=ft.Padding.only(left=10, right=10), alignment=ft.Alignment.CENTER,
                        content=second_field
                    )
                ]),
#Physics
                ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                    thirdtext,
                    ft.Container(
                        width=85, height=36,
                        border=ft.Border.all(1, "#E5E7EB"), border_radius=8,
                        padding=ft.Padding.only(left=10, right=10), alignment=ft.Alignment.CENTER,
                        content=third_field
                    )
                ]),
#Chemistry
                ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                    fourthtext,
                    ft.Container(
                        width=85, height=36,
                        border=ft.Border.all(1, "#E5E7EB"), border_radius=8,
                        padding=ft.Padding.only(left=10, right=10), alignment=ft.Alignment.CENTER,
                        content=fourth_field
                    )
                ]),
#Biology
                ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                    fifthtext,
                    ft.Container(
                        width=85, height=36,
                        border=ft.Border.all(1, "#E5E7EB"), border_radius=8,
                        padding=ft.Padding.only(left=10, right=10), alignment=ft.Alignment.CENTER,
                        content=fifth_field
                    )
                ]),msg,msg2,
#Total Score
                ft.Container(
                    bgcolor="#F0F6FF",
                    border_radius=10,
                    padding=12,
                    content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                        ft.Text("Total Score", size=12, weight="bold", color="#111827"),
                        ft.Text("401", size=12, weight="bold", color="#111827")
                    ])
                ),
# Save Button
                ft.Container(
                    bgcolor="#1565D8",
                    on_click=lambda e:score(first_field,second_field,third_field,fourth_field,fifth_field),
                    border_radius=10,
                    padding=ft.Padding.only(top=12, bottom=12),
                    alignment=ft.Alignment.CENTER,
                    content=ft.Row(alignment=ft.MainAxisAlignment.CENTER, spacing=8, controls=[
                        ft.Icon(ft.Icons.SAVE, size=16, color="white"),
                        ft.Text("Save Scores", size=13, weight="bold", color="white")
                    ])
                ),
            ])
        )
    )
    page.window.width=330
    page.window.height=700
    info()
    page.update()
    