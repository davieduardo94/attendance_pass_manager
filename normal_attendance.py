from password_manager import PasswordManager
from password_normal import NormalPassword


class NormalAttendance(PasswordManager):
    def __init__(self, attendance_type):
        self.attendance_type = attendance_type
        
    def create_pwd(self):
        """
        Criando a senha de acordo com o atendimento
        """
        return NormalPassword(self.attendance_type)