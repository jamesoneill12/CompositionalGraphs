from networkx.readwrite import json_graph
from  src.graph.ngram_graph.bigram_graph import *
from src.graph.lexical_graph.wordnet.wordnet_graph import wordnetGraph

filename = "C:/Users/1/James/grctc/GRCTC_Project/Classification/Data/docs/"
wg = wordnetGraph(filename)

#syn, anto = wg.get_corpus_syns(antonyms=True)
#print (syn)

wg.create_wordnetDocGraph(save_pic=True)
