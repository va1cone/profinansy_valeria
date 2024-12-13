#авторизация
login_page_url = 'https://frontend.test.profinansy.ru/login' #урл авторизации
input_login = "//input[@name = 'email']" #ввод почты на странице авторизации
input_password = "//input[@type='password']"#ввод пароля на странице авторизации
button_submit = "//button[@type = 'submit']" #кнопка войти
home_url = 'https://frontend.test.profinansy.ru/'

#домашняя страница
investment_button_on_home_page = '//span[@class="sc-cwHptR iTgSxi sc-gFAWRd hsCkDl" and text() = "Инвестиции" ]' #кнопка инвестиции на главной странице
portfolios_button_on_home_page = '/html/body/div[1]/div[3]/div[1]/div[2]/div/aside/div/div/div/div[3]/a[1]/div/span' #кнопка портфели на странице инвестиций
