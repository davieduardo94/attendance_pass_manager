from password_manager import PasswordManager
from password_priority import PriorityPassword


class PriorityAttendance(PasswordManager):
    def __init__(self, attendance_type):
        self.attendance_type = attendance_type
        
    def create_pwd(self):
        """
        Criando a senha de acordo com o atendimento
        """
        return PriorityPassword(self.attendance_type)