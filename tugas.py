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

for i in range(10):
    label = tk.Label(
        frame,
        text=f"Nilai Mata Pelajaran {i + 1}",
        width=25,
        anchor="w"
    )
    label.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(frame, width=20)
    entry.grid(row=i, column=1, padx=5, pady=5)

label_prodi = tk.Label(
    root,
    text="Prediksi Jurusan Anda:"
)
label_prodi.pack(pady=5)

