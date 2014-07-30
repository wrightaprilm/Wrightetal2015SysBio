#!/usr/bin/env python
#Small script to compare filtered xml files [metadata] to nexus files 		 #
#[matrices]. 																 #			
#This script is meant to be run after xml_parsing.py and will find the actual# 
#nexus datasets that correspond to XML metadata.		             #					 #
#call as: python choose_nexus.py directory_for_results dir_of_nexus dir_of_xml#
# Example: python choose_nexus.py final_sets ./Nexus ./xml
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

import os
import sys
import shutil

def make_directory(dirname):
	'''make a directory to hold our results'''
	if not os.path.exists(dirname):
		os.makedirs(dirname)
	return(dirname)
	
def parse_and_pass(dirname,source_nexus,source_xml):
	make_dir = make_directory(dirname)	
	file_list = [file for file in os.listdir(source_nexus) if file.endswith('.nex')]
	xml_list = [file for file in os.listdir(source_xml) if file.endswith('.xml')]
	basenames = [os.path.basename(file)[:-4] for file in xml_list]
	nex_basenames = [os.path.basename(file)[:-4] for file in file_list]
	overlap_set = [file for file in nex_basenames if file in basenames]
	ending = '.nex'
	extension_files = [file+ending for file in overlap_set]
	for file in extension_files:
	    shutil.copy('%s/%s' % (source_nexus,file), './%s/%s' % (dirname,file))

parse_and_pass(sys.argv[1],sys.argv[2],sys.argv[3])
