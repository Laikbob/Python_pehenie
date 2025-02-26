from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def solve_equation():
    try:
        highlight_empty_fields()

        a = float(lbl_a.get())
        b = float(lbl_b.get())
        c = float(lbl_c.get())

        D = b**2 - 4 * a * c

        if D > 0:
            x1 = round((-b + D**0.5) / (2 * a), 2)
            x2 = round((-b - D**0.5) / (2 * a), 2)
            label_result.config(text=f"D > 0 → два решения:\n x1 = {x1}, x2 = {x2}")
            draw_graph(a, b, c)

        elif D == 0:
            x = round(-b / (2 * a), 2)
            label_result.config(text=f"D = 0 → одно решение:\n x = {x}")
            draw_graph(a, b, c)

        else:
            label_result.config(text="D < 0 → решений нет")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

def draw_graph(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label=f"{a}x^2+ {b}x + {c}")
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.title('График квадратного уравнения')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def highlight_empty_fields():
    for entry in (lbl_a, lbl_b, lbl_c):
        entry.configure(bg="red" if not entry.get() else "#ffe6f0")

def aken():
    global lbl_a, lbl_b, lbl_c, label_result
    
    aken = Tk()
    aken.geometry("650x300")
    aken.title("Решение квадратного уравнения")
    aken.resizable(False, False)

    f1 = Frame(aken, width=650, height=300)
    f1.pack()

    ldl = Label(f1, text="Решение квадратного уравнения", font="Calibri 26", fg="green", bg="lightblue")
    ldl.grid(row=0, column=0, columnspan=7, pady=10)

    lbl_a = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=5)
    lbl_a.grid(row=1, column=0, padx=5)

    x2 = Label(f1, text="x^2+", font="Calibri 26", fg="green")
    x2.grid(row=1, column=1, padx=5)
    
    lbl_b = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=5)
    lbl_b.grid(row=1, column=2, padx=5)
    
    x = Label(f1, text="x +", font="Calibri 26", fg="green")
    x.grid(row=1, column=3, padx=5)

    lbl_c = Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=5)
    lbl_c.grid(row=1, column=4, padx=5)
    
    y = Label(f1, text="= 0", font="Calibri 26", fg="green")
    y.grid(row=1, column=5, padx=5)

    btn_lahenda = Button(f1, text="Решить", font="Calibri 26", fg="green", command=solve_equation)
    btn_lahenda.grid(row=2, column=0, columnspan=6, pady=20)

    label_result = Label(f1, text="Результат будет здесь", font="Calibri 18", fg="blue")
    label_result.grid(row=3, column=0, columnspan=6, pady=10)

    aken.mainloop()

aken()
