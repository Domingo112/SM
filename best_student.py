
import sqlite3, flet as ft, os
def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/best"
        )
    )
    page.window.width = 330
    page.window.height = 700
    page.bgcolor = "#F0F7FF"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    REGULAR_BLUE = "#0B4DB8"
    listing = ft.Column(spacing=0)
    def show(fullname, reg_no, total_score, average):

        try:
            avg_val = float(average) if average else 0
        except:
            avg_val = 0
        if avg_val >= 90:
            badge_bg = "#FEF3C7"
            badge_color = "#92400E"
            rank_icon = "🥇"
        elif avg_val >= 80:
            badge_bg = "#D1FAE5"
            badge_color = "#065F46"
            rank_icon = "⭐"
        else:
            badge_bg = "#DBEAFE"
            badge_color = "#1E40AF"
            rank_icon = ""
        return ft.Container(
            bgcolor="white",
            border_radius=12,
            padding=12,
            margin=ft.Margin.only(left=12, right=12, top=8),
            shadow=ft.BoxShadow(blur_radius=6, color="#15000000", offset=ft.Offset(0, 2)),
            content=ft.Row(
                spacing=12,
                controls=[
                    ft.CircleAvatar(
                        radius=22,
                        bgcolor="#DBEAFE",
                        content=ft.Text(fullname[0].upper(), color=REGULAR_BLUE, weight="bold", size=14)
                    ),
                    ft.Column(
                        expand=True,
                        spacing=3,
                        controls=[
                            ft.Text(fullname, size=13, weight="bold", color="#0F172A", max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                            ft.Text(f"Reg No: {reg_no}", size=11, color="#64748B"),
                            ft.Row(
                                spacing=6,
                                controls=[
                                    ft.Container(
                                        bgcolor=badge_bg,
                                        border_radius=20,
                                        padding=ft.Padding.only(left=8, right=8, top=3, bottom=3),
                                        content=ft.Text(f"{rank_icon} {avg_val:.1f}%", size=10, weight="bold", color=badge_color)
                                    ),
                                    ft.Text(f"Total: {total_score}", size=10, color="#475569")
                                ]
                            )
                        ]
                    ),
                    ft.Icon(ft.Icons.CHEVRON_RIGHT, size=16, color="#CBD5E1")
                ]
            )
        )
    def besting():
        DB_NAME = os.path.join(os.path.dirname(__file__), "student_management.db")
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        try:

            c.execute("""
                SELECT u.fullname, u.reg_no, s.*
                FROM users u
                INNER JOIN score s ON u.id = s.userid
            """)
            students = c.fetchall()
            listing.controls.clear()
            if not students:
                listing.controls.append(
                    ft.Container(
                        padding=50,
                        alignment=ft.Alignment.CENTER,
                        content=ft.Text("No students found", color="#64748B")
                    )
                )
            else:
                for stu in students:
                    totalscore=stu['score1']+stu['score2']+stu['score3']+stu['score4']+stu['score5']
                    avg=totalscore/5
                    hmm = show(
                        stu['fullname'],
                        stu['reg_no'],
                        totalscore,
                        avg
                    )
                    listing.controls.append(hmm)
        except Exception as e:
            listing.controls.append(ft.Text(f"Error: {e}", color="red"))
        finally:
            conn.close()
        page.update()
    page.add(
        ft.Container(
            width=page.window.width,
            content=ft.Column(
                spacing=0,
                controls=[

                    ft.Container(
                        content=ft.Row(
                            spacing=10,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", icon_size=20,on_click=lambda e:page.navigate("/staff_dashboard")),
                                ft.Text("Best Performing Students", color="white", size=14, weight="bold"),
                                ft.Container(expand=True),
                                ft.Icon(ft.Icons.EMOJI_EVENTS, color="#FBBF24", size=20)
                            ]
                        ),
                        height=75,
                        width=page.window.width,
                        bgcolor=REGULAR_BLUE,
                        padding=ft.Padding.only(left=6, right=12, top=25, bottom=8),
                        border_radius=ft.BorderRadius.only(bottom_left=12, bottom_right=12)
                    ),
                    ft.Container(height=8),
                    ft.Container(
                        padding=ft.Padding.only(left=14, right=14, top=6, bottom=4),
                        content=ft.Text(f"Top Students - Sorted by Average", size=12, weight="bold", color="#334155")
                    ),
                    listing
                ]
            )
        )
    )
    besting()
