#!/usr/bin/python
# -*- coding: utf-8 -*-
import gsm_um
import random 


########################################### CORRECT FUNCTIONS #########################################
def correctMobileID(p):
	#5220670380
	p.lengthMI=8;
	p.idDigit1=2;
	p.oddEven=1; p.typeOfId=1; 
	p.idDigit2_1=4; p.idDigit2=0; 
	p.idDigit3_1=4; p.idDigit3=0;
	p.idDigit4_1=2; p.idDigit4=5; 
	p.idDigit5_1=0; p.idDigit5=2;
	p.idDigit6_1=7; p.idDigit6=6;
	p.idDigit7_1=3; p.idDigit7=0;
	p.idDigit8_1=0; p.idDigit8=8;
	return p

def correctLocalAreaID(p):
	p.mccDigit1=0x2; 
	p.mccDigit2=0x0; 
	p.mccDigit3=0x4; 

	p.mncDigit1=0x0;
	p.mncDigit2=0x0; 
	p.mncDigit3=0x4;

	p.lac1=0x03; p.lac2=0xe9;
	return p

########################################## FUZZ FUNCTIONS #############################################
def mobileFillID(packet, permutation):
	length = len(permutation);

	current_packet_digit = 2;
	for i in range (0, length):

		currentHexDigit = int(permutation[i]);
		if(i % 2 == 0):
			exec "packet.idDigit%s = %d " % (current_packet_digit, currentHexDigit)
		else:
			exec "packet.idDigit%s_1 = %d " % (current_packet_digit, currentHexDigit)
			current_packet_digit = current_packet_digit + 1;

	return packet

def fuzzMobileId(p, typeOfId, lengthField, permutation):

	# Settings
	p.lengthMI=lengthField;
	p.idDigit1=2;
	p.oddEven=1;
	p.typeOfId=typeOfId;

	# digits start with length of packet p
	p = mobileFillID(p, permutation);

	return p

########################################### FIELD SELECTOR ############################################

def fuzzingLengthFields(field, function, typeOfId, lengthField, permutation):
	# Default backup value: Identity request
	p = '\x05\x18\x01';

	if(field == 1):
		if(function == 1):
			p = gsm_um.tmsiReallocationCommand();
			p = fuzzMobileId(p, typeOfId, lengthField, permutation);
			p = correctLocalAreaID(p);
			return p
		elif(function == 2):
			p = gsm_um.imsiDetachIndication();
			p = fuzzMobileId(p, typeOfId, lengthField, permutation);
			return p
		elif(function == 3):
			p = gsm_um.attachAccept();
			p = fuzzMobileId(p, typeOfId, lengthField, permutation);
			return p
		elif(function == 4):
			p = gsm_um.ptmsiReallocationCommand();
			p = fuzzMobileId(p, typeOfId, lengthField, permutation);
			return p
	return p