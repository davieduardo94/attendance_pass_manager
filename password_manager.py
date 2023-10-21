from i_password_generator import PasswordGenerator

# Factory Method
class PasswordManager():
    def createPwd(self):
        pass
    
    def createAttendance(self):
        password = self.createPwd()
        return f"Gerando senha\n{password.generatePwd()}"
    