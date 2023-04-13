# Upload Files to GitHub Repository with Python

Do you have multiple files in various folders on your computer that you want to upload to a GitHub repository, but the process is too time-consuming to do manually? This Python script can automate the process for you!

The script will upload all files in each folder present on your computer to your personal repository on GitHub. It will also create new folders in GitHub to replicate the file organization present on your computer.

# Prerequisites
Before running the script, you will need to install the PyGithub library by running the following command in your terminal or command prompt:


`pip install PyGithub`

# Usage
1. Clone or download this repository to your computer.

2. Open `upload_to_github.py` file in your favorite text editor.

3. Replace the `ACCESS_TOKEN`, `REPO_NAME`, `LOCAL_DIR`, `REPO_DIR`, and `repo_owner` variables with your own values.

4. Save the changes to `upload_to_github.py`.

5. Open your terminal or command prompt and navigate to the directory where the `upload_to_github.py` script is located.

6. Run the script by typing the following command:

`python3 upload_to_github.py`

The script will start uploading the files to your GitHub repository. Depending on the size of the files and the number of files being uploaded, it may take a few minutes to complete.

That's it! Your files should now be uploaded to your GitHub repository. If you encounter any errors, double-check that you have entered the correct values for the variables and that your access token has the necessary permissions to upload files to the repository.



