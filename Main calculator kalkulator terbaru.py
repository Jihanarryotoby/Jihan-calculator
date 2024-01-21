# step1 
print('---Kalkulator Sederhana---')
print('---Jihan arryo tobby---')
print('')
# step 2 
def tambah(x, y): #Ini adalah deklarasi fungsi yang dimulai dengan kata kunci 
    return x + y #(return yang mengembalikan hasil penjumlahan dari x dan y. Setelah fungsi dipanggil dengan.
            # memberikan nilai untuk x dan y, hasil penjumlahan akan dikembalikan sebagai output dari fungsi)
def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:    
#Ini adalah kondisi yang memeriksa apakah nilai y tidak sama dengan nol. Ini dilakukan untuk memastikan bahwa kita tidak mencoba 
        #untuk melakukan pembagian oleh nol, yang akan menyebabkan kesalahan (error) dalam matematika.
        return x / y 
    else: 
        return "Error: Pembagian oleh nol tidak diizinkan."
#Jika nilai y sama dengan nol, maka fungsi akan mengembalikan pesan kesalahan yang mengindikasikan bahwa pembagian oleh nol tidak diizinkan.
# step 3
def kalkulator():
    print("Pilih operasi:") #(print Ini mencetak pesan ke layar untuk memberi tahu pengguna bahwa mereka 
    print("1. Penjumlahan") #harus memilih operasi)
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan nomor operasi (1/2/3/4): ")#(input meminta pengguna untuk memasukkan nomor 
# operasi yang diinginkan melalui input keyboard. Input ini disimpan dalam variabel pilihan)
    if pilihan not in ('1', '2', '3', '4'):
        print("Pilihan tidak valid.")
        return #(Jika input tidak sama dengan salah satu dari empat nomor operasi yang valid, pesan 
# "Pilihan tidak valid." akan dicetak dan fungsi akan diakhiri dengan return,)
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
#Ini mengambil input dari pengguna untuk dua angka pertama dan kedua, dan mengonversinya menjadi tipe data float
#float(input()) digunakan agar pengguna dapat memasukkan angka desimal.
# step 4
    if pilihan == '1':
##Ini adalah struktur pengkondisian yang mengevaluasi pilihan operasi yang telah dimasukkan oleh pengguna (pilihan). Bergantung 
#pada operasi yang dipilih, program akan memanggil fungsi yang sesuai (tambah, kurang, kali, atau bagi) untuk melaksanakan operasi tersebut.
        print(angka1, "+", angka2, "=", tambah(angka1, angka2))
    elif pilihan == '2':
        print(angka1, "-", angka2, "=", kurang(angka1, angka2))
#Ini mencetak hasil penjumlahan angka1 dan angka2 jika pengguna memilih operasi perkurangan.
    elif pilihan == '3':
        print(angka1, "*", angka2, "=", kali(angka1, angka2))
    elif pilihan == '4':
        print(angka1, "/", angka2, "=", bagi(angka1, angka2))
# step 5
if __name__ == "__main__":
#Ini adalah cara yang umum digunakan untuk menentukan apakah skrip Python dijalankan secara langsung atau diimpor 
#sebagai modul ke skrip lain. Jika skrip dijalankan langsung, maka blok kode di dalamnya akan dijalankan.
    kalkulator()
