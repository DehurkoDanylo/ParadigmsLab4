class Worker:
    def __init__(self, surname, oklad):
        self.surname = surname
        self.oklad = oklad

    def up_oklad(self, sum):
        self.oklad = self.oklad + sum

    def calc_procent(self, old_oklad, new_oklad):
        return (new_oklad-old_oklad)/old_oklad*100


surname = 'Дегурко'
oklad = 1350
worker = Worker(surname='Дегурко', oklad=oklad)
up_oklad_to = 1200
print('---------')
print('Актуальні дані:')
print('Прізвище - '+surname)
print('Оклад - '+str(worker.oklad))
print('---------')
print('Збільшуємо оклад на ' + str(up_oklad_to)+'грн')
print('---------')
worker.up_oklad(up_oklad_to)
print('Дані після збільшення окладу:')
print('Прізвище - '+surname)
print('Оклад - '+str(worker.oklad))
print('---------')
print('Оклад збільшийвся на '+str(worker.calc_procent(oklad,worker.oklad))+'%')
print('---------')