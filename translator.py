
from datetime import datetime as dt, timezone as tz
text = str(input("Введіть текст для перекладу, або \"stop\" для зупинки програми: "))
eng_ukr = """`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>? """
ukr_eng = """'1234567890-=йцукенгшщзхїфівапролджєячсмитьбю.₴!"№;%:?*()_+ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ, """
all_numbers = """0123456789"""
all_symbols = """`-=[];',./~!@#$%^&*()_+{}:"<>? """
#для (стирання) створення нового файлу наступні 2 рядки:
# with open("log_book.txt", "w") as f:
#     f.write("")
def translator():
    has_eng = any(s.isalpha() and s in eng_ukr for s in text)
    has_ukr = any(s.isalpha() and s in ukr_eng for s in text)
    eng_result = []
    ukr_result = []
    for s in text:
        if s in eng_ukr:
            eng_result.append(s)
        elif s in ukr_eng:
            ukr_result.append(s)
    eng_to_text = (len(eng_result) / len(text)) * 100
    ukr_to_text = (len(ukr_result) / len(text)) * 100
    if has_eng or has_ukr:
        result = []
        for k in text:
            if k.isalpha():
                s = k
                if s in eng_ukr:
                    result.append(ukr_eng[eng_ukr.index(s)])
                elif s in ukr_eng:
                    result.append(eng_ukr[ukr_eng.index(s)])
            elif k in eng_ukr or k in ukr_eng:
                if eng_to_text > ukr_to_text:
                    result.append(ukr_eng[eng_ukr.index(k)])
                else:
                    result.append(eng_ukr[ukr_eng.index(k)])
            else:
                result.append(k)
        return "".join(result)
#    elif has_eng:
#        return"".join([ukr_eng[eng_ukr.index(symbols)] if symbols in eng_ukr else symbols for symbols in text])
#    elif has_ukr:
#        return"".join([eng_ukr[ukr_eng.index(symbols)] if symbols in ukr_eng else symbols for symbols in text])
    elif all(s.isdigit() and s in all_numbers for s in text):
        return text
    elif any(s in all_symbols or s in all_numbers for s in text):
        return text
    else:
        return "Ви ввели не коректне значення, або використовуєте мову якої немає в словниках програми!"
if text.lower() not in ("stop","стоп"):
    open_time = dt.now().astimezone()
    with open("log_book.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{open_time.strftime("%d.%m.%Y %X")} {open_time.strftime("UTC%z")[:6]}:{open_time.strftime("UTC%z")[6:]} Нове відкриття програми:")
    k = 0
    while text.lower() not in ("stop","стоп"):
        k += 1
        new_text = translator()
        translat_time = dt.now().astimezone()
        with open("log_book.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{translat_time.strftime("%d.%m.%Y %X")} {translat_time.strftime("UTC%z")[:6]}    Запис №{k}:\n    {str(text)} --> {str(new_text)}")
        text = str(input("Введіть наступний текст для перекладу: "))
    #print("Програму завершено!\The program is completed!")
    closed_time = dt.now().astimezone()
    with open("log_book.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{closed_time.strftime("%d.%m.%Y %X")} {closed_time.strftime("UTC%z")[:6]}:{closed_time.strftime("UTC%z")[6:]} Програму закрито!\n"+"-"*47)
else:
    #print("Програму завершено!\The program is completed!")
    closed_time = dt.now().astimezone()
    with open("log_book.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{closed_time.strftime("%d.%m.%Y %X")} {closed_time.strftime("UTC%z")[:6]}:{closed_time.strftime("UTC%z")[6:]} Програму закрито!\n"+"-"*47)