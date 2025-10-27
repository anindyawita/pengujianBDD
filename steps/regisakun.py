from behave import given, when, then

@given("Pengguna membuka halaman utama website Pusat Bahasa UNAIR")
def step_open_homepage(context):
    print("Membuka halaman https://elpt.pusatbahasa.unair.ac.id")

@when("Pengguna klik menu SIGN UP")
def step_click_signup(context):
    print("Klik tombol SIGN UP")

@when("Pengguna mengisi Username, Email, Password, Repeat Password, dan Captcha dengan data valid")
def step_fill_valid_form(context):
    print("Mengisi form registrasi dengan data valid")

@when("Pengguna mengisi form dengan data yang tidak lengkap atau salah")
def step_fill_invalid_form(context):
    print("Mengisi form dengan data tidak valid atau ada yang kosong")

@when("Pengguna klik tombol SIGN UP")
def step_click_signup_button(context):
    print("Klik tombol daftar")

@then("Sistem menampilkan notifikasi bahwa email verifikasi telah dikirim")
def step_show_verification_message(context):
    print("Notifikasi email verifikasi muncul")

@then("Pengguna menerima email verifikasi dalam beberapa saat")
def step_receive_verification_email(context):
    print("Email verifikasi diterima oleh pengguna")

@then("Akun belum bisa digunakan untuk memilih jadwal tes sebelum verifikasi email dilakukan")
def step_account_not_active(context):
    print("Akun belum aktif sebelum verifikasi email")

@then("Sistem menampilkan pesan error bahwa data harus diisi dengan benar")
def step_show_error_message(context):
    print("Pesan error data tidak lengkap muncul")
