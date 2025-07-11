import tkinter as tk
from tkinter import messagebox

def get_bmi_classification(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal (Healthy) Weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    elif 30.0 <= bmi <= 34.9:
        return "Obese (Class I)"
    elif 35.0 <= bmi <= 39.9:
        return "Obese (Class II)"
    else:
        return "Obese (Class III - Severe/Morbid Obesity)"

def calculate_bmi():
    weight = weight_entry.get()
    height = height_entry.get()

    if weight == "" or height == "":
        messagebox.showerror("Invalid input", "Please enter weight and height")
        return

    if weight.isalpha() or height.isalpha():
        messagebox.showerror("Invalid input", "Only numbers are allowed")
        return

    weight = float(weight)
    height_cm = float(height)

    if weight <= 0 or height_cm <= 0:
        messagebox.showerror("Invalid input", "Values must be positive numbers")
        return

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    result_var.set(f"Your BMI is: {bmi:.2f}")

    classification = get_bmi_classification(bmi)
    classification_var.set(f"Classification: {classification}")
    classification_label.pack()  

root = tk.Tk()
root.title("Simple BMI Calculator")
root.geometry("400x350")
root.configure(bg="white")

tk.Label(root, text="Weight (kg):", font=("Arial", 12), bg="white").pack(pady=(10, 2))
weight_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=20, bg="#e0f7fa")
weight_entry.pack(pady=5)

tk.Label(root, text="Height (cm):", font=("Arial", 12), bg="white").pack(pady=(10, 2))
height_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=20, bg="#e0f7fa")
height_entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
calc_button.pack(pady=15)

result_var = tk.StringVar()
result_var.set("Your BMI is: ___")

classification_var = tk.StringVar()
classification_var.set("")

result_frame = tk.LabelFrame(root, text="Result", font=("Arial", 12, "bold"), bg="white", fg="black", padx=10, pady=10)
result_frame.pack(pady=10, fill="x", padx=20)

result_label = tk.Label(result_frame, textvariable=result_var, font=("Arial", 16, "bold"), bg="white", fg="#333", width=25, pady=10)
result_label.pack()

classification_label = tk.Label(result_frame, textvariable=classification_var, font=("Arial", 14), bg="white", fg="#555")
root.mainloop()
