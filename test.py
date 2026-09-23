# def details():
#         print(ide)
#         DB_NAME=os.path.join(os.path.dirname(__file__),"student_management.db") 
#         conn=sqlite3.connect(DB_NAME)
#         conn.row_factory = sqlite3.Row
#         c=conn.cursor()
#         c.execute("select * from users where id = ?",(ide,))
#         items=c.fetchall()
#         result.controls.clear()
        
#         for item in items:
#                 hmm=detail_row(item["fullname"],item["Dept"],item['id'])
#                 result.controls.append(hmm)