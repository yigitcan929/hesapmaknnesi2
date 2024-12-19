import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        # Pencere başlığı ve boyutlandırma
        root.title("Hesap Makinesi")
        width = 500
        height = 450
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Giriş kutuları (rakam1, rakam2 ve sonuç)
        self.textBoxYazilanlar1 = tk.StringVar()
        self.textBoxYazilanlar2 = tk.StringVar()
        self.textBoxYazilanlar3 = tk.StringVar()

        # Giriş kutuları
        self.entry1 = tk.Entry(root, textvariable=self.textBoxYazilanlar1)
        self.entry1["borderwidth"] = "1px"
        self.entry1["font"] = tkFont.Font(family='Times', size=12)
        self.entry1["fg"] = "#333333"
        self.entry1["justify"] = "center"
        self.entry1.place(x=70, y=50, width=70, height=25)

        self.entry2 = tk.Entry(root, textvariable=self.textBoxYazilanlar2)
        self.entry2["borderwidth"] = "1px"
        self.entry2["font"] = tkFont.Font(family='Times', size=12)
        self.entry2["fg"] = "#333333"
        self.entry2["justify"] = "center"
        self.entry2.place(x=200, y=50, width=70, height=25)

        self.entry_result = tk.Entry(root, textvariable=self.textBoxYazilanlar3)
        self.entry_result["borderwidth"] = "1px"
        self.entry_result["font"] = tkFont.Font(family='Times', size=12)
        self.entry_result["fg"] = "#333333"
        self.entry_result["justify"] = "center"
        self.entry_result.place(x=130, y=120, width=70, height=25)

        # Etiketler
        label1 = tk.Label(root, text="Rakam 1")
        label1["font"] = tkFont.Font(family='Times', size=12)
        label1["fg"] = "#333333"
        label1.place(x=70, y=20, width=70, height=25)

        label2 = tk.Label(root, text="Rakam 2")
        label2["font"] = tkFont.Font(family='Times', size=12)
        label2["fg"] = "#333333"
        label2.place(x=200, y=20, width=70, height=25)

        label_result = tk.Label(root, text="Sonuç")
        label_result["font"] = tkFont.Font(family='Times', size=12)
        label_result["fg"] = "#333333"
        label_result.place(x=130, y=90, width=70, height=25)

        # İşlem butonları
        button_add = tk.Button(root, text="+", width=10, height=2, command=self.add)
        button_add.place(x=50, y=200)

        button_subtract = tk.Button(root, text="-", width=10, height=2, command=self.subtract)
        button_subtract.place(x=150, y=200)

        button_multiply = tk.Button(root, text="*", width=10, height=2, command=self.multiply)
        button_multiply.place(x=250, y=200)

        button_divide = tk.Button(root, text="/", width=10, height=2, command=self.divide)
        button_divide.place(x=350, y=200)

    # Matematiksel işlemler
    def add(self):
        try:
            num1 = float(self.textBoxYazilanlar1.get())
            num2 = float(self.textBoxYazilanlar2.get())
            result = num1 + num2
            self.textBoxYazilanlar3.set(result)
        except ValueError:
            self.textBoxYazilanlar3.set("Hata")

    def subtract(self):
        try:
            num1 = float(self.textBoxYazilanlar1.get())
            num2 = float(self.textBoxYazilanlar2.get())
            result = num1 - num2
            self.textBoxYazilanlar3.set(result)
        except ValueError:
            self.textBoxYazilanlar3.set("Hata")

    def multiply(self):
        try:
            num1 = float(self.textBoxYazilanlar1.get())
            num2 = float(self.textBoxYazilanlar2.get())
            result = num1 * num2
            self.textBoxYazilanlar3.set(result)
        except ValueError:
            self.textBoxYazilanlar3.set("Hata")

    def divide(self):
        try:
            num1 = float(self.textBoxYazilanlar1.get())
            num2 = float(self.textBoxYazilanlar2.get())
            if num2 == 0:
                self.textBoxYazilanlar3.set("Bölme Hatası")
            else:
                result = num1 / num2
                self.textBoxYazilanlar3.set(result)
        except ValueError:
            self.textBoxYazilanlar3.set("Hata")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
