#Web_Crawler.py
#License: None; Public Domain
#Developed by DEK
#Contato: wafw00f@outlook.com
#LINK TRACKER
import re

import requests
from bs4 import BeautifulSoup

TO_CRAWL = []
CRAWLED = set()
EMAILS = []


while True:
    def menu():
        print()
        print(">>>> Olá! Bem-Vindo à ferramenta Web Crawler LINK TRACKER!")
        print("----------------------------------------------------------")
        print("Opções:")
        print("1 - Fazer o Crawling em uma URL")
        print("2 - Exibir minha lista CRAWLED")
        print("3 - Exibir minha lista EMAILS")
        print("4 - Acessar Manual e Menu Info")
        print("0 - Sair")
        print("----------------------------------------------------------")
        print()



    def get_links(html):
        links = []
        try:
            soup = BeautifulSoup(html, "html.parser")
            tags_a = soup.find_all("a", href="True")
            for tag in tags_a:
                link = tag["href"]
                if link.startswith("http"):
                    links.append(link)

            return links
        except Exception as error:
            print(error)

    def crawl():
        while True:
            if TO_CRAWL:
                url = TO_CRAWL.pop()
                response = requests.get(url, headers=header)
                html = response.text
                links = get_links(html)
                if links:
                    for link in links:
                        if link not in CRAWLED and link not in TO_CRAWL:
                            TO_CRAWL.append(link)
                CRAWLED.add(url)
                print("Crawling {}".format(url))
                
                emails = get_emails(html)
                for email in emails:
                    if email not in EMAILS:
                        print(email)
                        EMAILS.append(email)
            else:
                print("Done")
                break
                
    def get_emails(html):
        emails = re.findall(r"\w[\w\,]+\w@\w[\w\.]+\w", html)
        return emails


    if __name__ == "__main__":
        menu()
        opcao = input("Escolha o que você pretende fazer.")
        if opcao == "1":
            url = input("Digite a URL no protocolo HTTP/HTTPS")
            usr = input("Digite o User-Agent")
            header = {"User-Agent": usr}
            if url and usr:
                if url.startswith("http") and len(usr) > 10:
                    TO_CRAWL.append(url)
                    crawl()
                elif len(url) < 10 or len(usr) < 10:
                    print("ERRO: Formato de URL e/ou User-Agent inválido!")
                    print("ERRO: O tamanho da URL e/ou do User-Agent é muito pequeno!")
                elif not usr:
                    print("ERRO: Insira um User-Agent!")
                else:
                    print("ERRO: Formato de URL inválido!")
                    print("ERRO: A URL precisa iniciar com http!")
            else:
                print("ERRO: Alguma coisa está errada!")
            
            
        elif opcao == "2":
            if CRAWLED:
                for item in CRAWLED:
                    print(item)
            else:
                print("A lista está vazia.")
                
        elif opcao == "3":
            if EMAILS:
                print("Lista de E-Mails:")
                for email in EMAILS:
                    print("    + {}".format(email))
            else:
                print("A lista está vazia.")
                
        elif opcao == "4":
            print()
            print("Obrigado por utilizar web_crawler.py!")
            print("License: None; Public Domain. Developed by DEK.")
            print()
            print("Para utilizá-la, basta passarmos a URL a qual desejamos fazer o Web Crawler, e o User-Agent.")
            print("Exemplo: http://exemplo.com, Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0")
            print()
            print("Além de nos trazer os links de uma URL, \nesta ferramenta nos traz todos os endereços de e-mail presentes em uma página web, por exemplo.")
            print("Recomenda-se rodá-la em uma IDE, como por exemplo VS Code, PyCharm ou Jupyter.")
            print("Contato: wafw00f@outlook.com")
            
        elif opcao == "0":
            break
            
        else:
            print("Digite uma opção válida!")
