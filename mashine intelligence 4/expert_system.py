import tkinter as tk
from tkinter import messagebox



rules = [
    (["не вмикається", "немає шуму"], "Проблема з блоком живлення"),
    (["не вмикається", "є шум"], "Можлива проблема з материнською платою"),
    (["є шум", "немає зображення"], "Можлива несправність відеокарти"),
    (["перегрівається"], "Потрібно почистити систему охолодження"),
    (["повільна робота"], "Можлива нестача оперативної пам’яті"),
]




def inference(facts):
    results = []

    for conditions, conclusion in rules:
        if all(cond in facts for cond in conditions):
            results.append(conclusion)

    return results




class ExpertSystemGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Експертна система діагностики ПК")

        tk.Label(root, text="Оберіть симптоми:", font=("Arial", 14)).pack(pady=10)

        self.symptoms = {
            "не вмикається": tk.IntVar(),
            "є шум": tk.IntVar(),
            "немає шуму": tk.IntVar(),
            "немає зображення": tk.IntVar(),
            "перегрівається": tk.IntVar(),
            "повільна робота": tk.IntVar()
        }

        for text, var in self.symptoms.items():
            tk.Checkbutton(root, text=text, variable=var).pack(anchor="w")

        tk.Button(root, text="Діагностувати", command=self.diagnose,
                  bg="green", fg="white", font=("Arial", 12)).pack(pady=15)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack()

    def diagnose(self):
        selected_facts = [name for name, var in self.symptoms.items() if var.get() == 1]

        if not selected_facts:
            messagebox.showwarning("Увага", "Оберіть хоча б один симптом")
            return

        results = inference(selected_facts)

        if results:
            self.result_label.config(text="\n".join(results))
        else:
            self.result_label.config(text="Немає діагнозу. Недостатньо даних.")




if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemGUI(root)
    root.mainloop()
