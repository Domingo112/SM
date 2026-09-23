import os,sqlite3
import flet as ft
def resultmain(page: ft.Page):
    page.views.append(
        ft.View(
            route="/result"
        )
    )
    page.bgcolor = "#F0F7FF"
    page.padding = 0
    page.window.width = 330
    page.window.height = 800
    page.scroll = ft.ScrollMode.AUTO
    page.title = "View Results"
    name = "Emmanuel Eshiet"
    class_roll = "SS2  •  Roll No: 412"
    firsttext=ft.Text("Mathematics", size=12, color="#0F172A", width=110)                          
    secondtext=ft.Text("Mathematics", size=12, color="#0F172A", width=110)
    thirdtext=ft.Text("Mathematics", size=12, color="#0F172A", width=110)
    fourthtext=ft.Text("Mathematics", size=12, color="#0F172A", width=110)
    fifthtext=ft.Text("Mathematics", size=12, color="#0F172A", width=110)
    dept=page.session.store.get("dept")
    ide=page.session.store.get("id")
    score1=ft.Text("0", size=12, color="#0F172A", width=35)
    score2=ft.Text("0", size=12, color="#0F172A", width=35)
    score3=ft.Text("0", size=12, color="#0F172A", width=35)
    score4=ft.Text("0", size=12, color="#0F172A", width=35)
    score5=ft.Text("0", size=12, color="#0F172A", width=35)
    grade1=ft.Text("none", size=12, color="#0F172A", width=35)
    grade2=ft.Text("none", size=12, color="#0F172A", width=35)
    grade3=ft.Text("none", size=12, color="#0F172A", width=35)
    grade4=ft.Text("none", size=12, color="#0F172A", width=35)
    grade5=ft.Text("none", size=12, color="#0F172A", width=35)
    
    resultext1=ft.Text("none")
    resultext2=ft.Text("none")
    resultext3=ft.Text("none")
    resultext4=ft.Text("none")
    resultext5=ft.Text("none")
    def result():
        DB_NAME = os.path.join(os.path.dirname(__file__), "student_management.db")
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(
        "Select * from score where userid=?",(ide,))
        avg=c.fetchall()
        for av in avg:
           
            score1.value=av["score1"]
            score2.value=av["score2"]
            score3.value=av["score3"]
            score4.value=av["score4"]
            score5.value=av["score5"]
            if av["score1"] <=100:
                grade1.value="A"
                resultext1.value="Passed"
                resultext1.color="#15803D" 
            if av["score1"] <=74:
                grade1.value="AB"
                resultext1.value="Passed"
                resultext1.color="#15803D" 
            if av["score1"] <=65:
                grade1.value="B"
                resultext1.value="Passed"
                resultext1.color="#15803D" 
            if av["score1"] <=55:
                grade1.value="C"
                resultext1.value="Passed"
                resultext1.color="#15803D"
            if av["score1"] <=45:
                grade1.value="D"
                resultext1.value="Passed"
                resultext1.color="#15803D" 
            if av["score1"] <=40:
                grade1.value="E"
                resultext1.value="Fair pass"
                resultext1.color="#edc001" 
            if av["score1"] <=39:
                grade1.value="F" 
                resultext1.value="Failed"
                resultext1.color="red" 
        #for grade2
            if av["score2"] <=100:
                grade2.value="A"
                resultext2.value="Passed"
                resultext2.color="#15803D" 
            if av["score2"] <=74:
                grade2.value="AB"
                resultext2.value="Passed"
                resultext2.color="#15803D" 
            if av["score2"] <=65:
                grade2.value="B"
                resultext2.value="Passed"
                resultext2.color="#15803D" 
            if av["score2"] <=55:
                grade2.value="C"
                resultext2.value="Passed"
                resultext2.color="#15803D" 
            if av["score2"] <=45:
                grade2.value="D"
                resultext2.value="Passed"
                resultext2.color="#15803D" 
            if av["score2"] <=40:
                grade2.value="E"
                resultext2.value=" Fair pass"
                resultext2.color="#edc001" 
            if av["score2"] <=39:
                grade2.value="F"
                resultext2.value="Failed"
                resultext2.color="red"  
        #for grade3
            if av["score3"] <=100:
                grade3.value="A"
                resultext3.value="Passed"
                resultext3.color="#15803D"  
            if av["score3"] <=74:
                grade3.value="AB"
                resultext3.value="Passed"
                resultext3.color="#15803D" 
            if av["score3"] <=65:
                grade3.value="B"
                resultext3.value="Passed"
                resultext3.color="#15803D" 
            if av["score3"] <=55:
                grade3.value="C"
                resultext3.value="Passed"
                resultext3.color="#15803D" 
            if av["score3"] <=45:
                grade3.value="D"
                resultext3.value="Passed"
                resultext3.color="#15803D" 
            if av["score3"] <=40:
                grade3.value="E"
                resultext3.value="Fair pass"
                resultext3.color="#edc001" 
            if av["score3"] <=39:
                grade3.value="F"
                resultext3.value="Failed"
                resultext3.color="red"  
        # for grade4
            if av["score4"] <=100:
                grade4.value="A"
                resultext4.value="Passed"
                resultext4.color="#15803D" 
            if av["score4"] <=74:
                grade4.value="AB"
                resultext4.value="Passed"
                resultext4.color="#15803D" 
            if av["score4"] <=65:
                grade4.value="B"
                resultext4.value="Passed"
                resultext4.color="#15803D" 
            if av["score4"] <=55:
                grade4.value="C"
                resultext4.value="Passed"
                resultext4.color="#15803D" 
            if av["score4"] <=45:
                grade4.value="D"
                resultext4.value="Passed"
                resultext4.color="#15803D" 
            if av["score4"] <=40:
                grade4.value="E"
                resultext4.value="Fair pass"
                resultext4.color="#edc001" 
            if av["score4"] <=39:
                grade4.value="F"
                resultext4.value="Failed"
                resultext4.color="red" 
        #for grade5
            if av["score5"] <=100:
                grade5.value="A"
                resultext5.value="Passed"
                resultext5.color="#15803D"  
            if av["score5"] <=74:
                grade5.value="AB"
                resultext5.value="Passed"
                resultext5.color="#15803D" 
            if av["score5"] <=65:
                grade5.value="B"
                resultext5.value="Passed"
                resultext5.color="#15803D" 
            if av["score5"] <=55:
                grade5.value="C"
                resultext5.value="Passed"
                resultext5.color="#15803D" 
            if av["score5"] <=45:
                grade5.value="D"
                resultext5.value="Passed"
                resultext5.color="#15803D" 
            if av["score5"] <=40:
                grade5.value="E"
                resultext5.value="Fair Pass"
                resultext5.color="#edc001" 
            if av["score5"] <=39:
                grade5.value="F"
                resultext1.value="Failed"
                resultext1.color="red"                                         
    print(dept)
    def pill(text):
        return ft.Container(
            bgcolor="#D1FAE5",
            border_radius=20,
            padding=ft.Padding.only(left=10, right=10, top=4, bottom=4),
            content=ft.Text(text, size=10, color="#15803D", weight="bold")
        )
    def on_back(e):
        print("Back to dashboard")
        page.navigate("/student")
    def on_report(e):
        print("View Detailed Report clicked")
    
    def resultdetail():
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
    page.add(
        ft.Container(
            width=330,
            bgcolor="white",
            border_radius=20,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=ft.Column(
                spacing=0,
                controls=[
#HEADER
                    ft.Container(
                        bgcolor="#0B4DB8",
                        padding=ft.Padding.only(left=10, right=16, top=40, bottom=14),
                        content=ft.Row(
                            spacing=12,
                            controls=[
                                ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", icon_size=20, on_click=on_back),
                                ft.Text("View Results", color="white", size=15, weight="bold"),
                            ]
                        )
                    ),

#TITLE
                    ft.Container(
                        padding=ft.Padding.only(left=14, right=14, top=16, bottom=8),
                        content=ft.Text("Subject Results", size=14, weight="bold", color="#0F172A")
                    ),
#TABLE HEADER
                    ft.Container(
                        bgcolor="#EFF6FF",
                        padding=ft.Padding.only(left=12, right=12, top=10, bottom=10),
                        margin=ft.Margin.only(left=14, right=14),
                        border_radius=ft.BorderRadius.only(top_left=8, top_right=8),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text("Subject", size=11, weight="bold", color="#475569", width=110),
                                ft.Text("Score", size=11, weight="bold", color="#475569", width=35),
                                ft.Text("Grade", size=11, weight="bold", color="#475569", width=35),
                                ft.Text("Status", size=11, weight="bold", color="#475569", width=60),
                            ]
                        )
                    ),
#ABLE ROWS
                    ft.Container(
                        margin=ft.Margin.only(left=14, right=14),
                        bgcolor="white",
                        border=ft.Border.all(1, "#EFF6FF"),
                        border_radius=ft.BorderRadius.only(bottom_left=8, bottom_right=8),
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.Container(padding=ft.Padding.only(left=12, right=12, top=12, bottom=12), content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[firsttext,score1 , grade1, resultext1])),
                                ft.Divider(height=1, color="#F1F5F9"),
                                ft.Container(padding=ft.Padding.only(left=12, right=12, top=12, bottom=12), content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[secondtext, score2, grade2, resultext2])),
                                ft.Divider(height=1, color="#F1F5F9"),
                                ft.Container(padding=ft.Padding.only(left=12, right=12, top=12, bottom=12), content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[thirdtext, score3, grade3, resultext3])),
                                ft.Divider(height=1, color="#F1F5F9"),
                                ft.Container(padding=ft.Padding.only(left=12, right=12, top=12, bottom=12), content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[fourthtext, score4, grade4, resultext4])),
                                ft.Divider(height=1, color="#F1F5F9"),
                                ft.Container(padding=ft.Padding.only(left=12, right=12, top=12, bottom=12), content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[fifthtext, score5, grade5, resultext5])),
                            ]
                        )
                    ),

                    
                   
                ]
            )
        )
    )
    result()
    resultdetail()
    page.update()
