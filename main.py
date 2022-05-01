
import os

def get_file_path(file_name):
    return os.path.join(os.getcwd(),file_name)

def get_dict_file(f_name, f_path,dict_file):
    with open(f_path, 'r', encoding='utf-8') as file:
        count = sum(1 for line in file)
        dict_file.setdefault(count, [f_name,f_path])

def uninon_files(dict_file,all_path):
    with open(all_path, 'w', encoding='utf-8') as file:
        for key, val in sorted(dict_file.items()):
            file.write(val[0] + '\n')
            file.write(str(key) + '\n')

            with open(val[1], 'r', encoding='utf-8') as file_list:
                line = file_list.readline()
                while line:
                    file.write(line)
                    line = file_list.readline()
                file.write('\n')
    
def main():
    sorted = 'sorted.txt'
    file1 = '1.txt'
    file2 = '2.txt'
    file3 = '3.txt'

    sorted_path = get_file_path(sorted)
    f_path_1 = get_file_path(file1)
    f_path_2 = get_file_path(file2)
    f_path_3 = get_file_path(file3)

    dict_file = {}

    get_dict_file(file1,f_path_1,dict_file)
    get_dict_file(file2,f_path_2,dict_file)
    get_dict_file(file3,f_path_3,dict_file)

    uninon_files(dict_file,sorted_path)


main()

