import math
from copy import copy
from sklearn.cross_validation import cross_val_score

def import_csv( filepath , has_header = True ) :
	csv_data = []
	with open( filepath , 'r' ) as f :
		p = lambda x : int( x ) if float( x ) == math.trunc( float( x ) ) else float( x )
		for line in f :
			if has_header :
				has_header = False
				continue
			sp = line[ :-1 ].split( ',' )
			numbers = sp[ :-1 ]
			sp = [ p( x ) for x in numbers ] + [ sp[ -1 ] ]
			csv_data.append( sp )
	return csv_data

def cross_validation( data , classifier , num_folds = 10 ) :
	stats = {}
	typeof = lambda x : 1 if x == 'spam' else 0
	X = [ row[ :-1 ] for row in data ]
	y = [ typeof( row[ -1 ] ) for row in data ]
	scores = [ 'precision' , 'recall' , 'f1' , 'mean_absolute_error' , 'mean_squared_error' ]
	for sc in scores :
		stats[ sc ] = cross_val_score( classifier , X , y , cv = num_folds , scoring = sc )
	return stats

def print_stats( stats ) :
	for k in stats :
		print "%s = %s +/- %s" % ( k.upper() , stats[ k ].mean() , stats[ k ].std() )
