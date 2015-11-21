import os
import signal
import time
from subprocess import Popen

''' K-NEAREST NEIGHBORS '''
distance = [ 'manhattan' , 'euclidean' , 'hamming' ]
k_nearest = [ 1 , 25 , 50 ]
NEAREST = 'python ../code/nearest_neighbors.py %s %s %s'
near_out_file = '../results/knear.txt'

''' DECISION TREE '''
criterion = [ 'gini' , 'entropy' ]
depth = [ 10 , 50 , 100 ]
DECISION = 'python ../code/decision_tree.py %s %s %s'
decision_out_file = '../results/decision.txt'

''' NAIVE BAYES '''
NAIVE = 'python ../code/naive_bayes.py %s %s'
alpha = [ 1 , 10 , 100 ]
naive_out_file = '../results/naive.txt'

''' GENERAL '''
datasets = [ '../data/term_freq_train.csv' , '../data/tf_idf_train.csv' ]
TIMEOUT = 1800

def timeout_command( command , timeout , outfile ) :
	start = time.time()
	process = Popen( command , stdout = outfile )
	while process.poll() is None :
		time.sleep( 0.1 )
		now = time.time()
		if now - start > timeout :
			os.kill( process.pid , signal.SIGKILL )
			os.waitpid( -1 , os.WNOHANG )

if __name__ == "__main__" :
	''' DECISION TREE '''
	for data in datasets :
		for crit in criterion :
			for d in depth :
				inst = ( DECISION % ( data , crit , d ) ).split()
				print "PROCESSING %s" % inst
				with open( decision_out_file , 'a' ) as f :
					timeout_command( inst , TIMEOUT , f )
	
	''' NAIVE BAYES '''
	for data in datasets :
		for alp in alpha :
			inst = ( NAIVE % ( data , alp ) ).split()
			print "PROCESSING %s" % inst
			with open( naive_out_file , 'a' ) as f :
				timeout_command( inst , TIMEOUT , f )
				
	''' K-NEAREST NEIGHBORS '''
	for data in datasets :
		for dist in distance :
			for k in k_nearest :
				inst = ( NEAREST % ( data , k , dist ) ).split()
				print "PROCESSING %s" % inst
				with open( near_out_file , 'a' ) as f :
					timeout_command( inst , TIMEOUT , f )
