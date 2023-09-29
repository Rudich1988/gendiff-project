import json
import yaml


def create_data_file(file, directory):
    if file[-4:] == 'json':
        return change_values(file, directory)
    elif file[-3:] == 'yml' or file[-4:] == 'yaml':
        return change_values_yaml(file, directory)


def change_values(file, directory):
    path_file = directory + file
    file_data = json.load(open(path_file))
    for key, value in file_data.items():
        if value in [False, True]:
            file_data[key] = str(value).lower()
    return file_data


def change_values_yaml(file, directory):
    path_file = directory + file
    with open(path_file, 'r') as yaml_file:
        file_data = yaml.safe_load(yaml_file)
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
            files_diff[key] = ('- ' + key + ': ' + str(data_1[key]) +
                               '\n' + '  + ' + key + ': ' + str(data_2[key]))
        elif key in data_1 and key not in data_2:
            files_diff[key] = '- ' + key + ': ' + str(data_1[key])
        elif key not in data_1 and key in data_2:
            files_diff[key] = '+ ' + key + ': ' + str(data_2[key])
    return files_diff


def generate_diff(file_1, file_2, files_directory):
    file_1_data = create_data_file(file_1, files_directory)
    file_2_data = create_data_file(file_2, files_directory)
    all_files_keys = sorted(list(set(file_1_data) | (set(file_2_data))))
    files_diff_result = '{\n'
    files_diff = make_files_diff(all_files_keys, file_1_data, file_2_data)
    files_values = list(files_diff.values())
    flag = False
    for value in files_values:
        if value[:2] == '- ' or value[:2] == '+ ':
            flag = True
    for index in files_diff:
        if flag:
            if files_diff[index][:2] in ['- ', '+ ']:
                files_diff_result += '  ' + files_diff[index] + '\n'
            else:
                files_diff_result += '    ' + files_diff[index] + '\n'
        else:
            files_diff_result += '  ' + files_diff[index] + '\n'
    files_diff_result += '}'
    return files_diff_result
