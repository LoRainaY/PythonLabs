# По номеру месяца напечатать пору года.
Mounths: list[str] = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

n = int(input("Введите номер месяца\n"))

try:
    if Mounths[n-1]=='Январь' or Mounths[n-1]=='Февраль' or Mounths[n-1]=='Декабрь':
        print("Зима")
    elif Mounths[n-1]=='Март' or Mounths[n-1]=='Апрель' or Mounths[n-1]=='Май':
        print("Весна")
    elif Mounths[n-1]=='Июнь' or Mounths[n-1]=='Июль' or Mounths[n-1]=='Август':
        print("Лето")
    else:
        print("Осень")
except IndexError:
    print("Неверно выбрано число")

