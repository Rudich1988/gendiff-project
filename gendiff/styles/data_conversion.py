def get_new_key_value(value):
    if type(value[0]) is dict:
        new_value_1 = value[0]
        new_value_2 = data_conversion(value[1])
    elif type(value[1]) is dict:
        new_value_1 = data_conversion(value[0])
        new_value_2 = value[1]
    else:
        new_value_1 = data_conversion(value[0])
        new_value_2 = data_conversion(value[1])
    return (new_value_1, new_value_2)


def check_description_data(key, value):
    if 'in file1' in value:
        return '- ' + key
    return '+ ' + key


def data_conversion(data):
    if type(data) is not dict:
        return str(data)
    final_data = {}
    for key, value in data.items():
        if 'in file1' in value or 'in file2' in value:
            new_key = check_description_data(key, value)
            final_data[new_key] = value[0]
        elif 'in 2 files' in value or 'diff values' in value:
            final_data[key] = data_conversion(value[0])
        elif 'diff types values' in value:
            new_value = get_new_key_value(value[:-1])
            final_data['- ' + key] = new_value[0]
            final_data['+ ' + key] = new_value[1]
    return final_data
