import os,sqlite3,threading
import flet as ft
def StudentDashboard(page: ft.Page):
    page.views.append(
        ft.View(
            route="/student"
        )
    )
    page.window.width=330
    page.window.height=700
    page.bgcolor = "#F0F7FF"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    id=page.session.store.get("id")
    fullname=page.session.store.get("fullname")
    dept=page.session.store.get("dept")
    page.session.store.set("dept",dept)
    page.session.store.set("id",id)
    regno=page.session.store.get("reg_no")
    small=ft.Text(" ",size=27)
    displayname=ft.Text("Null", color="white", size=16, weight="bold")
    displaydep_reg=ft.Text("SS2  •  Roll No: 412", color="#BFDBFE", size=11)
    averge=ft.Text("Result not released", size=16, weight="bold", color="#0F172A")
    progress=ft.ProgressRing(value=10, stroke_width=7, color="#10B981", bgcolor="#DBEAFE", width=90, height=90)
    status=ft.Text("Status", size=11, color="#15803D")
    remark=ft.Text("Nil", size=16, weight="bold", color="grey")
    checkicon=ft.Icon(ft.Icons.CHECK, size=16, color="grey")
#--- bestgraduate variables ---
    baloon=ft.Text("", size=15,weight="bold",text_align=ft.TextAlign.CENTER,color="#daa520")
    text=ft.Text("", size=28, text_align=ft.TextAlign.CENTER),
    
    
        
    def bestgraduate(loon,avh):
        loon.value=f"🌟Top Best with avg {avh}"
        
    def details():
        displayname.value=fullname
        small.value=fullname[0]
        displaydep_reg.value=f"{dept} • Reg no : {regno}"
        page.update()
    def Average():
        print(id)
        DB_NAME = os.path.join(os.path.dirname(__file__), "student_management.db")
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(
        "Select * from score where userid=?",(id,))
        avg=c.fetchall()
        
        
        for av in avg:
            
            listing=list(av)
            total=listing[2:7]
            total=sum(total)/5
            averge.value=total
            print(total)
            if total >= 70.0:
                bestgraduate(baloon,total)
            if total <= 100.0:
                progress.value=total/100 
                progress.color="#15803D"
                remark.value="Passed"
                remark.color="#15803D"
                status.color="#15803D"
                checkicon.color="#15803D"
            elif total <=90.0:
                progress.value=total/100 
                progress.color="#15803D"
                remark.value="Passed"
                remark.color="#15803D"
                status.color="#15803D"
                checkicon.color="#15803D"
            elif total <=80.0:
                progress.value=total/100
                progress.color="#15803D"
                remark.value="Passed"
                remark.color="#15803D"
                status.color="#15803D"
                checkicon.color="#15803D"
            elif total <=70.0:
                progress.value=total/100 
                progress.color="#15803D"
                remark.value="Passed"
                remark.color="#15803D"
                status.color="#15803D"
                checkicon.color="#15803D"
            elif total <=60.0:
                progress.value=total/100
                progress.color="#cba135"
                remark.value="Passed"
                remark.color="#15803D"
                status.color="#15803D"
                checkicon.color="#15803D"
            elif total <=50.0:
                progress.value=total/100
                progress.color="#cba135"
                remark.value="Passed"
                remark.color="#15803D"
                status.color="#15803D"
                checkicon.color="#15803D"
            elif total <=40.0:
                progress.value=total/100
                progress.color="red"
                remark.value="failed"
                remark.color="red"
                status.color="red"
                checkicon.color="red"
                checkicon.icon=ft.icons.Icons.WRONG_LOCATION
            if total == 30.0:
                progress.value=total/100
                progress.color="red"
                remark.value="failed"
                remark.color="red"
                status.color="red"
                checkicon.color="red"
                checkicon.icon=ft.icons.Icons.WRONG_LOCATION
            if total<=20.0:
                progress.value=total/100
                progress.color="red"
                remark.value="failed"
                remark.color="red"
                status.color="red"
                checkicon.color="red"
                checkicon.icon=ft.icons.Icons.WRONG_LOCATION
            if total<=10.0:
                progress.value=total/100
                progress.color="red"
                remark.value="failed"
                remark.color="red"
                status.color="red"
                checkicon.color="red"
                checkicon.icon=ft.icons.Icons.WRONG_LOCATION
            if total<=0.0:
                progress.value=total/100
                
                   
                                        
                        
            
            
            
        
        
        page.update()  
    overall_card = ft.Container(
        bgcolor="white",
        border_radius=16,
        padding=16,
        shadow=ft.BoxShadow(blur_radius=10, color="#1A1565D8", spread_radius=0),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    spacing=8,
                    controls=[
                        ft.Text("Overall Average", size=12, weight="bold", color="black"),
                        ft.Stack(
                            width=90, height=90,
                            controls=[
                                progress,
                                ft.Container(
                                    alignment=ft.Alignment.CENTER,
                                    width=90, height=90,
                                    content=averge
                                )
                            ]
                        )
                    ]
                ),
                ft.Container(
                    bgcolor="#DCFCE7",
                    border_radius=12,
                    padding=ft.Padding.only(left=16, right=16, top=12, bottom=12),
                    content=ft.Row(
                        spacing=10,
                        controls=[
                            ft.Column(spacing=2, controls=[
                                status,
                                remark,
                            ]),
                            ft.Container(
                                bgcolor="#BBF7D0",
                                shape=ft.BoxShape.CIRCLE,
                                padding=6,
                                content=checkicon
                            )
                        ]
                    )
                )
            ]
        )
    )
#--- Single View Results Card ---
    view_results_card = ft.Container(
        bgcolor="#DBEAFE",
        border_radius=20,
        padding=30,
        width=280,
        ink=True,
        on_click=lambda e: page.navigate("/result"),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Container(
                    bgcolor="#BFDBFE",
                    shape=ft.BoxShape.CIRCLE,
                    width=90, height=90,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(ft.Icons.ANALYTICS_ROUNDED, size=45, color="#1565D8")
                ),
                
                ft.Text("View Results", size=16, weight="bold", color="#0F172A")
            ]
        )
    )
    page.add(
        ft.Column(
            spacing=0,
            controls=[
#HEADER
                ft.Container(
                    bgcolor="#0B4DB8",
                    padding=ft.Padding.only(left=16, right=16, top=40, bottom=50),
                    border_radius=ft.BorderRadius.only(bottom_left=20, bottom_right=20),
                    content=ft.Column(
                        spacing=16,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row(spacing=10, controls=[
                                        ft.Icon(ft.Icons.SCHOOL, color="white", size=28),
                                        ft.Column(spacing=0, controls=[
                                            ft.Text("Maglo", color="white", size=14, weight="bold"),
                                            ft.Text("Uni", color="white", size=14, weight="bold"),
                                        ])
                                    ]),
                                    
                                ]
                            ),
                            ft.Row(
                                spacing=14,
                                controls=[
                                    ft.CircleAvatar(radius=32, content=small),
                                    ft.Column(spacing=2, controls=[
                                        ft.Text("Welcome,", color="#BFDBFE", size=12),
                                        displayname,
                                        displaydep_reg,
                                    ])
                                ]
                            )
                        ]
                    )
                ),
#OVERALL CONTAINER - overlap
                ft.Container(
                    margin=ft.Margin.only(left=16, right=16, top=-30),
                    content=overall_card
                ),
                ft.Container(
                    content=baloon,
                    alignment=ft.Alignment.CENTER,
                    
                    padding=ft.Margin.only(top=30)
                    
                    ),
#SINGLE CARD CENTERED
                ft.Container(
                    alignment=ft.Alignment.CENTER,
                    padding=ft.Padding.only(top=40, bottom=40),
                    content=view_results_card
                )
            ]
        )
    )
    details()
    Average()
    page.update()
    