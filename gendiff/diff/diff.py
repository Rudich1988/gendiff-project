import json

import yaml
from gendiff.styles.json_style import stylish_12
from gendiff.styles.plain import plain
from gendiff.styles.stylish import stylish


def get_format_function(format_name):
    if format_name == 'stylish':
        return stylish
    elif format_name == 'plain':
        return plain
    elif format_name == 'json':
        return stylish_12


def check_value(value):
    if type(value) is int and (value is not True and value is not False):
        return value
    else:
        if value in [False, True]:
            file_data = str(value).lower()
        elif value is None:#!!!
            file_data = 'null'
        else:
            file_data = value
        return file_data


def create_data_file(value_name, files_directory='tests/fixtures/'):
    if type(value_name) is str:
        if value_name[-5:] == '.json':
            filepath = value_name
            if '/' not in value_name:
                filepath = files_directory + value_name
            file_data = json.load(open(filepath))
        elif value_name[-4:] == '.yml' or value_name[-5:] == '.yaml':
            filepath = value_name
            if '/' not in value_name:
                filepath = files_directory + value_name
            with open(filepath, 'r') as yaml_file:
                file_data = yaml.safe_load(yaml_file)
        else:
            return value_name
    else:
        file_data = check_value(value_name)
        return file_data
    for key, value in file_data.items():
        file_data[key] = create_data_file(value)
    return file_data


def make_diff(data1, data2=None):
    if type(data1) is not dict or data2 is None:#!!!
        return create_data_file(data1)
    data1 = create_data_file(data1)
    data2 = create_data_file(data2)
    final_diff = {}
    all_files_keys = sorted(list(set(data1) | (set(data2))))
    for key in all_files_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                final_diff[key] = (make_diff(data1[key]), 'in 2 files')
            else:
                if (data1[key] != data2[key]
                    and type(data1[key]) is type(data2[key]) is dict):#!!!
                    final_diff[key] = (make_diff(data1[key],
                                                 data2[key]),
                                                 'diff values')
                else:
                    final_diff[key] = (make_diff(data1[key]),
                                       make_diff(data2[key]),
                                       'diff types values')
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
