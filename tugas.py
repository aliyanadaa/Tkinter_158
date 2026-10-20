import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x650")

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold")
)
judul.pack(pady=15)

frame = tk.Frame(root)
frame.pack(pady=10)

