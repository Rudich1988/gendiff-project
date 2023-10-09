def check_value(value):
    if value in ['false', 'true', 'null']:
        return False
    return True


def get_string(data, string=''):
    if type(data) != dict:
        if 'in file2' in data and len(data) == 2:
            if type(data[0]) == dict:
                return f"Property '{string}' was added with value: [complex value]\n"
            else:
                if check_value(data[0]):
                    return f"Property '{string}' was added with value: '{data[0]}'\n"
                else:
                    return f"Property '{string}' was added with value: {data[0]}\n"
        elif 'in file1' in data and len(data) == 2:
            return f"Property '{string}' was removed\n"
        elif 'diff types values' in data:
            if type(data[0]) == dict:
                if check_value(data[1]):                
                    return f"Property '{string}' was updated. From [complex value] to '{data[1]}'\n"
                else:
                    return f"Property '{string}' was updated. From [complex value] to {data[1]}\n"
            elif type(data[1]) == dict:
                if check_value(data[0]):
                    return f"Property '{string}' was updated. From '{data[0]}' to [complex value]\n"
                else:
                    return f"Property '{string}' was updated. From {data[0]} to [complex value]\n"
        elif 'not dict and diff' in data:
            if check_value(data[0]) == True and check_value(data[1]) == True:
                return f"Property '{string}' was updated. From '{data[0]}' to '{data[1]}'\n"
            elif check_value(data[0]) == True and check_value(data[1]) == False:
                return f"Property '{string}' was updated. From '{data[0]}' to {data[1]}\n"
            elif check_value(data[1]) == True and check_value(data[0]) == False:
                return f"Property '{string}' was updated. From {data[0]} to '{data[1]}'\n"
            else:
                return f"Property '{string}' was updated. From {data[0]} to {data[1]}\n"
        elif 'in 2 files' in data:
            return '\n'
        elif 'diff values' in data:
            return get_string(data[0], string)
    final_string = ''
    for key, value in data.items():
        result = str(get_string(value, string + '.' + key))
        final_string += f'{result}'
    return final_string


def plain(data):
    final_string = ''
    for key, value in data.items():
        result = f'{get_string(value, key)}\n'
        if result != '':
            final_string += result
    show_result = ''
    for row_of_differences in final_string.split('\n'):
        if row_of_differences != '':
            show_result += f'{row_of_differences}\n'
    return show_result[:-1]



    
