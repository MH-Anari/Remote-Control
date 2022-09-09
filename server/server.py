from flask import Flask
import subprocess
import config
import shlex

app = Flask(__name__) # init flask app

# handle not valid requests
@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Error 404. Command not found!</h1>', 404

@app.route('/<password>/<command>')
def cmd(password, command):
    try:
        # check password
        if password == config.password:
            command_result = subprocess.getoutput(command)
            return command_result
        else:
            return 'Password is incorrect'
    except:
        print('Invalid command')
        return 'Invalid command'

def ssh_availibility():
    ssh = subprocess.getstatusoutput('ssh')
    if ssh[0] == 0 or ssh[0] == 255:
        return True
    return False

if __name__ == '__main__':
    # configure local_port and password
    config.config()
    if ssh_availibility() == True:
        command = f'ssh -R 80:127.0.0.1:{config.port} nokey@localhost.run'
        subprocess.Popen(shlex.split(command), creationflags=subprocess.CREATE_NEW_CONSOLE)
        app.run('127.0.0.1', int(config.port))
    else:
        print('ssh is not available')