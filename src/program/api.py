import os
import json


class API:
    def __init__(self, name):
        self.file_name = name

    def get_file_name(self):
        return self.file_name
    
    def get_file(self):
        documents_path = os.path.join(os.path.expanduser("~"), "Documents")
        r6_folder_path = os.path.join(documents_path, "My Games", "Rainbow Six - Siege")
        
        try:
            directory = next(d for d in os.listdir(r6_folder_path) if os.path.isdir(os.path.join(r6_folder_path, d)))
        except StopIteration:
            raise FileNotFoundError("No directories found in the Rainbow Six - Siege folder.")
        
        file_path = os.path.join(r6_folder_path, directory, self.file_name)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {self.file_name} does not exist in the directory.")
        
        with open(file_path, 'r') as file:
            return file.read()
        
    def ini_to_json(self, ini_content):
        config = {}
        current_section = None
        
        for line in ini_content.splitlines():
            line = line.strip()
            if not line or line.startswith(';') or line.startswith('#'):
                continue
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1].strip()
                config[current_section] = {}
            else:
                key, value = line.split('=', 1)
                if current_section is not None:
                    config[current_section][key.strip()] = value.strip()
                else:
                    config[key.strip()] = value.strip()
        
        return json.dumps(config, indent=4)

    def json_to_ini(self, json_content):
        config = json.loads(json_content)
        ini_content = ""
        
        for section, parameters in config.items():
            ini_content += f"[{section}]\n"
            for key, value in parameters.items():
                ini_content += f"{key} = {value}\n"
            ini_content += "\n"
        
        return ini_content