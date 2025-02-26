from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox


def solve_equation():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        D = b**2 - 4 * a * c

        if D > 0:
            x1 = round((-b + D**0.5) / (2 * a), 2)
            x2 = round((-b - D**0.5) / (2 * a), 2)
            label_result.config(text=f"D > 0 → два решения:\n x1 = {x1}, x2 = {x2}")
            draw_graph(x1, x2)

        elif D == 0:
            x = round(-b / (2 * a), 2)
            label_result.config(text=f"D = 0 → одно решение:\n x = {x}")
            draw_graph()

        else:
            label_result.config(text="D < 0 → решений нет")

    except:
        messagebox.showerror("Ошибка")


def highlight_empty_fields(event):
    for entry in (entry_a, entry_b, entry_c):
        entry.configure(bg="red" if not entry.get() else "#ffe6f0")


def draw_graph(x1=None, x2=None):
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    x_range = np.linspace(x1 - 2, x2 + 2, 100) if x1 and x2 else np.linspace(-20, 20, 100)
    y = a * x_range**2 + b * x_range + c

    plt.plot(x_range, y, label=f"{a}x² + {b}x + {c}")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()


# Создание окна
root = Tk()
root.geometry("900x400")
root.resizable(False, False)
root.title("Решение квадратного уравнения")
root.configure(bg="white")

# Заголовок
Label(root, text="Решение квадратного уравнения", font=("Arial", 20), bg="white").pack(pady=20)

# Поля ввода и формула
entry_a = Entry(root, font=("Arial", 20), bg="#ffe6f0")
entry_a.place(x=40, y=180, width=100)
entry_a.bind("<KeyRelease>", highlight_empty_fields)

Label(root, font=("Arial", 20), text="x² +", bg="white").place(x=150, y=180)

entry_b = Entry(root, font=("Arial", 20), bg="#ffe6f0")
entry_b.place(x=275, y=180, width=100)
entry_b.bind("<KeyRelease>", highlight_empty_fields)

Label(root, font=("Arial", 20), text="x +", bg="white").place(x=385, y=180)

entry_c = Entry(root, font=("Arial", 20), bg="#ffe6f0")
entry_c.place(x=465, y=180, width=100)
entry_c.bind("<KeyRelease>", highlight_empty_fields)

Label(root, font=("Arial", 20), text="= 0", bg="white").place(x=575, y=180)

# Кнопка решения
Button(root, text="Решить", font=("Arial", 20), command=solve_equation, bg="#ffe6e6").place(x=650, y=140)

# Поле результата
label_result = Label(root, text="Ответ...", bg="#ddccff", compound="center", font=("Arial", 16))
label_result.place(x=120, y=290, width=600, height=90)

root.mainloop()

