from gendiff.styles.data_conversion import data_conversion


def equality_check(files_data):
    flag = True
    for key in files_data.keys():
        if key[:2] == '+ ' or key[:2] == '- ':
            flag = False
            break
    return flag


def check(value):
    if type(value) is str:
        if len(value) == 0:
            return ''
    return value


def final_stylish(files_data, indent_quantity=4, enclosure=1):
    if type(files_data) is not dict:
        return str(check(files_data))
    else:
        finish_string = '{\n'
        if equality_check(files_data) is True:
            for key, value in files_data.items():
                finish_string += (indent_quantity * enclosure) * ' ' + key + ': ' + final_stylish(value, enclosure=enclosure + 1) + '\n'
            finish_string += (indent_quantity * (enclosure - 1)) * ' ' + '}'
            return finish_string
        for key, value in files_data.items():
            if key[:2] != '- ' and key[:2] != '+ ':
                finish_string += (indent_quantity * enclosure) * ' ' + key + ': ' + final_stylish(value, enclosure=enclosure + 1) + '\n'
            else:
                finish_string += (indent_quantity * enclosure - 2) * ' ' + key + ': ' + final_stylish(value, enclosure=enclosure + 1) + '\n'
        finish_string += (indent_quantity * (enclosure - 1)) * ' ' + '}'
    return finish_string

'''
def get_new_key_value(value):
    if type(value[0]) is dict:
        new_value_1 = value[0]
        new_value_2 = stylish_1(value[1])
    elif type(value[1]) is dict:
        new_value_1 = stylish_1(value[0])
        new_value_2 = value[1]
    else:
        new_value_1 = stylish_1(value[0])
        new_value_2 = stylish_1(value[1])
    return (new_value_1, new_value_2)


def stylish_1(data):
    if type(data) is not dict:
        return str(data)
    final_data = {}
    for key, value in data.items():
        if 'in file1' in value:
            final_data['- ' + key] = value[0]
        elif 'in file2' in value:
            final_data['+ ' + key] = value[0]
        elif 'in 2 files' in value:
            final_data[key] = stylish_1(value[0])
        elif 'diff values' in value:
            final_data[key] = stylish_1(value[0])
        elif 'diff types values' in value:
            new_value = get_new_key_value(value[:-1])
            final_data['- ' + key] = new_value[0]
            final_data['+ ' + key] = new_value[1]
    return final_data
'''
'''
def stylish_1(data):
    if type(data) is not dict:
        return str(data)
    final_data = {}
    for key, value in data.items():
        if 'in file1' in value:
            final_data['- ' + key] = value[0]
        elif 'in file2' in value:
            final_data['+ ' + key] = value[0]
        elif 'in 2 files' in value:
            final_data[key] = stylish_1(value[0])
        elif 'diff values' in value:
            final_data[key] = stylish_1(value[0])
        elif 'diff types values' in value:
            if type(value[0]) is dict:
                final_data['- ' + key] = value[0]
                final_data['+ ' + key] = stylish_1(value[1])
            elif type(value[1]) is dict:
                final_data['- ' + key] = stylish_1(value[0])
                final_data['+ ' + key] = value[1]
            else:
                final_data['- ' + key] = stylish_1(value[0])
                final_data['+ ' + key] = stylish_1(value[1])
    return final_data
'''

def stylish(data):
    return final_stylish(data_conversion(data))
