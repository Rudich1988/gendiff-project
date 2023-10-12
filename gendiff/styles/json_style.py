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
            return '""'
        elif value in ['true', 'false', 'null', 'None']:
            return value
        else:
            return f'"{value}"'
    return value


def get_comma(flag):
    if flag is False:
        return ','
    return ''


def final_stylish(files_data, indent_quantity=4, enclosure=1):
    if type(files_data) is not dict:
        return str(check(files_data))
    else:
        finish_string = '{\n'
        if equality_check(files_data) is True:
            comma = 0
            for key, value in files_data.items():
                flag = False
                comma += 1
                if comma == len(files_data):
                    flag = True
                finish_string += (indent_quantity * enclosure) * ' ' + f'"{key}"' + ': ' + final_stylish(value, enclosure=enclosure + 1) + get_comma(flag) + '\n'
            finish_string += (indent_quantity * (enclosure - 1)) * ' ' + '}'
            return finish_string
        comma = 0
        for key, value in files_data.items():
            flag = False
            comma += 1
            if comma == len(files_data) and len(files_data) != 1:
                flag = True
            if key[:2] != '- ' and key[:2] != '+ ':
                finish_string += (indent_quantity * enclosure) * ' ' + f'"{key}"' + ': ' + final_stylish(value, enclosure=enclosure + 1) + get_comma(flag) + '\n'
            else:
                finish_string += (indent_quantity * enclosure - 2) * ' ' + f'"{key}"' + ': ' + final_stylish(value, enclosure=enclosure + 1) + get_comma(flag) + '\n'
        finish_string += (indent_quantity * (enclosure - 1)) * ' ' + '}'
    return finish_string


def stylish_12(data):
    return final_stylish(data_conversion(data))
