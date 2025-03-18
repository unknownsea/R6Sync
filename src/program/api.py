import os


class API:
    def __init__(self, name):
        self.file_name = name

    def get_file_name(self):
        return self.file_name
    
    def get_file(self):
        documents_path = os.path.join(os.path.expanduser("~"), "Documents")
        r6_folder_path = os.path.join(documents_path, "My Games", "Rainbow Six - Siege")
        directories = [d for d in os.listdir(r6_folder_path) if os.path.isdir(os.path.join(r6_folder_path, d))]
        if not directories:
            raise FileNotFoundError("No directories found in the Rainbow Six - Siege folder.")
        directory = os.path.join(r6_folder_path, directories[0])
        file_path = os.path.join(directory, self.file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return file.read()
        else:
            raise FileNotFoundError(f"The file {self.file_name} does not exist in the directory.")