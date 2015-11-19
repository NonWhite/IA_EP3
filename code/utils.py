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

''' PARSER CONSTANTS '''
PUNCTUATION = copy( SPACE_REPLACEABLE )
PUNCTUATION.extend( EMPTY_REPLACEABLE )
PUNCTUATION.extend( A_REPLACEABLE )

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
