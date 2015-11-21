import sys
import sklearn
from classifier_utils import *
from sklearn.neighbors import KNeighborsClassifier as knc

if __name__ == '__main__' :
	if len( sys.argv ) > 3 :
		infilepath , k , dist = sys.argv[ 1: ]
		data = import_csv( infilepath )
		cf = knc( n_neighbors = int( k ) , metric = dist )
		stats = cross_validation( data , cf )
		print "PARAMS: K=%s , metric=%s" % ( k , dist )
		print_stats( stats )
	else :
		print "Usage python %s [csv_file] [neighbors] [distance]" % sys.argv[ 0 ]
