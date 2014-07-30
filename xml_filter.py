#!/usr/bin/env python
#Small script to filter xml files [metadata] to increase independance of data#
#           																 #				           
#call as: python xml_filter.py dir_of_xml directory_for_parents dir_for_sibs #
# Example: python choose_nexus.py ./my_xmlfiles ./parents ./siblings         #
#    Copyright April Wright, 2014                                            #
#    wright.aprilm@gmail.com                                                 #
#                                                                            #
#  This program is free software; you can redistribute it and/or modify      #
#  it under the terms of the GNU General Public License as published by      #            
#  the Free Software Foundation; either version 3 of the License, or         #
#  (at your option) any later version.                                       #
#                                                                            #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#  GNU General Public License for more details.                              #
#                                                                            #
#  You should have received a copy of the GNU General Public License along   #
#  with this program. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                            #
##############################################################################

from xml.dom.minidom import parse, parseString
import os
import shutil
import sys

def find_xml(dirname):
	'''Find all candidate xml files'''
	flist = []
	for file in os.listdir(dirname):
    		if file.endswith('xml'):
        		flist.append(file)
	return(flist)

def find_parents(dirname,parent_dir):
	'''Find any datasets which are parents of others. Abandon them'''
	flist = find_xml(dirname)
	for file in flist:
		xmldoc = parse('%s/%s' % (dirname,file))
		if xmldoc.getElementsByTagName('Parent')[0].firstChild is None:
			shutil.move('%s/%s' % (dirname, file), '%s/%s' % (parent_dir, file))
	return(parent_dir)

def find_sibs(dirname,parent_dir,sib_dir):
		'''Find any siblings. You will have to manually decide how to deal 
		with these'''
		flist = find_xml(parent_dir)
		for file in flist:
				print file
				xmldoc = parse('%s/%s' % (parent_dir,file))
				if xmldoc.getElementsByTagName('Sibling')[0].firstChild is None:
					pass
				else:
					shutil.move('%s/%s' % (parent_dir,file), '%s/%s' % (parent_dir, file))
		return(flist)

find_sibs(sys.argv[1],sys.argv[2],sys.argv[3])

