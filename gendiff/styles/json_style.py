from gendiff.styles.data_conversion import data_conversion

INDENT_QUANTITY = 4


def transformation_value(value):
    #if isinstance(value, str):
     #   if len(value) == 0:
      #      return '""'
    if value in ['true', 'false', 'null'] or isinstance(value, int):
        return value
    return f'"{value}"'
    #return value


def get_comma(number, len_data):
    if len_data == number:
        return ''
    return ','


def create_string(enclosure, key, value, possible_comma, number=0):
    string = ((INDENT_QUANTITY * enclosure - number) * ' '
              + f'"{key}"' + ': '
              + final_style(value, enclosure=enclosure + 1)
              + possible_comma + '\n')
    return string


def final_style(files_data, enclosure=1):
    if not isinstance(files_data, dict):
        return str(transformation_value(files_data))
    else:
        finish_string = '{\n'
        count = 0
        for key, value in files_data.items():
            count += 1
            possible_comma = get_comma(count, len(files_data))
            if key[:2] != '- ' and key[:2] != '+ ':
                finish_string += create_string(enclosure, key, value,
                                               possible_comma)
            else:
                finish_string += create_string(enclosure, key, value,
                                               possible_comma, number=2)
        finish_string += (INDENT_QUANTITY * (enclosure - 1)) * ' ' + '}'
        return finish_string


def get_json_style(diff_files_data):
    return final_style(data_conversion(diff_files_data))
