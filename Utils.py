import os


# Create a directory to store all the output
def create_project_dir():
    output_folder = os.path.join(os.getcwd(), 'tokens')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

