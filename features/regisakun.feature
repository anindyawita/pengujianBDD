Feature: Registrasi akun pendaftaran pengguna
  Sebagai calon peserta tes
  Saya ingin membuat akun di sistem ELPT UNAIR
  Agar saya bisa login dan melanjutkan pendaftaran tes

  Background:
    Given Pengguna membuka halaman utama website Pusat Bahasa UNAIR

  Scenario: Registrasi akun berhasil untuk peserta umum atau alumni
    When Pengguna klik menu SIGN UP
    And Pengguna mengisi Username, Email, Password, Repeat Password, dan Captcha dengan data valid
    And Pengguna klik tombol SIGN UP
    Then Sistem menampilkan notifikasi bahwa email verifikasi telah dikirim
    And Pengguna menerima email verifikasi dalam beberapa saat
    And Akun belum bisa digunakan untuk memilih jadwal tes sebelum verifikasi email dilakukan

  Scenario: Registrasi gagal karena data tidak lengkap atau tidak valid
    When Pengguna klik menu SIGN UP
    And Pengguna mengisi form dengan data yang tidak lengkap atau salah
    And Pengguna klik tombol SIGN UP
    Then Sistem menampilkan pesan error bahwa data harus diisi dengan benar
