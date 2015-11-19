import sys
from utils import *
from math import log

def update( dict_words , lst_words ) :
	for k in lst_words :
		if k not in dict_words : dict_words[ k ] = 0
		dict_words[ k ] += 1

def get_words( cad ) :
	cad = cad.split()
	words = []
	for w in cad :
		if has_numbers( w ) : continue
		if is_url( w ) : continue
		if is_email( w ) : continue
		w = remove_punctuation( w ).strip()
		if len( w ) == 0 :
			continue
		else : 
			w = w.split()
			for sw in w : words.append( sw )
	return words

def parse_line( line ) :
	class_pos = line.find( ',' )
	class_value = line[ :class_pos ]
	line = line[ (class_pos + 1 ): ].lower() # TO LOWER CASE
	divs = line.split()
	dict_words = {}
	for block in divs :
		lst = get_words( block )
		update( dict_words , lst )
	row = ( class_value , dict_words )
	return row

def delete_stop_words( dictionary ) :
	return dictionary

def to_csv_format( data , dictionary ) :
	header = [ w for w in dictionary ]
	header.append( 'email_type' )
	print "NUM WORDS = %s" % len( dictionary )
	print "NUM ROWS = %s" % len( data )
	csv_data = []
	csv_data.append( header )
	for ( email_type , row ) in data :
		csv_row = []
		for h in header[ :-1 ] :
			if h in row : csv_row.append( row[ h ] )
			else : csv_row.append( 0 )
		csv_row.append( email_type )
		csv_data.append( csv_row )
	return csv_data

def to_term_freq_vector( infile , has_header = True ) :
	data = []
	dictionary = []
	with open( infile , 'r' ) as f :
		first = True
		for line in f :
			row = parse_line( line[ :-1 ] )
			if has_header and first :
				first = False
				continue
			data.append( row )
			words = [ w for w in row[ 1 ].keys() if w not in dictionary ]
			dictionary.extend( words )
	dictionary = delete_stop_words( dictionary )
	return to_csv_format( data , dictionary )

def to_tf_idf_vector( infile , has_header = True ) :
	data = []
	dictionary = []
	doc_freq = {}
	with open( infile , 'r' ) as f :
		first = True
		for line in f :
			row = parse_line( line[ :-1 ] )
			if has_header and first :
				first = False
				continue
			data.append( row )
			words = [ w for w in row[ 1 ].keys() if w not in dictionary ]
			dictionary.extend( words )
			for k in row[ 1 ].keys() :
				if k not in doc_freq : doc_freq[ k ] = 0
				doc_freq[ k ] += 1
	tf_idf_data = []
	N = len( data )
	for ( email_type , words ) in data :
		tf_idf_row = ( email_type , {} )
		for k in words :
			tf_idf_row[ 1 ][ k ] = words[ k ] * log( N / doc_freq[ k ] )
		tf_idf_data.append( tf_idf_row )
	dictionary = delete_stop_words( dictionary )
	return to_csv_format( tf_idf_data , dictionary )

def export( data , outfile ) :
	print "Exporting data to %s" % outfile
	with open( outfile , 'w' ) as f :
		for csv_row in data :
			csv_row = [ str( v ) for v in csv_row ]
			f.write( "%s\n" % ','.join( csv_row ) )

if __name__ == "__main__" :
	infile = DEFAULT_DATASET
	if len( sys.argv ) > 1 : infile = sys.argv[ 1 ]

	parsed_data = to_term_freq_vector( infile )
	export( parsed_data , DEFAULT_OUTFILE % 'term_freq' )

	parsed_data = to_tf_idf_vector( infile )
	export( parsed_data , DEFAULT_OUTFILE % 'tf_idf' )
