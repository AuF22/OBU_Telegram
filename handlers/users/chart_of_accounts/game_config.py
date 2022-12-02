import json
import random


def random_values():
    with open('C:\\Users\\analitik2\\PycharmProjects\\OBU_Telegram\\handlers\\users\\chart_of_accounts\\chart_of_accounting.json', 'r') as file:
        all_values = json.load(file)
    return all_values
