from locale import currency
from multiprocessing import current_process


class PassManager():

    current_password = 0
    last_password = 0
    def __init__(self, user) -> None:
        # recebendo o usuario para verificar se está preenchido
        self.user = user
    
    def pass_gen(self):
        self.current_password +=1
        self.last_password = self.current_password
        return self.current_password

    def pass_last(self):
        """ returns de last password called """
        return self.last_password

    def __str__(self) -> str:
        return "Current Password: %s \nLast Password: %s" %(self.current_password, self.last_password)