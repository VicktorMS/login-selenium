from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage): 
    """Encapsula as ações específicas para o login. Isso inclui localizar campos de e-mail, senha e botão de login."""
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


    def login(self, email, password):
        self.enter_text(*self.EMAIL_FIELD, email)
        self.enter_text(*self.PASSWORD_FIELD, password)
        self.click(*self.LOGIN_BUTTON)
