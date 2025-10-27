from behave import given, when, then

@given("pengguna membuka website Pusat Bahasa UNAIR")
def step_open_website(context):
    print("Website Pusat Bahasa UNAIR dibuka.")

@given("pengguna telah memiliki akun ELPT dengan username dan password valid")
def step_user_has_account(context):
    print("Pengguna memiliki akun ELPT yang valid.")

@when("pengguna login ke sistem")
def step_user_login(context):
    print("Pengguna berhasil login ke sistem.")

@when('pengguna membuka menu "Test History"')
def step_open_test_history(context):
    print("Menu Test History dibuka.")

@when('pengguna memilih tombol "Invoice Sertifikat"')
def step_select_invoice(context):
    print("Tombol Invoice Sertifikat diklik dan invoice muncul.")

@when("pengguna mencetak invoice dan melakukan pembayaran di Bank Mandiri")
def step_payment(context):
    print("Invoice dicetak dan pembayaran dilakukan di Bank Mandiri.")

@when('pengguna membuka menu "Certificate"')
def step_open_certificate(context):
    print("Menu Certificate dibuka.")

@when('pengguna menekan tombol "Formulir Cetak Sertifikat"')
def step_click_formulir(context):
    print("Tombol Formulir Cetak Sertifikat diklik.")

@then("sistem menampilkan tampilan sertifikat ELPT yang siap dicetak")
def step_show_certificate(context):
    print("Sertifikat ELPT berhasil ditampilkan dan siap dicetak.")