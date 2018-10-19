i. A one or two sentence answer each to the questions: What was the most difficult
part of this assignment? What was the easiest part?

I think the most difficult part is how to get the tokens from each html file. The easiest part
is to save the tokens to output files.

ii. Details about the format of the 3 index files (described in Part 2 below) you created.

For the TermIDFile, I used two a list of two dictionaries, the first dictionary is term to termId, the second one is
termId to document frequency.

Similarly, for DocumentIDFile, I also have a list of two dictionaries, one for document ID to document name, the other
one is document ID to document length.

In order to store the InvertedIndex, I used a dictionary of list of tuples. The dictionary key are the termIDs,
the values are lists of postings. Each post is a tuple, the first element in the tuple is the document ID and the second
one is the relevant term frequency.

iii. A run of the query Q and the results you got (see Part 3).

Search for "Baidu":
python UseIndex.py Baidu
Returns a list of document names:
['316', '260', '274', '264', '338', '11', '375', '361', '360', '75', '71', '172', '166', '358', '173', '66', '341',
 '382', '235', '223', '40', '168', '41', '352', '2', '184', '345', '90', '230', '280', '323', '336', '120', '35', '281',
  '283', '254', '122', '22', '133', '324', '318', '126', '33', '244', '250', '332']

iv. Optional: Any additional information you may wish to provide about running the
scripts.

Execute RunDataTransformer.sh will generate all the token files. Execute CreateIndex.sh will not only generate all the
token files but also produce the index files.
Since the process takes a really long time, I suggest only run the CreateIndex.sh and it will get you all the
required outputs.

Command for create index: ./CreateIndex.sh 'crawled_pages' 900
Command for use index: python UseIndex.py Baidu

Also, there is no extra package installed in this environment, therefore the requirement.txt is empty.