from behave import given, when, then

@given("Pengguna sudah login dan berada di halaman Home User")
def step_user_logged_in(context):
    print("Pengguna sudah login dan berada di halaman Home User")

@given("Pengguna sudah login dan membuka menu Search Test Schedule")
def step_user_open_search_menu(context):
    print("Pengguna sudah login dan membuka menu Search Test Schedule")

@when('Pengguna mengklik menu "Search Test Schedule"')
def step_click_search_menu(context):
    print('Pengguna mengklik menu "Search Test Schedule"')

@when("Pengguna memilih Type Test dan Date Test")
def step_select_type_and_date(context):
    print("Pengguna memilih Type Test dan Date Test")

@when("Memilih Type Test dan Date Test yang diinginkan")
def step_choose_test_type_date(context):
    print("Memilih Type Test dan Date Test yang diinginkan")

@when("Menekan tombol Search")
def step_click_search(context):
    print("Menekan tombol Search untuk mencari jadwal")

@when("Menekan tombol Search untuk mencari jadwal")
def step_click_search_button(context):
    print("Menekan tombol Search untuk mencari jadwal")

@then("Sistem menampilkan daftar jadwal tes yang tersedia")
def step_show_available_tests(context):
    print("Sistem menampilkan daftar jadwal tes yang tersedia")

@then('Pengguna menekan tombol "Apply Now" pada jadwal yang dipilih')
def step_click_apply_now(context):
    print('Pengguna menekan tombol "Apply Now" pada jadwal yang dipilih')

@then("Sistem menampilkan halaman Payment Confirmation")
def step_show_payment_confirmation(context):
    print("Sistem menampilkan halaman Payment Confirmation")

@then('Pengguna menekan tombol "Continue to payment"')
def step_click_continue_payment(context):
    print('Pengguna menekan tombol "Continue to payment"')

@then("Sistem menampilkan halaman Invoice berisi rincian pembayaran")
def step_show_invoice(context):
    print("Sistem menampilkan halaman Invoice berisi rincian pembayaran")

@then("Sistem menampilkan daftar jadwal yang kuotanya sudah penuh atau tidak tersedia")
def step_show_unavailable_schedule(context):
    print("Sistem menampilkan daftar jadwal yang kuotanya sudah penuh atau tidak tersedia")
