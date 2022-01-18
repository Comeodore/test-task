class LoginPage:
    def __init__(self):
        self.loginButton = 'com.ajaxsystems:id/login'
        self.loginField = 'com.ajaxsystems:id/login'
        self.passwordField = 'com.ajaxsystems:id/password'
        self.nextButton = 'com.ajaxsystems:id/next'

    def get_login_button_id(self):
        return self.loginButton

    def get_login_field_id(self):
        return self.loginField

    def get_password_field_id(self):
        return self.passwordField

    def get_next_button_id(self):
        return self.nextButton
