connect('weblogic','welcome1', 't3://localhost:7001')
print ''
print '======================================================'
print 'The script has been connected to the Admin Server'
print '======================================================'
print ''

srvName=raw_input('Please enter managed server name:')
#ipAddress=raw_input('Please enter the IP where the managed server will Listen for connections:')
port=input('Please enter the Port for the managed server:')

edit()
startEdit()
cd('/')
cmo.createServer(srvName)
cd('/Servers/' + srvName)
cmo.setListenAddress("")
cmo.setListenPort(port)
activate()
