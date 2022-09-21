from datetime import datetime

from user_attendance import UserAttendance


name = input('Digite o nome do paciente: ')
attendace = input('Digite o tipo de atendimento: ')
enterDate = datetime.utcnow()

registrar = UserAttendance(name, attendace, enterDate)

print(registrar)