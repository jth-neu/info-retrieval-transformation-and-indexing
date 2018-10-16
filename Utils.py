import os


# Create a directory to store all the output
def create_project_dir():
    token_folder = os.path.join(os.getcwd(), 'tokens')
    output_folder = os.path.join(os.getcwd(), 'output')
    if not os.path.exists(token_folder):
        os.mkdir(token_folder)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
