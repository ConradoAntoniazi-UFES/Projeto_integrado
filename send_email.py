import smtplib
from email.message import Message

def get_contacts(filename):
    nomes = []
    emails = []
    with open(filename, mode='r') as contacts_file:
        for contact in contacts_file:
            nomes.append(contact.split()[0])
            emails.append(contact.split()[1])
    return nomes, emails

def send_email(nome, email, cardapio_ru):  
    
    # criação de um objeto email.message.Message() para representar o email a ser enviado:
    msg = Message()

    msg['Subject'] = "CARDÁPIO DO RU" # define o assunto do email
    msg['From'] = 'conradoantoniazi@gmail.com' # define o remetente do email
    msg['To'] = email # define o destinatário do email
    password = 'projetoIntegrado123'

    msg.add_header('Content-Type', 'text/html') # indica que o conteúdo do email está em HTML
    email_content = f"""
    <p><b>===Cardápio RU===</b></p>
    <p>Olá {nome}! Este é o cardápio de hoje:<p>
    <p>{cardapio_ru}</p>
    """    
    msg.set_payload(email_content) # define o conteúdo como sendo o corpo do email a ser enviado

    # faz a conexão com o servidor do gmail:
    s = smtplib.SMTP('smtp.gmail.com: 587')

    # o TLS é um protocolo de segurança que protege a comunicação entre o cliente (seu código Python) 
    # e o servidor SMTP, garantindo que os dados sejam transmitidos de forma criptografada, tornando
    # a conexão mais segura
    s.starttls()

    # tenta fazer o login:
    try:
        s.login(msg['From'], password)
    except:
        print("Problema no envio de email para alerta.")
        return
    
    # caso o login tenha dado certo, envia o email:
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))