from i_password_generator import PasswordGenerator


class PriorityPassword(PasswordGenerator):
    __init = 0
    __password = 0
    __last_password = None
    
    def __init__(self, attendance_type):
        self.attendance_type = attendance_type
        

    def generate_pwd(self):
        if self.__init == 0:
            self.__password = self.__init + 1
            self.__init += 1
        else:
            self.__password = self.__init + 1
            self.__init += 1
        result = "Senha {}: P{}".format(self.attendance_type,self.__password)
        return result