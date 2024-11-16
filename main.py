import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP ayarları ve e-posta kimlik bilgileri
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'hzgratse@gmail.com'  # Gönderen e-posta adresi
password = 'cardinal1999Hz'  # Uygulama özgü şifre

# Alıcı ve gönderici bilgileri
from_email = 'hzgratse@gmail.com'
to_email = 'sarvar.mamarasulov@gmail.com'  # Alıcı e-posta adresi
subject = 'Python ile E-posta Gönderme Uygulaması'
body = 'Bu bir test e-postasıdır. Python kullanarak e-posta gönderiyorum.'

# MIME nesnesi oluşturma
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

# E-posta içeriği
msg.attach(MIMEText(body, 'plain'))

try:
    # SMTP sunucusuna bağlanma ve oturum açma
    mail = smtplib.SMTP(smtp_server, smtp_port)
    mail.ehlo()
    mail.starttls()
    mail.login(username, password)

    # E-posta gönderme
    mail.sendmail(from_email, to_email, msg.as_string())
    print('E-posta başarıyla gönderildi.')

    # SMTP oturumunu kapatma
    mail.quit()

except Exception as e:
    print(f'E-posta gönderilirken bir hata oluştu: {e}')
