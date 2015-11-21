import os
import sys
import statistics
import numpy as np
from math import *
from pylab import *
from os.path import *
from copy import deepcopy as copy

# TODO: Change to term_freq and tf_idf files
RESULTS_DIR = '../results/'
IMAGES_DIR = '../doc/images/'
datasets = [ 'decision_term_freq' , 'decision_tf_idf' , 'naive_term_freq' , 'naive_tf_idf' , 'knear' ]
colors = [ 'red' , 'green' , 'blue' , 'magenta' , 'cyan' , 'black' , 'white' , 'purple' ]
metrics = [ 'precision' , 'recall' , 'f1' ]

def read_content( fpath ) :
	data = []
	with open( fpath , 'r' ) as f :
		exp = None
		for line in f :
			if line.startswith( 'PARAMS' ) :
				if exp : data.append( copy( exp ) )
				exp = { 'params' : [] }
				sp = line[ :-1 ].split( 'PARAMS: ' )[ 1 ].split( ' , ' )
				for k in sp :
					rt = k.split( '=' )
					exp[ 'params' ].append( rt )
			elif line.startswith( 'PRECISION' ) :
				exp[ 'precision' ] = line[ :-1 ].split( ' = ' )[ 1 ].split( ' +/- ' )
				exp[ 'precision' ] = [ float( v ) for v in exp[ 'precision' ] ]
			elif line.startswith( 'RECALL' ) :
				exp[ 'recall' ] = line[ :-1 ].split( ' = ' )[ 1 ].split( ' +/- ' )
				exp[ 'recall' ] = [ float( v ) for v in exp[ 'recall' ] ]
			elif line.startswith( 'F1' ) :
				exp[ 'f1' ] = line[ :-1 ].split( ' = ' )[ 1 ].split( ' +/- ' )
				exp[ 'f1' ] = [ float( v ) for v in exp[ 'f1' ] ]
			elif line.startswith( 'MEAN_ABS' ) :
				exp[ 'mean_absolute_error' ] = line[:-1].split( ' = ' )[ 1 ].split( ' +/- ' )
				exp[ 'mean_absolute_error' ] = [ float( v ) for v in exp[ 'mean_absolute_error' ] ]
			elif line.startswith( 'MEAN_SQR' ) :
				exp[ 'mean_squared_error' ] = line[:-1].split( ' = ' )[ 1 ].split( ' +/- ' )
				exp[ 'mean_squared_error' ] = [ float( v ) for v in exp[ 'mean_squared_error' ] ]
		if exp : data.append( copy( exp ) )
	return data

def get_label( params ) :
	label = ', '.join( [ '='.join( k ) for k in params ] )
	return label

def makePlot( directory , dataname ) :
	print ' ================================ %s =============================== ' % dataname.upper()
	fpath = "%s%s.txt" % ( directory , dataname )
	experiment_data = read_content( fpath )
	num_data = len( experiment_data )
	#for data in experiment_data : print data

	bar_width = 0.2
	opacity = 0.4
	error_config = { 'ecolor': '0.3' }
	num_groups = len( metrics )

	index = np.arange( 0 , num_data * bar_width * num_groups , ( num_data + 1 ) * bar_width )
	cont = 0
	for data in experiment_data :
		row = [ data[ m ][ 0 ] for m in metrics ]
		bar( index + cont * bar_width , row , bar_width , alpha = opacity , color = colors[ cont ] , label = get_label( data[ 'params' ] ) )
		cont += 1
	
	xlabel( 'Metric' )
	ylabel( 'Percentages' )
	xticks( index + bar_width , tuple( [ m.upper() for m in metrics ] ) )
	legend( loc = 'lower right' )

	tight_layout()

	savefig( "%s%s" % ( IMAGES_DIR , dataname ) )
	#show()
	clf()

if __name__ == "__main__":
	directory = RESULTS_DIR
	if len( sys.argv ) > 1 : datasets = sys.argv[ 1: ]
	for d in datasets :
		makePlot( directory , d )