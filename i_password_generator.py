from abc import ABC, abstractclassmethod

# Interface
class PasswordGenerator(ABC):
    """
    Obrigando que as classes tenham este metodo
    """
    @abstractclassmethod
    def generatePwd(self):
        pass
