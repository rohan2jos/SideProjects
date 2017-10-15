import socket
from pif import get_public_ip
from subprocess import call
from espeak import espeak
import os
from os import  system
import subprocess

class GetDetails():

    debug_file = ""

    def __init__(self):
        self.debug_file = open("debug_father.log", "w")
        self.debug_file.write("[debug] entered the constructor \n")

    def get_ip(self):
        self.debug_file.write("[debug] checking public ip \n")
        IP = get_public_ip()
        return IP

    def get_hostname(self):
        self.debug_file.write("[debug] checking hostname \n")
        return socket.gethostname()

    def get_fqdn(self):
        self.debug_file.write("[debug] checking fqdn \n")
        return socket.getfqdn()

    def get_local_ip(self):
        self.debug_file.write("[debug] checking local ip \n")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]

    def look_in_dir(self, dirname, filename):
        print "[debug] looking in directory"
        fl = False
        if dirname is '.':
            speechdirname = "this directory"
        else:
            speechdirname = dirname
        call(["espeak", "scanning"])

        for f in os.listdir(dirname):
            print f
            if f == filename:
                print "[debug] file found"
                call(["espeak", "found " + filename + " in given directory"])
                fl = True
                break

        if fl is False:
            print "[debug] file not found"
            call(["espeak", "file not found"])

    def ping_test(self):
        parameters = "-c 1"
        self.debug_file.write("ping " + parameters + " " + "www.google.com")
        return system("ping " + parameters + " " + "www.google.com") == 0

    def read_mem(self):
        memtotal = open('/proc/meminfo').readlines()[1]
        return memtotal

    def read_cores(self):
        corestotal = open('/proc/cpuinfo').readlines()

        for line in corestotal:
            if 'cpu cores' in line:
                print line
                break

    def get_disk_stats(self):
        cmd = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE)
        out_str = str(cmd.stdout)
        for line in cmd.stdout:
            temp_line_arr = line.split()
            print temp_line_arr
            print "end line"

gd = GetDetails()

'''
call(["espeak", "performing a health test"])

call(["espeak", "checking system connection to internet"])

pt = gd.ping_test()

if pt is True:
    call(["espeak", "systems are online"])
else:
    call(["espeak", "system cannot ping, seems offline"])






ip = gd.get_ip()
ip = "public address is " + ip

call(["espeak", ip])

hostname = gd.get_hostname()
hostname = "host name is" + hostname
fqdn = gd.get_fqdn()
print fqdn
localip = gd.get_local_ip()
print localip

speech = "here is the public address"
call (["espeak", hostname])


#tofind = raw_input("enter the name of the file that you want to find :: ")
#dirname = raw_input("enter the name of the directory (the default if nothing is entered is /  However, this will take longer) :: ")
#gd.look_in_dir(dirname, tofind)
memtotal = gd.read_mem()
mem = []
for d in memtotal.split():
    try:
        mem.append(float(d))
    except ValueError:
        pass

print mem
print int(mem[0])
inGb = int(mem[0]) / (1024 * 1024)
print inGb

call(["espeak", "free memory is " + str(inGb) + " gigabytes and the system looks good"])
'''

gd.read_cores()
gd.get_disk_stats()