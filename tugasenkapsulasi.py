class Mahasiswa:
    def __init__(self, nama, umur):
        self.__nama = nama  # Properti private
        self.__umur = umur  # Properti private

    # Getter untuk properti nama
    def get_nama(self):
        return self.__nama

    # Setter untuk properti nama
    def set_nama(self, nama):
        self.__nama = nama

    # Getter untuk properti umur
    def get_umur(self):
        return self.__umur

    # Setter untuk properti umur
    def set_umur(self, umur):
        self.__umur = umur


# Membuat objek baru dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Anwar", 21)

# Mengakses variabel private menggunakan getter
print("Nama:", mahasiswa1.get_nama())
print("Umur:", mahasiswa1.get_umur())

# Mengubah nilai variabel private menggunakan setter
mahasiswa1.set_nama("Andi")
mahasiswa1.set_umur(22)

# Mengakses kembali variabel private yang sudah diubah
print("Nama baru:", mahasiswa1.get_nama())
print("Umur baru:", mahasiswa1.get_umur())
