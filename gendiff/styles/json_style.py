from gendiff.styles.data_conversion import data_conversion

INDENT_QUANTITY = 4


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

'''
def get_comma(flag):
    if flag is False:
        return ','
    return ''
'''
'''
def get_json_format_line(files_data, enclosure):
    finish_string = ''
    if equality_check(files_data) is True:
        count = 0
        for key, value in files_data.items():
            flag = False
            count += 1
            if count == len(files_data) and len(files_data) != 1:
                flag = True
            finish_string += (INDENT_QUANTITY * enclosure) * ' ' + f'"{key}"' + ': ' + final_stylish(value, enclosure=enclosure + 1) + get_comma(flag) + '\n'
        finish_string += (INDENT_QUANTITY * (enclosure - 1)) * ' ' + '}'
    return finish_string
'''



#!!!
def ge_comma(number, len_data):
    if len_data == number:
        return ''
    return ','




def final_style(files_data, enclosure=1, flag=True):
    if type(files_data) is not dict:
        return str(check(files_data))
    else:
        finish_string = '{\n'
        count = 0
        for key, value in files_data.items():
            count += 1
            possible_comma = ge_comma(count, len(files_data))
            if key[:2] != '- ' and key[:2] != '+ ':
                finish_string += (INDENT_QUANTITY * enclosure) * ' ' + f'"{key}"' + ': ' + final_style(value, enclosure=enclosure + 1) + ge_comma(count, len(files_data)) + '\n'
            else:
                finish_string += (INDENT_QUANTITY * enclosure - 2) * ' ' + f'"{key}"' + ': ' + final_style(value, enclosure=enclosure + 1) + ge_comma(count, len(files_data)) + '\n'
        finish_string += (INDENT_QUANTITY * (enclosure - 1)) * ' ' + '}'
        return finish_string
#!!!






'''
def final_stylish(files_data, enclosure=1):
    if type(files_data) is not dict:
        return str(check(files_data))
    else:
        finish_string = '{\n'
        #finish_string += get_json_format_line(files_data, enclosure)
        if equality_check(files_data) is True:
            count = 0
            for key, value in files_data.items():
                flag = False
                count += 1
                if count == len(files_data):
                    flag = True
                finish_string += (INDENT_QUANTITY * enclosure) * ' ' + f'"{key}"' + ': ' + final_stylish(value, enclosure=enclosure + 1) + get_comma(flag) + '\n'
            finish_string += (INDENT_QUANTITY * (enclosure - 1)) * ' ' + '}'
            return finish_string
        count = 0
        for key, value in files_data.items():
            flag = False
            count += 1
            if count == len(files_data) and len(files_data) != 1:
                flag = True
            if key[:2] != '- ' and key[:2] != '+ ':
                finish_string += (INDENT_QUANTITY * enclosure) * ' ' + f'"{key}"' + ': ' + final_stylish(value, enclosure=enclosure + 1) + get_comma(flag) + '\n'
            else:
                finish_string += (INDENT_QUANTITY * enclosure - 2) * ' ' + f'"{key}"' + ': ' + final_stylish(value, enclosure=enclosure + 1) + get_comma(flag) + '\n'
        finish_string += (INDENT_QUANTITY * (enclosure - 1)) * ' ' + '}'
    return finish_string
'''

def stylish_12(data):
    return final_style(data_conversion(data))
    #return final_stylish(data_conversion(data))
