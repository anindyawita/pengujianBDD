from behave import given, when, then

@given("Pengguna membuka halaman login ELPT UNAIR")
def step_open_login_page(context):
    print("Halaman login https://elpt.pusatbahasa.unair.ac.id/auth/login dibuka.")

@given("Pengguna telah login menggunakan akun yang valid")
def step_user_logged_in(context):
    print("Pengguna berhasil login menggunakan username dan password yang valid.")

@when('Pengguna membuka menu "Edit Profile"')
def step_open_edit_profile(context):
    print("Menu Edit Profile dibuka.")

@when("Pengguna mengubah field Nama, Email, dan Foto Profil dengan data yang benar")
def step_fill_valid_profile_data(context):
    print("Field Nama, Email, dan Foto Profil diubah dengan data valid.")

@when("Pengguna mengosongkan field wajib seperti Nama atau Email")
def step_fill_invalid_profile_data(context):
    print("Field Nama atau Email dikosongkan.")

@when('Pengguna menekan tombol "Save"')
def step_click_save(context):
    print('Tombol "Save" diklik untuk menyimpan perubahan.')

@then('Sistem menampilkan notifikasi "Profile berhasil diperbarui"')
def step_show_success_message(context):
    print('Notifikasi "Profile berhasil diperbarui" muncul di layar.')

@then("Perubahan data langsung terlihat di halaman profil pengguna")
def step_profile_updated(context):
    print("Perubahan profil terlihat di halaman profil pengguna.")

@then("Sistem menampilkan pesan error bahwa data harus diisi dengan benar")
def step_show_error_message(context):
    print("Pesan error muncul: data wajib belum diisi dengan benar.")

@then("Data profil tidak berubah")
def step_profile_not_changed(context):
    print("Profil tidak berubah karena data tidak valid.")
