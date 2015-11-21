from copy import deepcopy as copy

''' DEFAULT FILE PATHS '''
DEFAULT_DATASET = '../data/sms_spam.txt'
DEFAULT_OUTFILE = '../data/%s.csv'

SPACE_CHAR = ' '
EMPTY_CHAR = ''
A_CHAR = 'a'

SPACE_REPLACEABLE = [ '.' , '?' , '!' , ':' , ';' , '-' , '(' , ')' , '[' , ']' , '...' , '/' , ',' , '&' , '>' , '<' , '*' , '_' , '=' , '|' , '\xc2\xa1' , '\xc2\xac' , '+' , '~' , '\xe2\x80\x93' ]
EMPTY_REPLACEABLE = [ '#' , '\xc3\xa9' , '\xcb\x86' , '\xc2\xa5' , '\xe2\x80\x9d' , '\xc2\xbe' , '\xe2\x80\x99' , '\xe2\x82\xac' , '\xcb\x9c' , "\"" , "'" , '\xc2\xa8' , '\xe2\x80\x9c' , '\\' , '%' , '$' , '\xe2\x80\x98' , '\xe2\x80\xb0' , '\xc2\xa9' , '^' , '\xe2\x84\xa2' , '\xc5\x93' , '\xc2\xa3' ]
A_REPLACEABLE = [ '\xc3\xa3' , '\xc3\x83' ]

def get_replacement( char ) :
	if char in SPACE_REPLACEABLE : return SPACE_CHAR
	elif char in EMPTY_REPLACEABLE : return EMPTY_CHAR
	elif char in A_REPLACEABLE : return A_CHAR

def remove_punctuation( cad ) :
	for p in PUNCTUATION : cad = cad.replace( p , get_replacement( p ) )
	return cad

def has_numbers( cad ) :
	if cad.isdigit() : return True
	for ch in cad :
		if ch.isdigit() : return True
	return False

def is_url( cad ) :
	return cad.find( 'www' ) >= 0

def is_email( cad ) :
	return cad.find( '@' ) >= 0

def get_equivalent( word ) :
	if word in EQUIV : return EQUIV[ word ]
	return [ word ]

def is_stop_word( word ) :
	return word in STOP_WORDS

def read_equivalent_words() :
	eq = {}
	with open( '../data/equivalents.txt' , 'r' ) as f :
		for line in f :
			space_pos = line[ :-1 ].find( ' ' )
			key = line[ :space_pos ]
			rep = line[ space_pos+1:-1 ].split()
			#if len( rep ) == 1 : rep = [ rep ]
			eq[ key ] = rep
	return eq

def read_stop_words() :
	lst = []
	with open( '../data/stop_words.txt' , 'r' ) as f :
		for line in f :
			lst.append( line[ :-1 ] )
	return lst

''' PARSER CONSTANTS '''
PUNCTUATION = SPACE_REPLACEABLE + EMPTY_REPLACEABLE + A_REPLACEABLE
EQUIV = read_equivalent_words()
EQUIV = read_equivalent_words()
STOP_WORDS = read_stop_words()
