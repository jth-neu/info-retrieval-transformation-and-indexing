import re
from Utils import *

termId = 0
term_termId_dict = {}
termId_frequency_dict = {}
current_terms = {}
docId_docName_dict = {}
docId_docLength_dict = {}
docId_tokens_dict = {}
terms = set()
total_size = 0
total_token_number = 0


def transform_data_from_folder(folder_name, number_of_files):
    file_count = 0
    for filename in os.listdir(os.path.join(os.getcwd(), folder_name)):
        file_count += 1
        if file_count > number_of_files:
            break
        path = os.path.join(os.getcwd(), folder_name + '/' + filename)
        tokens = transform_data(path)
        save_tokens_to_file(tokens, filename, file_count)
        update_frequency()

        # stats
        global total_size, total_token_number
        total_size += os.path.getsize(path)
        total_token_number += len(tokens)


def transform_data(filename):
    with open(filename, 'r') as f:
        data = f.read()
        data = data.replace('.', '')   # Remove periods
        data = re.sub(r'<(head).*?</\1>(?s)', '', data)  # Remove head section from html
        data = re.sub(r'<(script).*?</\1>(?s)', '', data)  # Remove script section from html
        data = re.sub(r'<(style).*?</\1>(?s)', '', data)  # Remove style section from html
        data = re.sub(r'<[^>]*?>', ' ', data)  # Remove html tags
        text = re.sub(r'[^\w\s]', ' ', data)  # Remove all punctuations
        tokens = text.split()
        global current_terms, terms
        current_terms = set(tokens)
        terms.update(tokens)
        return tokens


# Write tokens to files
def write_tokens_to_file(filename, data):
    global termId
    with open(filename, 'w') as file:
        for element in data:
            file.write(element + '\n')
            if element not in term_termId_dict:
                term_termId_dict[element] = termId
                termId += 1


def save_tokens_to_file(tokens, filename, file_count):
    file = os.path.join(os.getcwd(), 'tokens/' + str(file_count) + '-' + filename)
    if not os.path.isfile(file):
        write_tokens_to_file(file, tokens)
        docId_docName_dict[file_count] = filename.replace('.txt', '')
        docId_docLength_dict[file_count] = len(tokens)
        docId_tokens_dict[file_count] = tokens


def update_frequency():
    for term in current_terms:
        term_id = term_termId_dict[term]
        if term_id not in termId_frequency_dict:
            termId_frequency_dict[term_id] = 1
        else:
            termId_frequency_dict[term_id] += 1


create_project_dir()
transform_data_from_folder(args.FolderName, args.NumFilesToProcess)
