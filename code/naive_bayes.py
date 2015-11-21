import sys
import sklearn
from classifier_utils import *
from sklearn.naive_bayes import MultinomialNB as mnb

if __name__ == '__main__' :
	if len( sys.argv ) > 2 :
		infilepath , alp = sys.argv[ 1: ]
		data = import_csv( infilepath )
		cf = mnb( alpha = float( alp ) )
		stats = cross_validation( data , cf )
		print "PARAMS: alpha=%s" % alp
		print_stats( stats )
	else :
		print "Usage python %s [csv_file] [neighbors] [distance]" % sys.argv[ 0 ]
