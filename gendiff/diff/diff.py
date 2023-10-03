import json
import yaml


def create_data_file(file):
    if isinstance(type(file), dict):
        file_data = file
    elif type(file) == str:
        if file[-5:] == '.json':
            file_data = json.load(open(file))
        elif file[-4:] == '.yml' or file[-5:] == '.yaml':
            with open(file, 'r') as yaml_file:
                file_data = yaml.safe_load(yaml_file)
        else:
            return file
    else:
        if file in [False, True]:
            file_data = str(file).lower()
        elif file == None:
            file_data = 'null'
        else:
            file_data = file
        return file_data
    for key, value in file_data.items():
        if value in [False, True]:
            file_data[key] = str(value).lower()
        elif file_data[key] == 'null':
            file_data[key] = 'null'
    return file_data


def make_diff(data1, data2=None):
    if type(data1) != dict:
        return create_data_file(data1)
    elif data2 == None:
        return create_data_file(data1)
    data1 = create_data_file(data1)
    data2 = create_data_file(data2)
    final_diff = {}
    all_files_keys = sorted(list(set(data1) | (set(data2))))
    for key in all_files_keys:
        if (key in list(set(data1) & set(data2)) and
            (data1[key] == data2[key] or
             (type(data1[key]) == type(data2[key]) == dict))):
            final_diff[str(key)] = make_diff(data1[key], data2[key])
        elif (key in list(set(data1) & set(data2)) and
              (data1[key] != data2[key] and (type(data1[key]) != dict or
                                             type(data2[key]) != dict))):
            final_diff['- ' + str(key)] = make_diff(data1[key])
            final_diff['+ ' + str(key)] = make_diff(data2[key])
        elif key not in list(set(data1) & set(data2)) and key in data1:
            final_diff['- ' + str(key)] = make_diff(data1[key])
        elif key not in list(set(data1) & set(data2)) and key in data2:
            final_diff['+ ' + str(key)] = make_diff(data2[key])
    return final_diff


def generate_diff(file_1, file_2, format, files_directory='gendiff/files/'):
    file_1_data = create_data_file(files_directory + file_1)
    file_2_data = create_data_file(files_directory + file_2)
    return format(make_diff(file_1_data, file_2_data))
