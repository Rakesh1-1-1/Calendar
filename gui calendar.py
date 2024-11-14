import calendar
from tkinter import *

def showCalendar():

    gui = Toplevel()
    gui.config(background='grey')
    gui.title("Calendar of the Year")
    gui.geometry("550x600")


    year = int(year_field.get())


    gui_content = calendar.calendar(year)

    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=0, column=0, padx=20, pady=20)

    gui.mainloop()


if __name__ == '__main__':
    new = Tk()
    new.config(background='black')
    new.title("Calendar")
    new.geometry("800x600")


    cal = Label(new, text="Calendar", fg='white', bg='black', font=("times", 40, "bold"))
    cal.grid(row=0, column=1, pady=20)


    year = Label(new, text="Enter the year", fg='white', bg='black', font=("times", 25))
    year.grid(row=1, column=1, pady=10)


    year_field = Entry(new, font=("times", 20))
    year_field.grid(row=2, column=1, pady=10)


    button = Button(new, text='Show Calendar', fg='white', bg='black', font=("times", 20), command=showCalendar)
    button.grid(row=3, column=1, pady=20)


    exit_button = Button(new, text='Exit', fg='white', bg='black', font=("times", 20), command=new.quit)
    exit_button.grid(row=4, column=1, pady=20)

    new.mainloop()