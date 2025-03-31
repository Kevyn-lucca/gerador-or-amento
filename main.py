import jinja2
import pdfkit
import keyboard
import time

 

def gerar_pdf():

    nome_vendedor = "teste da silva"
    nome_cliente = "cliente da silva"
    item1 = "teste item1"
    item2 = "teste item2"

    context = {'nome_vendedor': nome_vendedor, 'nome_cliente': nome_cliente, 'item1': item1, 'item2': item2}
    
    carrega_template = jinja2.FileSystemLoader('./')

    env_template = jinja2.Environment(loader=carrega_template)

    template = env_template.get_template('template.html')

    output_pdf =  template.render(context)


    config = pdfkit.configuration(wkhtmltopdf='c:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

    pdfkit.from_string(output_pdf, 'orçamento chaveiro.pdf',configuration = config, css='style.css')
    print("PDF gerado")


# DEBUG: GERA O PDF NOVAMENTE COM CTRL+G
keyboard.add_hotkey('ctrl+g',  gerar_pdf)

print("Pressione Ctrl+G para ativar a função de rotação")
print("Pressione ESC para sair")

try:
    while True:
        if keyboard.is_pressed('esc'):
            print("Saindo...")
            break
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa encerrado")
finally:
    keyboard.unhook_all()  