import os

def get_required_files():
    required_files = []
    required_files.append('package.json')
    required_files.append('README.md')
    required_files.append('index.html')
    required_files.append('src/index.js')
    return required_files

def check_project_structure(root_dir):
    required_files = get_required_files()
    for file in required_files:
        file_path = os.path.join(root_dir, file)
        if not os.path.exists(file_path):
            return False
    return True

def main():
    root_dir = os.getcwd()
    if check_project_structure(root_dir):
        print("Project structure is correct.")
    else:
        print("Project structure is incorrect. Please refer to the documentation or contact the project maintainer.")

if __name__ == "__main__":
    main()