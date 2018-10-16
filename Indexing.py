import DataTransformer
import json
import os


def save_term_id_file():
    file = os.path.join(os.getcwd(), 'output/' + 'TermIDFile.txt')
    with open(file, 'w') as termIDFile:
        json.dump([DataTransformer.term_termId_dict, DataTransformer.termId_frequency_dict], termIDFile)

save_term_id_file()