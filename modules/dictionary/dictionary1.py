#! /usr/bin/env python
# -*- coding: utf-8 -*-
# English Malayalam Dictionary
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in


import os
import pickle
class Dictionary():
	
	def lookup_en_ml(self, key):
		self.dictFile="data/dict.dat"
		pickled_dict=open(self.dictFile,'r')
		self.dictionary=pickle.load(pickled_dict)
		meaning=""
		if self.dictionary.has_key(key):
			meaningList=self.dictionary[key]
			for meaning in meaningList:
				meaning=meaning+meaning.strip()	+"\n"
		else :
			meaning="No Meaning found"
		return meaning.decode('utf-8')
	def process(self,form):
		response = """
		<h2>English Malayalam Dictionary</h2></hr>
		<p>Enter the word to lookup in the dictionary
		</p>
		<form action="" method="post">
		<input type="text" value="%s" name="search_key"/>
		<input  type="submit" id="Find_Meaning" value="Find Meaning"  name="action" style="width:12em;"/>
		</br>
		</form>
		"""
		if(form.has_key('search_key')):
			search_key = form['search_key'].value.decode('utf-8')
			response=response % search_key
			response = response+"<h2>Search Results</h2></hr>"
			if(search_key==None):
				response = response+ "Enter a word to find meaning."
			else:		
				response = response+ self.lookup_en_ml(search_key)
		else:
			response=response % ""	
		return response
	def get_module_name(self):
		return "English Malayalam Dictionary"
	def get_info(self):
		return 	"English Malayalam Dictionary. Dictionary is compiled by Kerala state IT Mission"	
		
def getInstance():
	return Dictionary()
if __name__ == "__main__":
	d = Dictionary()
	response = "<h2>Search Results</h2></hr>"
	response = response+ d.lookup_en_ml(u"help")
	print response.encode('utf-8')
	
