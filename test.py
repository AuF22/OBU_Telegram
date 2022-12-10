from fuzzywuzzy import fuzz
from Data.data import accounting_entries
import difflib


def sim(text1, text2):
    normalized1 = text1.lower()
    normalized2 = text2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()


list_of_entries = []

for entry in accounting_entries:
    entry = entry.split('\n', 1)
    list_of_entries.append(entry[-1])


while True:
    ent = input()
    if ent == 'end':
        break

    elif 'дт' in ent.lower() or 'д-т' in ent.lower():
        for list_ent in list_of_entries:
            similarity = sim(ent, list_ent)

            if similarity >= 0.8:
                print(similarity)
                print(list_ent, end='\n\n')
