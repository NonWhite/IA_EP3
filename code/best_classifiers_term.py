import sys
import sklearn
from classifier_utils import *
from sklearn.naive_bayes import MultinomialNB as mnb
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.neighbors import KNeighborsClassifier as knc
from sklearn.metrics import classification_report as report

def classify( model , train_data , test_data , model_name ) :
	print "Testing with %s" % model_name
	X = [ row[ :-1 ] for row in train_data ]
	y = [ row[ -1 ] for row in train_data ]
	model.fit( X , y )

	X_test = [ row[ :-1 ] for row in test_data ]
	y_real = [ row[ -1 ] for row in test_data ]
	y_pred = model.predict( X_test )
	print report( y_real , y_pred )

if __name__ == '__main__' :
	if len( sys.argv ) > 2 :
		train_fpath , test_fpath = sys.argv[ 1: ]
		train_data = import_csv( train_fpath )
		test_data = import_csv( test_fpath )
		''' DECISION TREE '''
		cf = dtc( criterion = 'entropy' , max_depth = 100 )
		classify( cf , train_data , test_data , 'decision_tree' )
		
		''' NEAREST NEIGHBORS '''
		cf = knc( n_neighbors = 1 , metric = 'euclidean' )
		classify( cf , train_data , test_data , 'knearest_neighbors' )
		
		''' NAIVE BAYES '''
		cf = mnb( alpha = 1.0 )
		classify( cf , train_data , test_data , 'naive_bayes' )
	else :
		print "Usage python %s [train_csv_file] [test_csv_file]" % sys.argv[ 0 ]
