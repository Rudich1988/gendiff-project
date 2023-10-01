def equality_check(files_data):
    flag = True
    for key in files_data.keys():
        if key[:2] == '+ ' or key[:2] == '- ':
            flag = False
            break
    return flag




def generate_diff(files_data, indent_quantity=4, enclosure=1):
    if type(files_data) != dict:
        return str(files_data)
    else:
        finish_string = '{\n'
        if equality_check(files_data) == True:
            for key,value in files_data.items():
                finish_string += (indent_quantity * enclosure) * ' ' + key + ': ' + generate_diff(value, enclosure=enclosure + 1) + '\n'
            finish_string += (indent_quantity * (enclosure - 1)) * ' '  + '}'
            return finish_string
        for key,value in files_data.items():
            if key[:2] != '- ' and key[:2] != '+ ':
                finish_string += (indent_quantity * enclosure) * ' '  + key + ': ' + generate_diff(value, enclosure=enclosure + 1) + '\n'
            else:
                finish_string += (indent_quantity * enclosure - 2) * ' '  + key + ': ' + generate_diff(value, enclosure=enclosure + 1) + '\n'
        finish_string += (indent_quantity * (enclosure - 1)) * ' '  + '}'
    return finish_string
