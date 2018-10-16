import DataTransformer
import json
import os

inverted_index = {}


def save_term_id_file():
    file = os.path.join(os.getcwd(), 'output/' + 'TermIDFile.txt')
    with open(file, 'w') as termIDFile:
        json.dump([DataTransformer.term_termId_dict, DataTransformer.termId_frequency_dict], termIDFile)


def save_doc_id_file():
    file = os.path.join(os.getcwd(), 'output/' + 'DocumentIDFile.txt')
    with open(file, 'w') as documentIDFile:
        json.dump([DataTransformer.docId_docName_dict, DataTransformer.docId_docLength_dict], documentIDFile)


def create_inverted_index():
    for term in DataTransformer.terms:
        term_id = DataTransformer.term_termId_dict[term]
        for docId in DataTransformer.docId_tokens_dict:
            frequency = DataTransformer.docId_tokens_dict[docId].count(term)
            posting = (docId, frequency)
            if term_id not in inverted_index:
                inverted_index[term_id] = []
            if frequency > 0:
                inverted_index[term_id].append(posting)


def save_inverted_index():
    create_inverted_index()
    file = os.path.join(os.getcwd(), 'output/' + 'InvertedIndex.txt')
    with open(file, 'w') as index_file:
        json.dump(inverted_index, index_file)


save_term_id_file()
save_doc_id_file()
save_inverted_index()