from abc import ABC, abstractclassmethod

# Interface
class PasswordGenerator(ABC):
    @abstractclassmethod
    def generatePwd(self):
        pass
