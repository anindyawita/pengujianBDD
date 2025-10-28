Feature: Pemilihan Jadwal Tes ELPT
  Sebagai peserta tes
  Saya ingin dapat mencetak sertifikat setelah melakukan pembayaran
  Agar saya bisa mendapatkan bukti resmi hasil ujian ELPT

  Background:
    Given Pengguna sudah login dan berada di halaman Home User

  Scenario: Pemilihan jadwal tes berhasil
    When Pengguna mengklik menu "Search Test Schedule"
    And Memilih Type Test dan Date Test yang diinginkan
    And Menekan tombol Search
    Then Sistem menampilkan daftar jadwal tes yang tersedia
    And Pengguna menekan tombol "Apply Now" pada jadwal yang dipilih
    Then Sistem menampilkan halaman Payment Confirmation
    And Pengguna menekan tombol "Continue to payment"
    Then Sistem menampilkan halaman Invoice berisi rincian pembayaran

  Scenario: Pemilihan jadwal tes gagal karena kuota penuh atau tidak tersedia
    When Pengguna memilih Type Test dan Date Test
    And Menekan tombol Search untuk mencari jadwal
    Then Sistem menampilkan daftar jadwal yang kuotanya sudah penuh atau tidak tersedia
