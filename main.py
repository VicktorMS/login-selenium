# main.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import config

def main():
    # Configurações do ChromeDriver
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")  # Executa em modo headless
    # chrome_options.add_argument("--headless")  # Executa em modo headless (sem interface gráfica)
    chrome_options.add_argument("--no-sandbox")  # Recomendado para WSL
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Recomendado para WSL
    chrome_options.add_argument("--disable-gpu")  # Opcional: desabilita a GPU
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    service = Service("/usr/local/bin/chromedriver")
    print("Inicializando o ChromeDriver...")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("ChromeDriver inicializado.")
    # Inicializa a página de login e realiza o login
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL + "/entrar")
    # login_page.open("https://www.google.com")
    login_page.login(config.EMAIL, config.PASSWORD)

    # Verifica se o login foi bem-sucedido
    print("Título da página após login:", driver.title)

    print("End Script")
    # driver.quit()

if __name__ == "__main__":
    main()
