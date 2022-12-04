import json


def chart_all_values():
    with open('C:\\Users\\mrase\\OneDrive\\Documents\\GitHub\\OBU_Telegram\\handlers\\users\\chart_of_accounts'
              '\\chart_of_accounting.json', 'r') as file:
        all_values = json.load(file)
    return all_values


def wiring_all_values():
    from Data.data import accounting_entries
    all_values = {}
    for entry in accounting_entries:
        entry = entry.split('\n', 1)[::]
        all_values[entry[1]] = entry[0]
    return all_values
