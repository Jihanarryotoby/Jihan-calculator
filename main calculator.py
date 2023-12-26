# step1 
print('---Kalkulator Sederhana---')
print('---Jihan arryo tobby---')
print('')
# step 2 
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:    # disinikita menggunakan if untuk nilai yang benar
        return x / y 
    else: # dan disini menggunakan else untuk nilai yang salah 
        return "Error: Pembagian oleh nol tidak diizinkan."
# step 3
def kalkulator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan nomor operasi (1/2/3/4): ")

    if pilihan not in ('1', '2', '3', '4'):
        print("Pilihan tidak valid.")
        return
# step 3
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
# step 4
    if pilihan == '1':
        print(angka1, "+", angka2, "=", tambah(angka1, angka2))
    elif pilihan == '2':
        print(angka1, "-", angka2, "=", kurang(angka1, angka2))
    elif pilihan == '3':
        print(angka1, "*", angka2, "=", kali(angka1, angka2))
    elif pilihan == '4':
        print(angka1, "/", angka2, "=", bagi(angka1, angka2))
# step 5
if __name__ == "__main__":
    kalkulator()
