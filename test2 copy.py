from datetime import datetime

# Припустимо, у нас є дата у вигляді рядка
date_string = "Сьогодні: 2023.03.12"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу
