import glob
import dendropy
import sys
import re

dph_default = 'PRSET Symdirihyperpr = fixed(inifinity);'
dph_uniform = 'PRSET Symdirihyperpr = fixed(1);'
dph_smooth = 'PRSET Symdirihyperpr = exp(1.0);'
auto_close = 'SET autoclose=yes;'


def parse_nexus(source_nexus):
	'''small function to take an input of a directory of nexus files and parse them into a file'''
	for file in glob.glob( os.path.join(source_nexus, '*.nex') ):
		with open(file) as f:
			data_set = [line for line in f]
			data_set_list.append(data_set)
	return(data_set_list)

def assemble_nexus(dph_default,dph_uniform, dph_smooth, auto_close):
	data_set_list = parse_nexus(sys.argv[1])
	pattern = re.compile(r' (ord.+?);', flags=re.DOTALL|re.IGNORECASE|re.MULTILINE)

	for data_set in data_set_list:
		for line in data_set:
			logfile = 'LOG START filename=%s' % data_set
			b = pattern.findall(line)
			if len(b) > 0:
				b = ( " ".join( repr(entry) for entry in b ) )
				print b
				
				

		
assemble_nexus(dph_default,dph_uniform, dph_smooth, auto_close)
	
