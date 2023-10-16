from json import dumps

from gendiff.styles.data_conversion import data_conversion


def get_json_style(diff_files_data):
    return dumps(data_conversion(diff_files_data))
