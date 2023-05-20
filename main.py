import tkinter as tk
from tkinter import messagebox
import pymysql

# 连接到数据库
connection = pymysql.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

# 创建游标对象
cursor = connection.cursor()


# 查询函数
def search_records():
    # 获取检索条件
    student_id = student_id_entry.get()
    name = name_entry.get()
    age_from = age_from_entry.get()
    age_to = age_to_entry.get()
    gender = gender_entry.get()
    department = department_entry.get()
    course_name = course_name_entry.get()
    prerequisite_name = prerequisite_name_entry.get()
    credit = credit_entry.get()
    grade = grade_entry.get()

    # 构造查询语句
    query = f"SELECT * FROM student, course, sc WHERE student.student_id = sc.student_id AND course.course_id = sc.course_id"
    conditions = []

    if student_id:
        conditions.append(f"student.student_id = {student_id}")
    if name:
        conditions.append(f"student.name = '{name}'")
    if age_from:
        conditions.append(f"student.age >= {age_from}")
    if age_to:
        conditions.append(f"student.age <= {age_to}")
    if gender:
        conditions.append(f"student.gender = '{gender}'")
    if department:
        conditions.append(f"student.department = '{department}'")
    if course_name:
        conditions.append(f"course.name = '{course_name}'")
    if prerequisite_name:
        conditions.append(f"course.prerequisite = '{prerequisite_name}'")
    if credit:
        conditions.append(f"course.credit = {credit}")
    if grade:
        conditions.append(f"sc.grade = {grade}")

    if conditions:
        query += " AND " + " AND ".join(conditions)

    try:
        # 执行查询
        cursor.execute(query)
        result = cursor.fetchall()

        # 在表格中显示结果
        display_results(result)

    except pymysql.Error as e:
        messagebox.showerror("查询失败", str(e))


# 在表格中显示查询结果
def display_results(result):
    result_text.delete('1.0', tk.END)
    for row in result:
        result_text.insert(tk.END, row)
        result_text.insert(tk.END, "\n")


# 构造用户界面
def create_user_interface():
    root = tk.Tk()
    root.title("学生数据库查询")
    root.geometry("800x600")

    # 学号
    student_id_label = tk.Label(root, text="学号：")
    student_id_label.grid(row=0, column=0)
    student_id_entry = tk.Entry(root)
    student_id_entry.grid(row=0, column=1)

    # 姓名
    name_label = tk.Label(root, text="姓名：")
    name_label.grid(row=1, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=1, column=1)

    # 年龄
    age_label = tk.Label(root, text="年龄：")
    age_label.grid(row=2, column=0)
    age_from_entry = tk.Entry(root, width=5)
    age_from_entry.grid(row=2, column=1)
    age_to_entry = tk.Entry(root, width=5)
    age_to_entry.grid(row=2, column=2)

    # 性别
    gender_label = tk.Label(root, text="性别：")
    gender_label.grid(row=3, column=0)
    gender_entry = tk.Entry(root)
    gender_entry.grid(row=3, column=1)

    # 系名
    department_label = tk.Label(root, text="系名：")
    department_label.grid(row=4, column=0)
    department_entry = tk.Entry(root)
    department_entry.grid(row=4, column=1)

    # 课程名
    course_name_label = tk.Label(root, text="课程名：")
    course_name_label.grid(row=5, column=0)
    course_name_entry = tk.Entry(root)
    course_name_entry.grid(row=5, column=1)

    # 先行课名
    prerequisite_name_label = tk.Label(root, text="先行课名：")
    prerequisite_name_label.grid(row=6, column=0)
    prerequisite_name_entry = tk.Entry(root)
    prerequisite_name_entry.grid(row=6, column=1)

    # 学分
    credit_label = tk.Label(root, text="学分：")
    credit_label.grid(row=7, column=0)
    credit_entry = tk.Entry(root)
    credit_entry.grid(row=7, column=1)

    # 成绩
    grade_label = tk.Label(root, text="成绩：")
    grade_label.grid(row=8, column=0)
    grade_entry = tk.Entry(root)
    grade_entry.grid(row=8, column=1)

    # 查询按钮
    search_button = tk.Button(root, text="查询", command=search_records)
    search_button.grid(row=9, column=0)

    # 查询结果文本框
    result_text = tk.Text(root)
    result_text.grid(row=10, column=0, columnspan=2)

    root.mainloop()


# 主程序
if __name__ == '__main__':
    create_user_interface()

# 关闭数据库连接
connection.close()
