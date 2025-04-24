import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x500")
        self.root.configure(bg="silver")

        # Screen
        self.screen = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
        self.screen.grid(row=0, column=0, columnspan=4, pady=20)

        # Bind keyboard input
        self.root.bind("<Key>", self.on_key_press)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('^', 5, 2)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 15), bg="lightgrey", fg="black",
                               activebackground="darkgrey", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char == "C":
            self.screen.delete(0, tk.END)
        elif char == "=":
            try:
                expression = self.screen.get()
                result = eval(expression.replace("^", "**"))  # Replace ^ with ** for power operation
                self.screen.delete(0, tk.END)
                self.screen.insert(0, str(result))
            except Exception as e:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, "Error")
        else:
            self.screen.insert(tk.END, char)

    def on_key_press(self, event):
        key = event.char
        if key in "0123456789+-*/^":
            self.on_button_click(key)
        elif key == "\r":  # Enter key
            self.on_button_click("=")
        elif key == "\x08":  # Backspace key
            current_text = self.screen.get()
            self.screen.delete(0, tk.END)
            self.screen.insert(0, current_text[:-1])
        elif key.lower() == "c":  # Clear screen with 'C' or 'c'
            self.on_button_click("C")


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
