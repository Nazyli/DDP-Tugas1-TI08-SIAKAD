def menghitung_grade_indeks(nilai):
    grade = ""
    indeks = 0
    if 85 <= nilai <= 100:
        grade = "A"
        indeks = 4.0
    elif 70 <= nilai < 85:
        grade = "B"
        indeks = 3.0
    elif 55 <= nilai < 70:
        grade = "C"
        indeks = 2.0
    elif 40 <= nilai < 55:
        grade = "D"
        indeks = 1.0
    elif nilai < 40:
        grade = "E"
        indeks = 0.0
    return grade, indeks

print("\n==================================================================")
print("Fitur Input Nilai Mahasiswa")
nim = input("Masukkan NIM : ")
jmlKul = 0
while jmlKul < 1 or jmlKul > 8:
    jmlKul = int(input("Berapa jumlah mata kuliah yang diambil? "))
    if(jmlKul < 1 or jmlKul > 8):
        print("Jumlah mata kuliah harus antara 1-8 \n ")
print("==================================================================")

totalSks = 0
indexPrestasi = 0
for i in range (jmlKul):
    print("\nNilai Mata Kuliah", i+1)
    matkul = input("Nama Mata Kuliah\t: ")
    sks = int(input("Beban SKS mata kuliah\t: "))
    kuis = int(input("Nilai Kuis\t\t: "))
    tugas1 = int(input("Nilai Tugas 1\t\t: "))
    tugas2 = int(input("Nilai Tugas 2\t\t: "))
    uts = int(input("Nilai UTS\t\t: "))
    uas = int(input("Nilai UAS\t\t: "))
    nilai = (0.15 * kuis) + (0.15 * tugas1) + (0.2 * tugas2) + (0.25 * uts) + (0.25 * uas)
    grade, indeks = menghitung_grade_indeks(nilai)
    totalSks += sks
    indexPrestasi += (sks * indeks)
    print("Nilai untuk mata kuliah {0} : {1} (grade {2})".format(matkul,nilai, grade))

print("\n==================================================================")
print("Rangkuman")
print("NIM \t\t\t: ", nim)
print("Total SKS \t\t: ", totalSks)
print("Indeks Prestasi \t: ", indexPrestasi/totalSks)
print("==================================================================")



# Nama : Evry Nazyli Ciptanto
# NIM : 0110220045
# Kelas : Teknik Informatika - TI08