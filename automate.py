from subprocess import call
file_name = raw_input(" Enter file name: ")
complete_file_name = "~/bin/"+file_name
command=''
while  command != 'e':
	command = raw_input (" Enter command: ")
	print "Enter e to exit"
	echo_argument = command + ' > ' + complete_file_name
	call(["echo", echo_argument])

