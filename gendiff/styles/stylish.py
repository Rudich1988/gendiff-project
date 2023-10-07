def equality_check(files_data):
    flag = True
    for key in files_data.keys():
        if key[:2] == '+ ' or key[:2] == '- ':
            flag = False
            break
    return flag


def final_stylish(files_data, indent_quantity=4, enclosure=1):
    if type(files_data) != dict:
        return str(files_data)
    else:
        finish_string = '{\n'
        if equality_check(files_data) == True:
            for key,value in files_data.items():
                finish_string += (indent_quantity * enclosure) * ' ' + key + ': ' + final_stylish(value, enclosure=enclosure + 1) + '\n'
            finish_string += (indent_quantity * (enclosure - 1)) * ' '  + '}'
            return finish_string
        for key,value in files_data.items():
            if key[:2] != '- ' and key[:2] != '+ ':
                finish_string += (indent_quantity * enclosure) * ' '  + key + ': ' + final_stylish(value, enclosure=enclosure + 1) + '\n'
            else:
                finish_string += (indent_quantity * enclosure - 2) * ' '  + key + ': ' + final_stylish(value, enclosure=enclosure + 1) + '\n'
        finish_string += (indent_quantity * (enclosure - 1)) * ' '  + '}'
    return finish_string




def stylish_1(data):
    if type(data) != dict:
        return str(data)
    final_data = {}
    for key, value in data.items():
        if 'in file1' in value:
            final_data['- ' + key] = value[0]
        elif 'in file2' in value:
            final_data['+ ' + key] = value[0]
        elif 'in 2 files' in value:
            final_data[key] = stylish_1(value[0])
        elif 'not dict and diff' in value:
            final_data['- ' + key] = stylish_1(value[0])
            final_data['+ ' + key] = stylish_1(value[1])
        elif 'diff values' in value:
            final_data[key] = stylish_1(value[0])
            #final_data['+ ' + key] = stylish_1(value[1])
        elif 'diff types values' in value:
            if type(value[0]) == dict:
                final_data['- ' + key] = value[0]
                final_data['+ ' + key] = stylish_1(value[1])
            else:
                final_data['- ' + key] = stylish_1(value[0])
                final_data['+ ' + key] = value[1]
    return final_data


def stylish(data):
    return final_stylish(stylish_1(data))
    