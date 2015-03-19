import glob
import dendropy
import sys
import re
import os

source_nexus = sys.argv[1]

def parse_nexus(source_nexus):
	'''small function to take an input of a directory of nexus files and parse them into a file'''
	data_set_list = []
	path_list = []
	for file in glob.glob( os.path.join(source_nexus, '*.nex') ):
		with open(file) as f:
			data_set = [line for line in f]
			data_set_list.append(data_set)
			path_list.append(glob.glob( os.path.join(source_nexus, '*.nex')))
	return(data_set_list, path_list)

def assemble_nexus():
	data_set_list = parse_nexus(source_nexus)
	pattern = re.compile(r' (ord.+?);', flags=re.DOTALL|re.IGNORECASE|re.MULTILINE)
	for data_set in data_set_list:
		for line in data_set:
			logfile = 'LOG START filename=%s' % data_set
			b = pattern.findall(line)
			if len(b) > 0:
				b = ( " ".join( repr(entry) for entry in b ) )
				print b
				
def add_dtype():
	'''MrBayes expects to be told a data type. So let's tell it one.'''
	data_set_list = parse_nexus(source_nexus)
	data_set_list = data_set_list[:1]
	for data_set in data_set_list:	
		for data in data_set:
			for line in data:
				if line.startswith('        FORMAT '):
					line = line.split(' ')	
					line.insert(2, 'DATATYPE=standard')
	return(line)

def write_out(source_nexus):
	data_sets = add_dtype()
	path_list = parse_nexus(source_nexus)[1:]
	for list  in path_list:		
		for path in list:
			filename = '_dtype'.join(path)
			print filename
			with open (filename) as f:
				f.write(data_set)
	

		
write_out(source_nexus)
	
