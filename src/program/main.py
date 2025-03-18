from api import API
R6Sync = API("GameSettings.ini")

print(R6Sync.get_file_name())
print(R6Sync.get_file())