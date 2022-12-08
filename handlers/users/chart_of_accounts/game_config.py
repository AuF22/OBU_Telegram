import json


def chart_all_values() -> dict:
    """
    Загружает план счетов из json файла для дальнейшей обработки
    Loads chart of accounts from json file for further processing
    :return: dict
    """
    with open('handlers/users/chart_of_accounts/chart_of_accounting.json', 'r') as file:
        all_values = json.load(file)
    return all_values


def wiring_all_values() -> dict:
    """
    Загружает список для дальнейшей ее переработки в словарь
    Loads a list for further processing into a dictionary
    :param: from Data.data import accounting_entries # список с хоз.операциями
    :return: dict
    """
    from Data.data import accounting_entries
    all_values = {}
    for entry in accounting_entries:
        entry = entry.split('\n', 1)[::]
        all_values[entry[1]] = entry[0]
    return all_values
