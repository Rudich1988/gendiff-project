import json
import yaml


from gendiff.styles.stylish import stylish
from gendiff.styles.plain import plain
from gendiff.styles.json_style import stylish_12


def get_format_function(format_name):
    if format_name == 'stylish':
        return stylish
    elif format_name == 'plain':
        return plain
    elif format_name == 'json':
        return stylish_12


def create_data_file(file, files_directory='tests/fixtures/'):
    flag = True
    if isinstance(type(file), dict):
        file_data = file
    elif type(file) == str:
        if file in [False, True]:
            file_data = str(file).lower()
        elif file[-5:] == '.json':
            file = files_directory + file
            file_data = json.load(open(file))
        elif file[-4:] == '.yml' or file[-5:] == '.yaml':
            file = files_directory + file
            with open(file, 'r') as yaml_file:
                file_data = yaml.safe_load(yaml_file)
                flag = False
        else:
            return file
    else:
        if file in [False, True]:
            file_data = str(file).lower()
        elif file == None:
            file_data = 'null'
        elif file == 'None' and flag == False:
            file_data == 'null'
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
    elif type(data1) == dict and data2 == None:
        return create_data_file(data1)
    data1 = create_data_file(data1)
    data2 = create_data_file(data2)
    final_diff = {}
    all_files_keys = sorted(list(set(data1) | (set(data2))))
    for key in all_files_keys:
        if key in data1 and key in data2 and type(data1[key]) != dict:
            if data1[key] == data2[key]:
                final_diff[key] = (make_diff(data1[key]), 'in 2 files')
            else:
                final_diff[key] = (make_diff(data1[key]), make_diff(data2[key]), 'not dict and diff')
        elif key in data1 and key in data2 and data1[key] != data2[key]:
            if type(data1[key]) != type(data2[key]) and (type(data1[key]) == dict or type(data2[key]) == dict):
                final_diff[key] = (data1[key], data2[key], 'diff types values')
            if key in data1 and key in data2 and data1[key] != data2[key] and type(data1[key]) == type(data2[key]) == dict:
                final_diff[key] = (make_diff(data1[key], data2[key]), 'diff values')
            elif key in data1 and key not in data2:
                final_diff[key] = (make_diff(data1[key]), make_diff(data2[key]), 'in file1')
        elif key not in data1 and key in data2:
            final_diff[key] = (make_diff(data2[key]), 'in file2')
        elif key not in data2 and key in data1:
            final_diff[key] = (make_diff(data1[key]), 'in file1')
    return final_diff


def generate_diff(file_1, file_2, format='stylish'):
    format_function = get_format_function(format)
    file_1_data = create_data_file(file_1)
    file_2_data = create_data_file(file_2)
    return format_function(make_diff(file_1_data, file_2_data))
