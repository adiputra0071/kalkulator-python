def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return x / y

def main():
    print("=== Kalkulator Sederhana Python ===")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")

    while True:
        pilihan = input("\nMasukkan pilihan (1/2/3/4/5): ")

        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator ini!")
            break

        if pilihan in ('1', '2', '3', '4'):
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                continue

            if pilihan == '1':
                print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
            elif pilihan == '2':
                print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
            elif pilihan == '3':
                print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
            elif pilihan == '4':
                hasil = bagi(angka1, angka2)
                if isinstance(hasil, str):
                    print(hasil)
                else:
                    print(f"Hasil: {angka1} / {angka2} = {hasil}")
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5.")

if __name__ == "__main__":
    main()