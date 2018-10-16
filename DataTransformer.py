import re
from Utils import *


def transform_data_from_folder(folder_name, number_of_files):
    file_count = 0
    for filename in os.listdir(os.path.join(os.getcwd(), folder_name)):
        file_count += 1
        if file_count > number_of_files:
            break
        tokens = transform_data(os.path.join(os.getcwd(), folder_name + '/' + filename))
        save_tokens_to_file(tokens, filename, file_count)


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
        return tokens


# Write tokens to files
def write_tokens_to_file(filename, data):
    with open(filename, 'w') as file:
        for element in data:
            file.write(element + '\n')


def save_tokens_to_file(tokens, filename, file_count):
    file = os.path.join(os.getcwd(), 'tokens/' + str(file_count) + '-' + filename)
    if not os.path.isfile(file):
        write_tokens_to_file(file, tokens)


create_project_dir()
transform_data_from_folder('crawled_pages', 10)
