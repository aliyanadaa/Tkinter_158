import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x650")

# Label judul
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold")
)
judul.pack(pady=15)

# Frame untuk input nilai
frame = tk.Frame(root)
frame.pack(pady=10)

# Membuat 10 input nilai mata pelajaran
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

# Label pilihan jurusan
label_prodi = tk.Label(
    root,
    text="Prediksi Jurusan Anda:"
)
label_prodi.pack(pady=5)

# Dropdown pilihan jurusan
prodi = tk.StringVar()
prodi.set("Teknologi Informasi")

pilihan_prodi = tk.OptionMenu(
    root,
    prodi,
    "Teknologi Informasi"
)
pilihan_prodi.pack()

# Fungsi hasil prediksi
def hasil_prediksi():
    hasil.config(
        text="Hasil Prediksi: Teknologi Informasi"
    )

# Tombol hasil prediksi
tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
tombol.pack(pady=15)

# Label hasil prediksi
hasil = tk.Label(
    root,
    text="Hasil Prediksi:"
)
hasil.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()