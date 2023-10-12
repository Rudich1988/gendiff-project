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
        elif value is None:
            file_data = 'null'
        else:
            file_data = value
        return file_data


def processing_filepath(filepath, directory='tests/fixtures/'):
    if filepath[-5:] == '.json':
        if '/' not in filepath:
            filepath = directory + filepath
        file_data = json.load(open(filepath))
    else:
        if '/' not in filepath:
            filepath = directory + filepath
        with open(filepath, 'r') as yaml_file:
            file_data = yaml.safe_load(yaml_file)
    return file_data


def create_data_file(value_name, files_directory='tests/fixtures/'):
    if type(value_name) is str:
        if value_name[-5:] in ['.json', '.yaml'] or value_name[-4:] == '.yml':
            file_data = processing_filepath(value_name)
        else:
            return value_name
    else:
        file_data = check_value(value_name)
        return file_data
    for key, value in file_data.items():
        file_data[key] = create_data_file(value)
    return file_data


def check_same_keys(key, file1_data, file2_data):
    if file1_data[key] == file2_data[key]:
        return (make_diff(file1_data[key]), 'in 2 files')
    else:
        if type(file1_data[key]) is type(file2_data[key]) is dict:
            return (make_diff(file1_data[key], file2_data[key]), 'diff values')
        else:
            return (make_diff(file1_data[key]), make_diff(file2_data[key]),
                    'diff types values')


def make_diff(data1, data2=None):
    if type(data1) is not dict or data2 is None:
        return create_data_file(data1)
    data1 = create_data_file(data1)
    data2 = create_data_file(data2)
    final_diff = {}
    all_files_keys = sorted(list(set(data1) | (set(data2))))
    for key in all_files_keys:
        if key in data1 and key in data2:
            final_diff[key] = check_same_keys(key, data1, data2)
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
