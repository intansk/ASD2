import os

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def fib(l, d, h):
    cari1 = 0
    cari2 = 1
    fib = cari1 + cari2
    while (fib < h):
        cari1 = cari2
        cari2 = fib
        fib = cari1 + cari2
    offset = -1
    while (fib > 1):
        i = min(offset + cari1, h-1)
        if (l[i] < d):
            fib = cari2
            cari2 = cari1
            cari1 = fib - cari2
            offset = i
        elif (l[i] > d):
            fib = cari1
            cari2 = cari2 - cari1
            cari1 = fib - cari2
        else:
            return i
    if (cari2 and l[h-1] == d):
        return h-1
    return -1

def search():
    print(" >> Nama", r, "Berhasil Ditemukan <<")
    for index in range(len(var)):
        if type(var[index]) == list:
            kolom = fib(var[index], r, len(var[index]))
            print("Index: ", index,)
            print("Kolom: ", kolom, "\n") #wahyu wibi 
            return
        else:
            if var[index] == r:
                kolom = fib(var[index], r, len(var[index]))
                print("Index: ", index, "\n") #arsel, avivah, daiva
                return
            
def skip():
    sekip = input("Tekan Enter Untuk Melanjutkan ")

while True:
    r = input("Masukkan nama: ")
    os.system("cls")
    if r == "Arsel":
        search()
        skip()
        os.system("cls")
    elif r == "Avivah":
        search()
        skip()
        os.system("cls")
    elif r == "Daiva":
        search()
        skip()
        os.system("cls")
    elif r == "Wahyu":
        search()
        skip()
        os.system("cls")
    elif r == "Wibi":
        search()
        skip()
        os.system("cls")
    else:
        print("KESALAHAN")
        break