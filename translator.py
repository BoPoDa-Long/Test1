text = str(input("Введіть текст для перекладу, або \"stop\" для зупинки програми: "))
eng_ukr = """`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>? """
ukr_eng = """'1234567890-=йцукенгшщзхїфівапролджєячсмитьбю.₴!"№;%:?*()_+ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ, """
all_numbers = """0123456789"""
all_symbols = """`-=[];',./~!@#$%^&*()_+{}:"<>? """
#для (стирання) створення нового файлу наступні 2 рядки:
# with open("log_book.txt", "w") as f:
#     f.write("")
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
if text.lower() not in ("stop","стоп"):
    with open("log_book.txt", "a", encoding="utf-8") as f:
        f.write("\nНове відкриття програми:")
    k = 0
    while text.lower() not in ("stop","стоп"):
        k += 1
        with open("log_book.txt", "a", encoding="utf-8") as f:
            f.write(f"\n    Запис №{k}:\n    {str(text)} --> ")
        new_text = translator()
        print(f"Результат: {new_text}")
        with open("log_book.txt", "a", encoding="utf-8") as f:
            f.write(f"{str(new_text)}")
        text = str(input("Введіть наступний текст для перекладу: "))
    print("Програму завершено!\The program is completed!")
    with open("log_book.txt", "a", encoding="utf-8") as f:
        f.write("\nПрограму закрито!\n"+"-"*30)
else:
    print("Програму завершено!\The program is completed!")
    with open("log_book.txt", "a", encoding="utf-8") as f:
        f.write("\nПрограму закрито!\n"+"-"*30)