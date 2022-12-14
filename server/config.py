import re

password = ''
local_ip = ''
port = ''

# configure password and local port
def config():
    global password, local_ip, port
    config_file = open('config.txt', 'r')
    line_number = 1
    for line in config_file:
        conf = re.findall('(.*)=(.*)', line)

        # config password
        if conf[0][0] == 'password':
            password = conf[0][1]

        # config port
        if conf[0][0] == 'port':
            port = conf[0][1]
        
    config_file.close()