Feature: Edit Profile Pengguna ELPT UNAIR
  Sebagai pengguna ELPT
  Saya ingin dapat mengedit data profil saya
  Agar informasi akun saya tetap akurat dan terbaru

  Background:
    Given Pengguna membuka halaman login ELPT UNAIR
    And Pengguna telah login menggunakan akun yang valid

  Scenario: Pengguna berhasil memperbarui profil dengan data valid
    When Pengguna membuka menu "Edit Profile"
    And Pengguna mengubah field Nama, Email, dan Foto Profil dengan data yang benar
    And Pengguna menekan tombol "Save"
    Then Sistem menampilkan notifikasi "Profile berhasil diperbarui"
    And Perubahan data langsung terlihat di halaman profil pengguna

  Scenario: Pengguna gagal memperbarui profil karena data tidak valid
    When Pengguna membuka menu "Edit Profile"
    And Pengguna mengosongkan field wajib seperti Nama atau Email
    And Pengguna menekan tombol "Save Profile"
    Then Sistem menampilkan pesan error bahwa data harus diisi dengan benar
    And Data profil tidak berubah
