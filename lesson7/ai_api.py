import configparser

config_ini = configparser.ConfigParser()
config_ini.read('auth.ini', encoding='utf-8')

user = config_ini['DEFAULT']['User']
endpoint = config_ini['DEFAULT']['Endpoint']
auth_key = config_ini['DEFAULT']['Auth_key']

print(endpoint, auth_key)