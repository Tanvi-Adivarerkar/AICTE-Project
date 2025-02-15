import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def decrypt():
    file_path = filedialog.askopenfilename(title="Select Encrypted Image")
    if not file_path:
        return

    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Invalid Image File")
        return

    try:
        with open("password.txt", "r") as file:
            stored_password = file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "Password file not found.")
        return

    pas = simpledialog.askstring("Input", "Enter passcode for decryption:", show="*")
    if pas != stored_password:
        messagebox.showerror("Error", "Incorrect password. Decryption failed.")
        return

    n, m, z = 0, 0, 0
    message = ""
    c = {i: chr(i) for i in range(256)}

    while True:
        pixel_value = img[n, m, z]
        char = c.get(pixel_value, "?")
        if char == "\0":
            break
        message += char
        n += 1
        m += 1
        z = (z + 1) % 3

    messagebox.showinfo("Decryption Successful", f"Decrypted message:\n{message}")

# Create GUI window
root = tk.Tk()
root.title("Image Decryption")
root.geometry("400x200")
root.config(bg="#2C3E50")

# Title Label
title_label = tk.Label(root, text="Image Decryption", font=("Courier New", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
title_label.pack(pady=10)

# Decrypt Button
btn_decrypt = tk.Button(root, text="Decrypt Message", command=decrypt, font=("Courier New", 12, "bold"), bg="#3498DB", fg="#FFFFFF", height=2, width=20)
btn_decrypt.pack(pady=10)

# Run the GUI
root.mainloop()
