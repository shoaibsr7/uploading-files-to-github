# Run the following command on terminal first depending on what python version you are using
# (Either) python3 -m pip install PyGithub
# (OR) pip install PyGithub

# github package is used to interact with GitHub API which you will get from PyGithub
from github import Github
# os package is used to traverse through the local directory and its subdirectories
import os

# Your personal access token for GitHub authentication
ACCESS_TOKEN = 'XXX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Creating a PyGithub object using your access token
g = Github(ACCESS_TOKEN)

# The repository where you want to upload the files
REPO_NAME = 'xyz'

# The path to the local directory where your files are located
LOCAL_DIR = '/Users/xyz/'

# The path in your repository where you want to upload the files
REPO_DIR = 'Assignment'
# REPO_DIR = 'Practicums'
# REPO_DIR = 'Quiz'
# REPO_DIR = 'Lab'
# REPO_DIR = 'Notes'

# The owner of the repository
repo_owner = 'xyz'

# Getting the repository object
repo = g.get_user(repo_owner).get_repo(REPO_NAME)

# Traversing through the local directory and its subdirectories
for root, dirs, files in os.walk(LOCAL_DIR):
    # Creating the directory structure in the repository
    repo_path = REPO_DIR + root.replace(LOCAL_DIR, '').replace('\\', '/')

    try:
        # Create a .gitkeep file in each directory to ensure that Git tracks empty directories
        repo.create_file(repo_path + '/.gitkeep', 'Initializing directory', branch='main')

    except:
        # If the .gitkeep file already exists, do nothing
        pass

    # Uploading each file in the directory to the repository
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'rb') as file_content:
            try:
                # Try to read the file contents as UTF-8 text
                content = file_content.read().decode('utf-8')
                repo_file_path = repo_path + '/' + file

                # Upload the file to the repository
                repo.create_file(repo_file_path, 'commit message', content, branch='main')
                print(f'{file_path} uploaded successfully!')

            except UnicodeDecodeError:
                # If the file contents cannot be decoded as UTF-8, assume it is a binary file and read it in binary mode
                content = file_content.read()
                repo_file_path = repo_path + '/' + file

                # Upload the file to the repository as a binary file
                repo.create_file(repo_file_path, 'commit message', content, branch='main')

                print(f'{file_path} uploaded successfully as binary file!')

            except:
                # If an error occurs when uploading the file, print an error message
                print(f'{file_path} failed to upload.')
