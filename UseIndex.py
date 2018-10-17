import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Query", help="The query you are looking for")
args = parser.parse_args()


document_id_file = json.load(open("output/DocumentIDFile.txt", "r"))
term_id_file = json.load(open("output/TermIDFile.txt", "r"))
inverted_index = json.load(open("output/InvertedIndex.txt", "r"))

docId_docName_dict = document_id_file[0]
docId_docLength_dict = document_id_file[1]
term_termId_dict = term_id_file[0]
termId_frequency_dict = term_id_file[1]


def term_to_termid(term):
    return term_termId_dict[term]


def termid_to_ilist(termid):
    return inverted_index[termid]


def term_to_docId(term):
    term_id = term_to_termid(term)
    postings = termid_to_ilist(str(term_id))
    docIds = [i[0] for i in postings]
    return docIds


def docId_to_docName(id):
    return docId_docName_dict[str(id)]


def search(query):
    try:
        docIds = term_to_docId(query)
        search_result = []
        for docId in docIds:
            search_result.append(docId_to_docName(docId))
        print(search_result)
        return search_result
    except:
        print('No results found.')


search(args.Query)
