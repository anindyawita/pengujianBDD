Feature: Cetak Sertifikat ELPT
  Sebagai peserta ELPT
  Saya ingin dapat mencetak sertifikat setelah melakukan pembayaran
  Agar saya bisa mendapatkan bukti resmi hasil ujian ELPT

  Background:
    Given pengguna membuka website Pusat Bahasa UNAIR
    And pengguna telah memiliki akun ELPT dengan username dan password valid

  Scenario: Pengguna berhasil mencetak sertifikat ELPT
    When pengguna login ke sistem
    And pengguna membuka menu "Test History"
    And pengguna memilih tombol "Invoice Sertifikat"
    And pengguna mencetak invoice dan melakukan pembayaran di Bank Mandiri
    And pengguna membuka menu "Certificate"
    And pengguna menekan tombol "Formulir Cetak Sertifikat"
    Then sistem menampilkan tampilan sertifikat ELPT yang siap dicetak