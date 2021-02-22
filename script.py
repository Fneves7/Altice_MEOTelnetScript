import getpass
import telnetlib

host = "192.168.1.254" #host address, change it
user = input("Username: ")
password = getpass.getpass()
tn = telnetlib.Telnet(host)

#read the output terminal until the word login shows up on console
tn.read_until(b"Login: ")
tn.write(user.encode('ascii') + b"\n")
#verification condition logic
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#commands
tn.write(b"lan/dhcp/show\n")
tn.write(b"quit\n")

#print the results
print(tn.read_all().decode('ascii'))