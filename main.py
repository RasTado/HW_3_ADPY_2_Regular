from pprint import pprint
import csv
import re


def open_file(open_new_file):
    with open(open_new_file, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list

# TODO 1: выполните пункты 1-3 ДЗ


# 1 поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке
# изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;


def ls_name_corrector(data_n):
    for pos, person in enumerate(data_n):
        fnd_pattern = r'\w+'
        name = (re.findall(fnd_pattern, person[0]))
        if len(name) == 3:
            data_n[pos][0] = name[0]
            data_n[pos][1] = name[1]
            data_n[pos][2] = name[2]
        elif len(name) == 2:
            data_n[pos][0] = name[0]
            data_n[pos][1] = name[1]
        else:
            pass


def fs_name_corrector(data_n):
    for pos, person in enumerate(data_n):
        fnd_pattern = r'\w+'
        name = (re.findall(fnd_pattern, person[1]))
        if len(name) == 2:
            data_n[pos][1] = name[0]
            data_n[pos][2] = name[1]
        else:
            pass


# 2 привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99
# доб.9999;


def phone_corrector(data_ph):
    for pos, number in enumerate(data_ph):
        fnd_pattern = r'(\+7|8)\s?\(?(\d{3}){1}\)?[\s|-]?(\d{3})?[\s|-]?(\d{2})?[\s|-]?' \
                      r'(\d{2})?[\ |(]*(доб[.])*]?\s*]?(\d*)[\ |)]*'
        res_pattern = '+7(\\2)\\3-\\4-\\5 \\6\\7'
        result = re.sub(fnd_pattern, res_pattern, number[5]).strip()
        data_ph[pos][5] = result


# 3 объединить все дублирующиеся записи о человеке в одну.


def unit_double(data_ud):
    result_list = [data_ud[0]]
    del (data_ud[0])
    data_ud.sort()
    result_list.append(data_ud[0])
    for list_ in data_ud:
        if list_[0] == result_list[-1][0] and list_[1] == result_list[-1][1]:
            for pos, value in enumerate(result_list[-1]):
                if not value:
                    result_list[-1][pos] = list_[pos]
        else:
            result_list.append(list_)
    return result_list


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

def write_file(r_data):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(r_data)


if __name__ == '__main__':
    data = open_file('phonebook_raw.csv')
    ls_name_corrector(data)
    fs_name_corrector(data)
    phone_corrector(data)
    res_data = unit_double(data)
    write_file(res_data)