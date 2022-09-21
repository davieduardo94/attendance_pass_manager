class UserAttendance():
    def __init__(self, name, attendance, enterDate) -> None:
        self.name = name
        self.attendance = attendance
        self.enterDate = enterDate

    def __str__(self) -> str:
         return "Bem vindo %s \nTipo atendimento: %s \nHorario: %s" %(self.name, self.attendance, self.enterDate)
