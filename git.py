from RPA.Browser.Selenium import Selenium

# iniciar selenium
browser = Selenium()

# entra na pg do github
browser.open_available_browser("https://github.com/login")

# wait para esperar a pg abrir
browser.wait_until_page_contains_element("login_field")

# loginm e senha
browser.input_text("login_field", "evertonds@gmail.com")
browser.input_text("password", "")

# clicar em login
browser.click_button("commit")
browser.
# aguardar o load
#browser.wait_until_page_contains_element("dashboard")

# fechar
#browser.close_browser()
