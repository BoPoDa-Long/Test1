text = str(input("Введіть текст для перекладу, або \"stop\" для зупинки програми: "))
eng_ukr = """`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>? """
ukr_eng = """'1234567890-=йцукенгшщзхїфівапролджєячсмитьбю.₴!"№;%:?*()_+ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ, """
all_numbers = """0123456789"""
all_symbols = """`-=[];',./~!@#$%^&*()_+{}:"<>? """
with open("Перекладач.txt", "w") as f:
    f.write("")
def translator():
    if any(s.isalpha() and s in eng_ukr for s in text):
        return"".join([ukr_eng[eng_ukr.index(symbols)] if symbols in eng_ukr else symbols for symbols in text])
    elif any(s.isalpha() and s in ukr_eng for s in text):
        return"".join([eng_ukr[ukr_eng.index(symbols)] if symbols in ukr_eng else symbols for symbols in text])
    elif all(s.isdigit() and s in all_numbers for s in text):
        return text
    elif any(s in all_symbols or s in all_numbers for s in text):
        return text
    else:
        return "Ви ввели не коректне значення, або використовуєте мову якої немає в словниках програми!"
while text.lower() not in ("stop","стоп"):
    
    print("Результат:",translator())
    text = str(input("Введіть наступний текст для перекладу: "))
print("Програму завершено!\The program is completed!")