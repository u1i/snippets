from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('somehost.com', port=9122, username='me', password='passwd891')

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

#scp.put('test.txt', 'test2.txt')

scp.put('test.txt', remote_path='/tmp/test.txt')

scp.close()
