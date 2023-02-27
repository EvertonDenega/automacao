import rpa as r
import pyautogui as p


r.init()
r.url('https://github.com/')
p.sleep(2)

login = r.click('/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a')
user = r.text('//*[@id="login_field"]')
r.close()




# texto_email = dolar_hoje + 'hoje' + str(pd.Timestamp('today'))

# de = 'evertonds@gmail.com'
# senha = ''
# para = 'evertonds@gmail.com'

# message = MIMEMultipart()
# message['From']= de 
# message['to'] = para
# message['Subject'] = 'Cotacao do dolar hoje ' #Titulo do e-mail

# message.attach(MIMEText(texto_email, 'plain'))

# session = smtplib.SMTP('smtp.gmail.com', 587)# Usuario do Gmail com porta
# session.starttls()#habilitar seguranca
# session.login(de, senha)
# texto = message.as_string()
# session.sendmail(de, para, texto)
# session.quit()