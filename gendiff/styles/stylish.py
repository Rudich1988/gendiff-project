from gendiff.styles.data_conversion import data_conversion


INDENT_QUANTITY = 4


def create_string(enclosure, key, value, number=0):
    string = ((INDENT_QUANTITY * enclosure - number)
              * ' ' + key + ': '
              + final_style(value, enclosure=enclosure + 1)
              + '\n')
    return string


def final_style(files_data, enclosure=1):
    if not isinstance(files_data, dict):
        return str(files_data)
    finish_string = '{\n'
    for key, value in files_data.items():
        if key[:2] != '- ' and key[:2] != '+ ':
            finish_string += create_string(enclosure, key, value)
        else:
            finish_string += create_string(enclosure, key, value, number=2)
    finish_string += (INDENT_QUANTITY * (enclosure - 1)) * ' ' + '}'
    return finish_string


def get_stylish(diff_files_data):
    return final_style(data_conversion(diff_files_data))
