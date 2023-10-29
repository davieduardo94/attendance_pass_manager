from i_password_generator import PasswordGenerator

# Factory Method
class PasswordManager():
    def create_pwd(self):
        pass
    
    def create_attendance(self):
        password = self.create_pwd()
        return f"Gerando senha\n{password.generate_pwd()}"
    