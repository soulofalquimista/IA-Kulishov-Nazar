import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Експертні системи")
root.geometry("400x250")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Медична")

def diagnose():
    s = entry1.get().lower()
    if "кашель" in s and "температура" in s:
        result1.config(text="Можливий діагноз: ГРВІ або грип")
    elif "голова" in s:
        result1.config(text="Можливий діагноз: мігрень")
    else:
        result1.config(text="Недостатньо даних")

tk.Label(tab1, text="Введіть симптоми:").pack(pady=5)
entry1 = tk.Entry(tab1, width=40)
entry1.pack()

tk.Button(tab1, text="Діагноз", command=diagnose).pack(pady=5)
result1 = tk.Label(tab1, text="")
result1.pack()


tab2 = tk.Frame(notebook)
notebook.add(tab2, text="Фінанси")

def advise():
    risk = entry2.get().lower()
    if "низький" in risk:
        result2.config(text="Рекомендація: облігації, депозити")
    elif "середній" in risk:
        result2.config(text="Рекомендація: ETF, фонди")
    elif "високий" in risk:
        result2.config(text="Рекомендація: акції росту, крипто")
    else:
        result2.config(text="Вкажіть рівень ризику")

tk.Label(tab2, text="Рівень ризику:").pack(pady=5)
entry2 = tk.Entry(tab2)
entry2.pack()

tk.Button(tab2, text="Отримати пораду", command=advise).pack(pady=5)
result2 = tk.Label(tab2)
result2.pack()


tab3 = tk.Frame(notebook)
notebook.add(tab3, text="Техніка")

def recommend():
    req = entry3.get().lower()
    if "ігри" in req:
        result3.config(text="Рекомендація: ПК з потужною відеокартою")
    elif "навчання" in req:
        result3.config(text="Рекомендація: ноутбук середнього класу")
    elif "офіс" in req:
        result3.config(text="Рекомендація: бюджетний ноутбук")
    else:
        result3.config(text="Уточніть вимоги")

tk.Label(tab3, text="Ваші вимоги:").pack(pady=5)
entry3 = tk.Entry(tab3, width=40)
entry3.pack()

tk.Button(tab3, text="Підібрати", command=recommend).pack(pady=5)
result3 = tk.Label(tab3)
result3.pack()


root.mainloop()
