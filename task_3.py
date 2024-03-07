def files_reader(file_list: list):
    '''×èòàåò ôàéë ïî øàáëîíó:
            2.txt  # Èìÿ ôàéëà
            1      # Êîë-âî ñòðîê
            Ñòðîêà íîìåð 1 ôàéëà íîìåð 2
            '''
    files_dict_len = {}

    for file_name in file_list:
        with open(file_name, 'r') as f:
            for count, l in enumerate(f, 1):
                ...
            files_dict_len[count] = file_name
    sorted_len = dict(sorted(files_dict_len.items()))

    for i in sorted_len.keys():
        with open(sorted_len.get(i)) as f:
            print(str(sorted_len.get(i)))
            print(i)
            print(f.read().strip())
    return ''

def files_reader_2(file_list: list):
    '''Объединяет файлы в один по шаблону:
           2.txt  # Имя файла
           1      # Кол-во строк
           Строка номер 1 файла номер 2'''

    files_dict_len = {}

    for file_name in file_list:
        with open(file_name, 'r') as f:
            for count, l in enumerate(f, 1):
                ...
            files_dict_len[count] = file_name
    sorted_len = dict(sorted(files_dict_len.items()))

    with open('new.txt', 'w') as n_f:
        for i in sorted_len.keys():
            with open(sorted_len.get(i)) as f:
                n_f.write(str(sorted_len.get(i))+ '\n')
                n_f.write(str(i)+ '\n')
                n_f.write(f.read().strip()+ '\n')
    return ''


print(files_reader_2(['1.txt', '2.txt', '3.txt']))
