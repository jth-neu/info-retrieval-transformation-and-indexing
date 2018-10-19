import DataTransformer
import json
import os

inverted_index = {}


def save_term_id_file():
    print('Now creating TermIDFile.')
    file = os.path.join(os.getcwd(), 'output/' + 'TermIDFile.txt')
    with open(file, 'w') as termIDFile:
        json.dump([DataTransformer.term_termId_dict, DataTransformer.termId_frequency_dict], termIDFile)


def save_doc_id_file():
    print('Now creating DocumentIDFile.')
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
    print('Now creating InvertedIndex.')
    create_inverted_index()
    file = os.path.join(os.getcwd(), 'output/' + 'InvertedIndex.txt')
    with open(file, 'w') as index_file:
        json.dump(inverted_index, index_file)


def save_stats():
    print('Now creating stats file.')
    file = os.path.join(os.getcwd(), 'stats.txt')
    index_file_size = get_index_files_size()
    with open(file, 'w') as stats_file:
        stats_file.write('Total size of all input files: ' + str(DataTransformer.total_size) + ' bytes. \n')
        stats_file.write('Total number of tokens: ' + str(DataTransformer.total_token_number) + ' \n')
        stats_file.write('Total number of unique tokens: ' + str(len(DataTransformer.terms)) + ' \n')
        stats_file.write('Total size of three index files: ' + str(index_file_size) + ' bytes. \n')
        stats_file.write('Ratio of index size to total size: ' +
                         str(index_file_size/DataTransformer.total_size) + ' \n')


def get_index_files_size():
    size = 0
    for filename in os.listdir(os.path.join(os.getcwd(), 'output')):
        path = os.path.join(os.getcwd(), 'output/' + filename)
        size += os.path.getsize(path)
    return size

save_term_id_file()
save_doc_id_file()
save_inverted_index()
save_stats()
