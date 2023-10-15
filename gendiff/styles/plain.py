from gendiff.diff.diff_names import (IN_2_FILES, IN_FILE1,
                                     DIFF_TYPES_VALUES, DIFF_VALUES)


def check_value(value):
    if value in ['false', 'true', 'null'] or isinstance(value, int):
        return value
    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def create_description_diff(path, data):
    if IN_FILE1 in data:
        return f"Property '{path}' was removed\n"
    if DIFF_TYPES_VALUES in data:
        return (f"Property '{path}' was updated. "
                f"From {check_value(data[0])} to {check_value(data[1])}\n")
    if IN_2_FILES in data:
        return '\n'
    if DIFF_VALUES in data:
        return get_string(data[0], path)
    else:
        return (f"Property '{path}' was "
                f"added with value: {check_value(data[0])}\n")


def get_string(data, path_value=''):
    if not isinstance(data, dict):
        description = create_description_diff(path_value, data)
        return description
    final_string = ''
    for key, value in data.items():
        result = str(get_string(value, path_value + '.' + key))
        final_string += f'{result}'
    return final_string


def get_plain_style(diff_files_data):
    final_string = ''
    for key, value in diff_files_data.items():
        result = f'{get_string(value, key)}\n'
        if result != '':
            final_string += result
    show_result = ''
    for row_of_differences in final_string.split('\n'):
        if row_of_differences != '':
            show_result += f'{row_of_differences}\n'
    return show_result[:-1]
