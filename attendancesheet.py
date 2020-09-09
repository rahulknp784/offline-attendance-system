import attendance
from tkinter import *
from pandas import read_excel

# **************   for GUI    ********************* #
root = Tk()
root.geometry('600x400')
command = StringVar()
status = StringVar()
attendance_image = StringVar()
date = StringVar()

df = read_excel('attendance.xlsx')
# **************   for Attendance   ********************* #


def fill_present(names):
    values = ''
    d1 = date.get()
    for i in range(len(list(df['NAME']))):
        if df['NAME'][i].lower() in names:
            values += 'Present '
        else:
            values += 'Absent '
    df[d1] = values.split()


def submit():
    attendance_img = attendance_image.get()
    names = attendance.take_attendance(attendance_img)
    fill_present(names)
    try:
        df.drop(['Unnamed: 0'], axis=1, inplace=True)
    except KeyError:
        pass
    df.to_excel('attendance.xlsx')
    status.set(f'Present Students: {len(names)}')
    print(df)


# **************   for GUI    ********************* #

command.set('Enter command')


def info():
    df2 = read_excel('attendance.xlsx', index_col="NAME")
    if command.get() in list(df['NAME']):
        l1 = list(df2.loc[command.get()])
        status.set(f'Total Present : {l1.count("Present")}, Percentage : {round((l1.count("Present")/(len(l1)-1))*100)} %')
    else:
        status.set('Wrong Name')


root.configure(bg='skyblue')
mainFrame = Frame(root, bg='skyblue')
mainFrame.grid(row=1, column=0)
f1 = Frame(mainFrame, bg='skyblue', )
f1.grid(row=1, column=0)

Label(f1, text='Current Date :', font='Verdana 15', bg='skyblue').grid(row=1, column=0, padx=10)
Entry(f1, borderwidth=2, font='Verdana', bg='gray', fg='white', textvariable=date).grid(row=1, column=1, pady=10)

Label(f1, text='Photo for Attendance :', font='Verdana 15', bg='skyblue').grid(row=2, column=0, padx=10)
Entry(f1, borderwidth=2, font='Verdana ', bg='gray', fg='white', textvariable=attendance_image).grid(row=2, column=1, pady=10)

f2 = Frame(mainFrame, bg='skyblue', )
f2.grid(row=2, column=0)
Button(f2, text='Take Attendance', font='Verdana 10 bold', borderwidth=5, bg='orange', padx=10, command=submit).pack()

f3 = Frame(mainFrame, bg='skyblue')
f3.grid(row=3, column=0, padx=50)
Label(f2, text='StudentInfo', font='Verdana 20 bold', bg='skyblue', pady=20).pack()

Label(f3, text='Command :', font='Verdana 15', bg='skyblue').grid(row=1, column=0, padx=70)
Entry(f3, borderwidth=2, font='Verdana ', bg='gray', fg='white', textvariable=command).grid(row=1, column=1,)

f4 = Frame(mainFrame, bg='skyblue')
f4.grid(row=4, column=0, padx=50)
Button(f4, text='Get Info', font='Verdana 10 bold', borderwidth=5, bg='orange', padx=10, command=info).pack(pady=10)
Entry(f4, borderwidth=2, font='Verdana ', bg='gray', fg='white', width=40, textvariable=status).pack(pady=20)

root.mainloop()
