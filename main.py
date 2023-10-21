from password_manager import PasswordManager
from priority_attendance import PriorityAttendance
from normal_attendance import NormalAttendance


# funcao generica simulando o client
# implementando o tipo de classe PasswordManager
def client_code(passwodManager: PasswordManager):
    # aceesando o nome da classe
    print(f'App: Carregado com {passwodManager.__class__.__name__}')
    # chamando o metodo de PassworManager
    print(f"{passwodManager.createAttendance()}")

if __name__ == "__main__":
    client_code(NormalAttendance('Normal'))
    print('\n')
    client_code(PriorityAttendance('Priority'))