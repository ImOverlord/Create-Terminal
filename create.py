#! /usr/bin/env python3
#ImOverlord
import os
import sys

#create file_type file_name
chmod = 700
header = {
	"py": "#! /usr/bin/env python\n",
	"py3":"#! /usr/bin/env python3\n",
	"c":"/*\n** EPITECH PROJECT, 2017\n** file_name.c\n** File description:\n**	desc\n*/\n"
	}

def add_header(params, file_name):
	file = open(file_name, "w")
	file.write(header[params[1]])
	file.close()

def check_valid_params(params):
	if len(params) < 3:
		print("Invalid Number of parameters")
		exit()

def check_valid_type(params):
	if params[1] == "py3":
		file_type = "py"
	else:
		file_type = params[1]
	command = ''.join(["touch ", params[2], ".", file_type])
	os.system(command)
	file_name = ''.join([params[2],".", file_type])
	add_header(params, file_name)
	if file_type == "py":
		command = ''.join(["chmod ", str(chmod), " ", file_name])
		os.system(command)

check_valid_params(sys.argv)
check_valid_type(sys.argv)
