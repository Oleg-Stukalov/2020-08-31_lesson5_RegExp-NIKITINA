import re

pattern = r"(\+7|8)?\s*\(\s*(\d+)\s*\)\s*(\d+)(\s*|-?)(\d+)(\s*|-?)(\d+)"
regex = re.compile(pattern)

text = '(812) 433-31-16;" (812) 433-30-52; (812) 640-35-34                                           ";"Секретарь  начальника: 8 (812) 433-30-45; Бухгалтерия: 8 (812) 433-49-88; Заместитель начальника пансионата по административно-хозяйственной деятельности: 8 (812)  432-97-31;                                   Заместитель начальника пансионата профилактическо-оздоровительного отделения: 8 (812)  432-97-32; Заместитель начальника пансионата-начальник филиала: 8(40153)2-10-81; Администратор по размещению: 8 (812) 432-97-33   '

text2 = regex.sub(r"+7 (\2) \3-\5-\7", text)
#text2 = regex.sub(r"(\+7|8)?\s*\(\s*(\d+)\s*\)\s*(\d+)(\s*|-?)(\d+)(\s*|-?)(\d+)", text)
print('***text2: ', text2)

phones_list = regex.findall(text)
print('phones_list: ', phones_list)
print("".join(phones_list[0]))