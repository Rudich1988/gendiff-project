from gendiff.styles.data_conversion import data_conversion


INDENT_QUANTITY = 4


def transformation_value(value):
    if type(value) is str:
        if len(value) == 0:
            return ''
    return value


def final_style(files_data, enclosure=1):
    if type(files_data) is not dict:
        return str(transformation_value(files_data))
    else:
        finish_string = '{\n'
        for key, value in files_data.items():
            if key[:2] != '- ' and key[:2] != '+ ':
                finish_string += ((INDENT_QUANTITY * enclosure) *
                                  ' ' + key + ': ' +
                                  final_style(value, enclosure=enclosure + 1) +
                                  '\n')
            else:
                finish_string += ((INDENT_QUANTITY * enclosure - 2) *
                                  ' ' + key + ': ' +
                                  final_style(value, enclosure=enclosure + 1) +
                                  '\n')
        finish_string += (INDENT_QUANTITY * (enclosure - 1)) * ' ' + '}'
        return finish_string


def get_stylish(data):
    return final_style(data_conversion(data))
