
import os, sqlite3
import flet as ft
def TeacherDashboard(page: ft.Page):
    page.views.append(
        ft.View(route="/staff_dashboard")
    )
    page.clean()
    REGULAR_BLUE = "#0B4DB8"
    page.bgcolor = "#F0F4FF"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0
    page.window.width = 330
    page.window.height = 700

    page.appbar = ft.AppBar(
        bgcolor=REGULAR_BLUE,
        elevation=0,
        title=ft.Text("Teacher Dashboard", color="white", size=16, weight=ft.FontWeight.BOLD),
        leading=ft.IconButton(icon=ft.Icons.MENU, icon_color="white", icon_size=20),
        actions=[
            ft.Container(
                margin=ft.Margin.only(right=12),
                content=ft.CircleAvatar(
                    radius=16,
                    bgcolor="white",
                    content=ft.Icon(ft.Icons.PERSON, color=REGULAR_BLUE, size=20)
                )
            )
        ],
    )
    tostu = ft.Text("0", weight=ft.FontWeight.BOLD, color=REGULAR_BLUE, size=22)
    def totalstudent():
        try:
            DB_NAME = os.path.join(os.path.dirname(__file__), "student_management.db")
            conn = sqlite3.connect(DB_NAME)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute("Select count(id) as id from users")
            totalstu = c.fetchone()
            tostu.value = str(totalstu["id"]) if totalstu else "0"
            conn.close()
        except:
            tostu.value = "0"
    totalstudent()

    def stat_card(icon, title, value_control, color1, color2):
        return ft.Container(
            expand=True,
            height=95,
            bgcolor="white",
            border_radius=16,
            padding=14,
            shadow=ft.BoxShadow(blur_radius=12, color="#10000000", offset=ft.Offset(0, 4)),
            content=ft.Column(
                spacing=8,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(
                                width=36, height=36,
                                bgcolor=color1,
                                border_radius=10,
                                content=ft.Icon(icon, color="white", size=20),
                                alignment=ft.Alignment.CENTER
                            ),
                            ft.Icon(ft.Icons.MORE_HORIZ, size=16, color="#CBD5E1")
                        ]
                    ),
                    ft.Column(
                        spacing=2,
                        controls=[
                            ft.Text(title, size=11, color="#64748B", weight=ft.FontWeight.W_500),
                            value_control
                        ]
                    )
                ]
            )
        )
    def action_card(icon, label, bg_color, on_click_route):
        return ft.Container(
            width=150,
            height=110,
            bgcolor="white",
            border_radius=16,
            ink=True,
            shadow=ft.BoxShadow(blur_radius=10, color="#0E000000", offset=ft.Offset(0, 3)),
            on_click=lambda e: page.navigate(on_click_route),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.Container(
                        width=48, height=48,
                        bgcolor=bg_color,
                        border_radius=14,
                        content=ft.Icon(icon, color="white", size=22),
                        alignment=ft.Alignment.CENTER
                    ),
                    ft.Text(label, size=11, weight=ft.FontWeight.BOLD, color="#1E293B", text_align=ft.TextAlign.CENTER)
                ]
            )
        )
    page.add(
        ft.Container(
            width=330,
            content=ft.Column(
                spacing=0,
                controls=[

                    ft.Container(
                        bgcolor=REGULAR_BLUE,
                        padding=ft.Padding.only(left=18, right=18, top=12, bottom=20),
                        border_radius=ft.BorderRadius.only(bottom_left=20, bottom_right=20),
                        content=ft.Column(
                            spacing=6,
                            controls=[
                                ft.Text("Welcome back 👋", color="#DBEAFE", size=12),
                                ft.Text("Manage your students easily", color="white", size=13, weight=ft.FontWeight.BOLD),
                            ]
                        )
                    ),

                    ft.Container(
                        padding=ft.Padding.only(left=12, right=12, top=16),
                        content=ft.Row(
                            spacing=12,
                            controls=[
                                stat_card(ft.Icons.GROUPS, "Total Students", tostu, REGULAR_BLUE, "#DBEAFE"),
                                stat_card(ft.Icons.EMOJI_EVENTS, "Top Avg", ft.Text("94.2%", weight=ft.FontWeight.BOLD, color="#065F46", size=18), "#10B981", "#D1FAE5"),
                            ]
                        )
                    ),

                    ft.Container(
                        padding=ft.Padding.only(left=16, right=16, top=20, bottom=10),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text("Quick Actions", weight=ft.FontWeight.BOLD, size=14, color="#0F172A"),
                                ft.Text("See all", size=11, color=REGULAR_BLUE, weight=ft.FontWeight.BOLD)
                            ]
                        )
                    ),

                    ft.Container(
                        padding=ft.Padding.only(left=12, right=12),
                        content=ft.Column(
                            spacing=12,
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=12,
                                    controls=[
                                        action_card(ft.Icons.PERSON_ADD, "Add Student", "#2563EB", "/add"),
                                        action_card(ft.Icons.SEARCH, "Search Student", "#7C3AED", "/search"),
                                    ]
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=12,
                                    controls=[
                                        action_card(ft.Icons.EDIT_NOTE, "Add Scores", "#F59E0B", "/add_score"),
                                        action_card(ft.Icons.DELETE_OUTLINE, "Delete Student", "#EF4444", "/search"),
                                    ]
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.START,
                                    spacing=12,
                                    controls=[
                                        ft.Container(
                                            width=150,
                                            height=110,
                                            bgcolor=REGULAR_BLUE,
                                            border_radius=16,
                                            ink=True,
                                            shadow=ft.BoxShadow(blur_radius=10, color="#300B4DB8", offset=ft.Offset(0, 4)),
                                            on_click=lambda e: page.navigate("/best"),
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                spacing=10,
                                                controls=[
                                                    ft.Container(
                                                        width=48, height=48,
                                                        bgcolor="#FFFFFF30",
                                                        border_radius=14,
                                                        content=ft.Icon(ft.Icons.EMOJI_EVENTS, color="white", size=22),
                                                        alignment=ft.Alignment.CENTER
                                                    ),
                                                    ft.Text("Best Performing", size=11, weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER)
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            width=150,
                                            height=110,
                                            bgcolor="white",
                                            border_radius=16,
                                            border=ft.Border.all(1, "#E2E8F0", ),
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                spacing=6,
                                                controls=[
                                                    ft.Icon(ft.Icons.AUTO_GRAPH, color="#94A3B8", size=26),
                                                    ft.Text("Reports", size=11, weight=ft.FontWeight.BOLD, color="#94A3B8"),
                                                    ft.Text("Coming soon", size=9, color="#CBD5E1"),
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ]
                        )
                    ),
                    ft.Container(height=30)
                ]
            )
        )
    )
    page.update()