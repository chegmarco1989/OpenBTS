#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import time
import binascii
import os
from libmich.formats import *
import gsm_um
import simple_fuzzer_def as fuzzer
from adb import ADB
import itertools
from math import factorial

# Fill in current mobile device

if len(sys.argv) > 2:
    device = sys.argv[1];
    imsi = sys.argv[2];
else:
	print("ERROR: Device name not found.")
	print("Call the script with: ./simple_fuzzer #DEVICE #IMSI");
	print("Where #DEVICE is the name and #IMSI is the IMSI of the mobile device.");
	sys.exit(0);


############################################### SETTINGS #############################################
# Default OpenBTS port
TESTCALL_PORT = 28670;
adb = ADB();

date = str(time.strftime("%Y%m%d-%H%M%S"));
location_prefix = "logs/logs_packets/simple_fuzzer/";

log_packets_title = location_prefix + device + "_log_" + date + ".txt";

# Fuzzer settings
currentLength = 2;
maxLength = 200;

# The amount of runs
maxRun = 1000;

# Select specific field and function
# Detailed list in simple_fuzzer_def.py
packet_field = 1;
packet_function = 1;

# Turn on/off prints
verbose = True;

# Creat socket
tcsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcsock.settimeout(6)

################################################# LOG ################################################
def saveRadioLog(adb,title):
	adb.logcatRadio(title);
	return

def saveLogcat(adb,title):
	adb.logcat(title);
	return

def clearLogs():
	adb.logcatRadioClear();
	adb.logcatClear();
	return

def log_adb(adb, packet_field, packet_function, maxLength, maxRun):
	log_directory = "logs/logs_adb/";
	log_title = "field_" + str(packet_field) 
	+ "_function_" + str(packet_function) 
	+ str(time.strftime("%Y%m%d-%H%M%S")) 
	+ "_length_" + str(maxLength) 
	+ "_runs_" + str(maxRun) +"x_";
	
	saveRadioLog(adb, log_directory + log_title);
	saveLogcat(adb, log_directory + log_title);
	clearLogs();

def log_packets(length, counter, packet, parsed_packet, reply, parsed_reply):
	with open(log_packets_title, "a") as myfile:
		myfile.write("-------------------------------------------------------------------------------\n"
			+ "INPUT - Length: " + str(length) + " Counter: " + str(counter) + "\n" 
			+ str(packet).encode("hex") + "\n" 
			+ parsed_packet + "\n\n"
			+ "OUTPUT - Length: " + str(length) + " Counter: " + str(counter) + "\n"
			+ str(reply).encode("hex") + "\n"
			+ parsed_reply + "\n\n");

def log_restart():
	with open(log_packets_title, "a") as myfile:
		myfile.write("\n\nCHANNEL RESTART \n \n");

############################################## CHANNEL ###############################################
# Send a restart to OpenBTS to establish a new channel
def establishNewChannel():
   restart = "RESTART";
   tcsock.sendto(restart, ('127.0.0.1', TESTCALL_PORT));
   # Log when the channel restars
   log_restart();
   time.sleep(6);
   return

def send(tcsock, packet, length, counter):
		try:
			tcsock.sendto(packet, ('127.0.0.1', TESTCALL_PORT))
			reply = tcsock.recv(1024)
		except socket.timeout:
			print "socket.timeout: Mobile device is not responding";
			establishNewChannel();
			return False

		#Libmich parses the input and output
		parsed_packet = repr(L3Mobile.parse_L3(packet));
		parsed_reply = repr(L3Mobile.parse_L3(reply));

		# Can the reply be parsed by Libmich?
		if "ERROR" not in parsed_reply:
			print "Received packet: ", str(reply).encode("hex") + "\n";
			print "GSM_UM interpetation: " + '\n' + parsed_reply + "\n\n";
		# Create a new channel if a incorrect package has been send by the mobile device.
		else:
			establishNewChannel();
			return False

		log_packets(length, counter, packet, parsed_packet, reply, parsed_reply);
		return True

############################################### UTILS ################################################
def printPacket(packet, length, permsCurrent, permutation, prefix):
		print('------------------------------- INPUT  -------------------------------' + '\n');
		print('Current permutation: ' + str(permsCurrent));
		print('Current hexvalue: ' + permutation.encode("hex"));
		# Fuzzing counter
		print "Current hexbytes: ", length;

		# Make the packet readable
		printable = str(packet).encode("hex");
		print "Current complete packet: " + printable + '\n';

		# Decode printable hex to make it usable for L3Mobile.
		# Adding the \x for the bytes.
		l3msg = printable.decode('hex');
		l3msg_input = repr(L3Mobile.parse_L3(l3msg));

		print "GSM_UM interpetation: \n " + l3msg_input + '\n\n';
		print "------------------------------- OUTPUT -------------------------------" + '\n';

def convert(int_value):
   encoded = format(int_value, '02x')

   length = len(encoded)
   encoded = encoded.zfill(length+length%2)

   return encoded.decode('hex')  

########################################### SIMPLE FUZZER ############################################
# Fuzzer specific settings

# From current length till end
currentLength = 0;
maxLength = 2;

# Select specific field and function
# Detailed list in simple_fuzzer_def.py
packet_field = 1;
packet_function = 5;

# Turn on/off prints
verbose = True;

while currentLength <= maxLength:

	# Get and store the magic bytes for a specific function
	packet = fuzzer.fuzzingLengthFields(packet_field, packet_function);
	prefix = packet;

	# Limits for permutations
	permsCurrent = 0;
	permsEnd = 16 ** currentLength;

	if not verbose:
		print('Current length: ' + str(currentLength));

	while permsCurrent < permsEnd:
		# Convert permutation to hexadecimal
		permutation = convert(permsCurrent);
		# Create the packet using the prefix and converted permutation
		packet = prefix + permutation;
		if(verbose):
			printPacket(packet, currentLength, permsCurrent, permutation, prefix);

		# Send packet to the mobile device.
		result = send(tcsock, packet, currentLength, permsCurrent);

		if(result):
			permsCurrent = permsCurrent + 1;
		# else:
		# 	# do some error handling / restart channel.
		# 	permsCurrent = permsCurrent;

	# Hexadecimal value, so to keep length consistent with actualoutput, + 2 is added.
	currentLength = currentLength + 2;

# Save the radio log from mobile device
#log(adb, packet_field, packet_function, maxLength, maxRun);