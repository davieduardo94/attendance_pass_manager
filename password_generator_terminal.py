from __future__ import barry_as_FLUFL
from datetime import datetime
from password_manager import PassManager

from user_attendance import UserAttendance


# name = input('Digite o nome do paciente: ')
# attendace = input('Digite o tipo de atendimento: ')
# enterDate = datetime.utcnow()

# while True:
#     name = 'Davi'
#     attendace = 'Consulta'
#     enterDate = datetime.utcnow()

#     registrar = UserAttendance(name, attendace, enterDate)
#     pwd = PassManager(UserAttendance.__name__)
#     print("Senha:" + str(pwd.pass_gen()))
#     print(pwd)


#     print(registrar)
#     t = input('Continuar? 1 - Sim / 2 - Nao')
#     if t == '1':
#         continue
#     else:
#         break

"""
gerenciamento de senhas
Usuario informa o nome e o tipo de atendimento
a senha é chamada
a ultima senha é armazenada
chamada no proximo
"""
password_n = None
password_p = None


# name = input('Nome: ')

init_normal = 0
init_prioridade = 0
last_password_priority = []
last_password_normal = []

while True:
    atendimento = 'Consulta'
    operation = int(input('Gerar senha:\n1 - Senha normal\n2 - Prioridade \
                          \n3 - Mostrar ultimas 5 senhas Normais\n4 - Mostrar ultimas 5 senhas prioritarias\n'))
    if operation == 1:
        if init_normal == 0:
            password_n = init_normal+1
            init_normal += 1
        else:
            last_password_normal.append('N'+str(password_n))
            password_n = init_normal+1
            init_normal += 1
            print(f'Ultima senha chamada: {last_password_normal[-1]}')
        print(f'Sua senha: N{password_n}')
    elif operation == 2:
        if init_prioridade == 0:
            password_p = init_prioridade+1
            init_prioridade += 1
        else:
            last_password_priority.append('P'+str(password_p))
            password_p = init_prioridade+1
            init_prioridade += 1
            print(f'Ultima senha chamada: P{last_password_priority[-1]}')
        print(f'Sua senha: P{password_p}')
    elif operation == 3:
        print(' - '.join(last_password_normal[-6:]))
    elif operation == 4:
        print(' - '.join(last_password_priority[-6:]))
    else:
        break
