from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import pyautogui as p

driver = webdriver.Chrome(ChromeDriverManager().install())

# entrar no google
driver.get("https://www.google.com/")

# aguardar o load
time.sleep(2)

# entar no github
driver.get("https://github.com/")

time.sleep(2)

# Clicar em sign in
sign_in = driver.find_element("xpath", '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a')
sign_in.click()

time.sleep(2)

# colocar usuario e senha para logar.
user = driver.find_element("xpath", '//*[@id="login_field"]')
user.send_keys("evertonds@gmail.com")
senha = driver.find_element("xpath", '//*[@id="password"]')
senha.send_keys("Everton@205")
senha.send_keys(Keys.RETURN)

time.sleep(3)

# entrar em 'new'
repositorio = driver.find_element("xpath", '/html/body/div[1]/div[5]/div/aside/div/loading-context/div/div[1]/div/h2/a')
repositorio.click()

time.sleep(3)

repo_nome = driver.find_element("xpath", '//*[@id="repo-name-suggestion"]/strong')
repo_nome.click()

# Colocando o nome do repositório
# repo_nome = driver.find_element("xpath", '//*[@id="repository_name"]')
# repo_nome.send_keys("robot-rpa")
time.sleep(3)

#incluindo descricao
repo_desc = driver.find_element("xpath", '//*[@id="repository_description"]')
repo_desc.send_keys("testando robozin de login e criacao de repo")
time.sleep(3)

#selecionar add readme
repo_readme = driver.find_element("xpath", '//*[@id="repository_auto_init"]')
repo_readme.click()

criar_repo = driver.find_element("xpath", '//*[@id="new_repository"]/div[5]/button')
criar_repo.click()
time.sleep(5)

# abrir https para clonar
clonar = driver.find_element("xpath", '//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[1]/div[2]/span[1]/get-repo/details/summary')
clonar.click()
time.sleep(5)

#copiar link
#clone_link = driver.find_element("xpath", '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span[1]/get-repo/details/div/div/div[1]/tab-container/div[2]/ul/li[1]/tab-container/div[2]/div/div/clipboard-copy/svg[1]')
clone_link = driver.find_element("xpath", '//*[@id="local-panel"]/ul/li[1]/tab-container/div[2]/div/div/clipboard-copy')
clone_link.click()

# abrindo cmd com pyautogui
p.hotkey('win', 'r', duration=1)
p.sleep(1)
p.typewrite('cmd')
p.sleep(1)
p.hotkey('enter')
p.sleep(1)
p.typewrite('cd Documents')
p.hotkey('enter')
p.sleep(1)
p.typewrite('git clone ')
p.sleep(1)
p.hotkey("ctrl", "v")
p.sleep(1)
p.hotkey('enter')
p.sleep(1)
p.typewrite('code .')
p.sleep(1)
p.hotkey('enter')
time.sleep(5)

# criando arquivo py e digitando comando
p.moveTo(x=551, y=204, duration=1)
p.click(x=551, y=204)
p.typewrite('robo0.py')
p.sleep(2)
p.hotkey('enter')
p.sleep(1)
p.typewrite('print("Hello")')

# git add commit
p.hotkey('win', 'r', duration=1)
p.sleep(1)
p.typewrite('cmd')
p.sleep(1)
p.hotkey('enter')
p.sleep(1)
p.typewrite('cd Documents')
p.hotkey('enter')
p.sleep(1)
p.typewrite('git add .')
p.sleep(1)
p.hotkey('enter')
p.typewrite('git commit -m "commit robo"')
p.hotkey('enter')
p.sleep(1)
p.typewrite('git push')
p.hotkey('enter')

#driver.quit()