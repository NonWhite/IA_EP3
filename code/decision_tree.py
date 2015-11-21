import sys
import sklearn
from classifier_utils import *
from sklearn.tree import DecisionTreeClassifier as dtc

if __name__ == '__main__' :
	if len( sys.argv ) > 3 :
		infilepath , crit , depth = sys.argv[ 1: ]
		data = import_csv( infilepath )
		cf = dtc( criterion = crit , max_depth = int( depth ) )
		stats = cross_validation( data , cf )
		print "PARAMS: criterion=%s , max_depth=%s" % ( crit, depth )
		print_stats( stats )
	else :
		print "Usage python %s [csv_file] [neighbors] [distance]" % sys.argv[ 0 ]
