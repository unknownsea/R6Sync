from api import API
R6Sync = API("GameSettings.ini")

print(R6Sync.get_file_name())

data = R6Sync.get_file()
json_data = R6Sync.ini_to_json(data)
ini_data = R6Sync.json_to_ini(json_data)

print(data)
print(json_data)
print(ini_data)