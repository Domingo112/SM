import flet as ft
import register
import email_register
import fullinfo
import staff_dashboard
import login
import search_details
import search_student,add_score,student_panel,student_result,best_student,add_student


def main(page: ft.Page):
    def route_change():
        page.views.clear()
        if page.route == "/":
            login.loginING(page)
        elif page.route == "/email_register":
            email_register.email(page)
        elif page.route == "/fullinfo":
            fullinfo.complete_registration(page)
        elif page.route == "/staff_dashboard":
            staff_dashboard.TeacherDashboard(page)
        elif page.route == "/register":
           register.register(page)
        elif page.route == "/details":
            search_details.ViewStudentDetails(page)
        elif page.route == "/search":
            search_student.ViewStudents(page) 
        elif page.route =="/add_score":
            add_score.ViewAddScores(page)       
        elif page.route =="/student":
            student_panel.StudentDashboard(page)
        elif page.route =="/result":
            student_result.resultmain(page)
        elif page.route =="/best":
            best_student.main(page)
        elif page.route =="/add":
            add_student.AddStudent(page)               
        page.update()

    page.on_route_change = route_change
    route_change()


ft.run(main)
