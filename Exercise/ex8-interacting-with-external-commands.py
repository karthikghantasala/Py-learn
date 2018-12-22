"""
Its not uncommon for a process to run on a server and listen to a port.
#Unfortunately, you sometimes dont want that process to keep running, but all you know is the port that you want to free up.
#Youre going to write a script to make it easy to get rid of those pesky processes.
Write a script that does the following
Takes a port_number as its only argument.
Calls out to lsof to determine if there is a process listening on that port.
If there is a process, kill the process and inform the user.
If there is no process, print that there was no process running on that port.
Python's standard library comes with an HTTP server that you can use to start a server listening on a port (5500 in this case) with this line:
$ python -m SimpleHTTPServer 5500
Use a separate terminal window/tab to test our your script to kill that process.
Hints:
You may need to install lsof. Use this command:
$ sudo yum install -y lsof
Use this line of lsof to get the port information:
lsof -n -i4TCP:PORT_NUMBER
That will return multiple lines, and line youll want will contain LISTEN.
Use the string split() method to break a string into a list of its words.
You can either use the kill command outside of Python or the os.kill(pid, 9) function.
"""
# !/bin/python
import subprocess
import sys
import os

port_num = int(sys.argv[1])

try:
    port_num1 = int(sys.argv[1])
except ValueError:
    pass

try:
   subprocess.check_call("lsof -n -i4TCP:%d" % port_num, shell=True)
except subprocess.CalledProcessError as error:
    print ("error Message:" + str(error))


"""
import subprocess
import os
from argparse import ArgumentParser

parser = ArgumentParser(description='kill the running process listening on a given port')
parser.add_argument('port', type=int, help='the port number to search for')

port = parser.parse_args().port

try:
    output = subprocess.check_output(['lsof', '-n', "-i4TCP:%s" % port])
except subprocess.CalledProcessError:
    print("No process listening on port %s" % port)
else:
    listening = None

    for line in output.splitlines():
        if "LISTEN" in line:
            listening = line
            break

    if listening:
        # PID is the second column in the output
        pid = int(listening.split()[1])
        os.kill(pid, 9)
        print("Killed process %s" % pid)
    else:
        print("No process listening on port %s" % port)
"""