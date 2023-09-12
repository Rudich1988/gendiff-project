import json


def change_values(file):
    path_file = 'gendiff/files/' + file
    file_data = json.load(open(path_file))
    for key, value in file_data.items():
        if value in [False, True]:
            file_data[key] = str(value).lower()
    return file_data


def make_files_diff(files_keys, data_1, data_2):
    files_diff = {}
    for key in files_keys:
        if key in data_1 and key in data_2 and data_1[key] == data_2[key]:
            files_diff[key] = key + ': ' + str(data_1[key])
        elif key in data_1 and key in data_2 and data_1[key] != data_2[key]:
            files_diff[key] = '- ' + key + ': ' + str(data_1[key]) + '\n' + '  + ' + key + ': ' + str(data_2[key])
        elif key in data_1 and key not in data_2:
            files_diff[key] = '- ' + key + ': ' + str(data_1[key])
        elif key not in data_1 and key in data_2:
            files_diff[key] = '+ ' + key + ': ' + str(data_2[key])
    return files_diff

def generate_diff(file_1, file_2):
    file_1_data = change_values(file_1)
    file_2_data = change_values(file_2)
    all_files_keys = sorted(list(set(file_1_data) | (set(file_2_data))))
    files_diff_result = '{\n'
    files_diff = make_files_diff(all_files_keys, file_1_data, file_2_data)
    files_values = list(files_diff.values())
    flag = False
    for value in files_values:
        if value[:2] == '- ' or value[:2] == '+ ':
            flag = True
    for index in files_diff:
        if flag == True:
            if files_diff[index][:2] in ['- ', '+ ']:
                files_diff_result += '  ' + files_diff[index] + '\n'
            else:
                files_diff_result += '    ' + files_diff[index] + '\n'
        else:
            files_diff_result += '  ' + files_diff[index] + '\n'
    files_diff_result += '\n}'
    return files_diff_result
