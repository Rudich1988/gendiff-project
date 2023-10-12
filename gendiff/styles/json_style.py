from gendiff.styles.data_conversion import data_conversion

INDENT_QUANTITY = 4


def transformation_value(value):
    if type(value) is str:
        if len(value) == 0:
            return '""'
        elif value in ['true', 'false', 'null', 'None']:
            return value
        else:
            return f'"{value}"'
    return value


def get_comma(number, len_data):
    if len_data == number:
        return ''
    return ','


def final_style(files_data, enclosure=1, flag=True):
    if type(files_data) is not dict:
        return str(transformation_value(files_data))
    else:
        finish_string = '{\n'
        count = 0
        for key, value in files_data.items():
            count += 1
            possible_comma = get_comma(count, len(files_data))
            if key[:2] != '- ' and key[:2] != '+ ':
                finish_string += ((INDENT_QUANTITY * enclosure) * ' '
                                  + f'"{key}"' + ': '
                                  + final_style(value, enclosure=enclosure + 1)
                                  + possible_comma + '\n')
            else:
                finish_string += ((INDENT_QUANTITY * enclosure - 2) * ' '
                                  + f'"{key}"' + ': '
                                  + final_style(value, enclosure=enclosure + 1)
                                  + possible_comma + '\n')
        finish_string += (INDENT_QUANTITY * (enclosure - 1)) * ' ' + '}'
        return finish_string


def get_json_style(data):
    return final_style(data_conversion(data))
