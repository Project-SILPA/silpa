#! /usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
def getTemplate():
	return open(os.path.dirname(__file__)+"/../"+getTemplateName()).read()
def getTemplateName():
	return loadConfiguration()["SILPA_TEMPLATE"]	
def getCopyrightInfo():
	return loadConfiguration()["SILPA_SITE_COPYRIGHT"]		
def getModulesList():
	conf_dict=loadConfiguration()
	action_dict={}
	for item in conf_dict	:
		if(item.startswith("SILPA_ACTION.")):
			action_dict[item.replace("SILPA_ACTION.","")]=conf_dict[item]
	return 	action_dict	
def getStaticContent(page):
	try:
		return open(os.path.dirname(__file__)+"/../doc/"+page).read()
	except:
		return "Could not find the requested page "+	page
def handleStats():
	Hits="0"	
	try:
		InFile = open(os.path.dirname(__file__)+"/../count.dat", "r")	# Text file with total hits
		Hits = InFile.readline()
	except:
		pass	
	x = int(Hits) + 1
	h = str(x)
	OutFile = open(os.path.dirname(__file__)+"/../count.dat", "w")
	OutFile.write(str(x))
	OutFile.close()

def loadConfiguration():
	conf_dict={}
	conffile = codecs. open(os.path.dirname(__file__)+"/../silpa.conf",encoding='utf-8', errors='ignore')
	while 1:
		text = unicode( conffile.readline())
		if text == "":
			  break
		line = text.split("#")[0].strip()
		if(line == ""):
			  continue 
		try:	  
			lhs = line.split("=") [ 0 ]  
			rhs = line.split("=") [ 1 ]  
			conf_dict[lhs]=rhs
		except:
			pass	
	return conf_dict
if __name__ == '__main__':
	print getModulesList()	
