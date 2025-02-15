import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def encrypt():
    file_path = filedialog.askopenfilename(title="Select Image")
    if not file_path:
        return

    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Invalid Image File")
        return

    msg = simpledialog.askstring("Input", "Enter secret message:")
    if not msg:
        return

    password = simpledialog.askstring("Input", "Set a passcode:", show="*")
    if not password:
        return

    with open("password.txt", "w") as file:
        file.write(password)

    msg += "\0"
    d = {chr(i): i for i in range(256)}

    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    save_path = os.path.join(os.path.dirname(file_path), "encryptedImage.png")
    cv2.imwrite(save_path, img)
    messagebox.showinfo("Success", f"Message encrypted and saved as:\n{save_path}")

root = tk.Tk()
root.title("Image Encryption")
root.geometry("400x200")
root.config(bg="#2C3E50")

title_label = tk.Label(root, text="Image Encryption", font=("Courier New", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
title_label.pack(pady=10)

btn_encrypt = tk.Button(root, text="Encrypt Message", command=encrypt, font=("Courier New", 12, "bold"), bg="#3498DB", fg="#FFFFFF", height=2, width=20)
btn_encrypt.pack(pady=10)

root.mainloop()
