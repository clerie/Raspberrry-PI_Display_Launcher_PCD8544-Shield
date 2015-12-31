import os

print '=Display Commander='
os.system('sudo python launcher/welcome.py')
print 'Type "quit" to exit.'
print ''

quit = 0

while quit == 0:
	cmd = raw_input("> ")

	if cmd == 'quit':
		quit = 1
	else:
		print''
		print '-'
		os.system('sudo python plugins/' + cmd + '.py')
		print '-'
		print ''
