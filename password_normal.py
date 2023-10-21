from i_password_generator import PasswordGenerator

# Implementando a interface PasswordGenerator
class NormalPassword(PasswordGenerator):
    __init = 0
    __password = 0
    __last_password = 0
    
    def __init__(self, attendance_type):
        self.attendance_type = attendance_type
        

    def generatePwd(self):
        if self.__init == 0:
            self.__password = self.__init + 1
            self.__init += 1
        else:
            self.__password = self.__init + 1
            self.__init += 1
        result = "Senha &: \nN%".format(self.attendance_type,self.__password)
        return result