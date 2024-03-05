def files_reader(file_list: list):
    '''Читает файл по шаблону:
            2.txt  # Имя файла
            1      # Кол-во строк
            Строка номер 1 файла номер 2
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


print(files_reader(['1.txt', '2.txt', '3.txt']))
