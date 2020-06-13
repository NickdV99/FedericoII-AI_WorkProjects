import treepredict as tp
import pandas as pd


mydata = tp.load_dataset('agaricus-lepiota.data')
#mydata = pd.read_csv('agaricus-lepiota.data') pandas load data in a different from tp.load_dataset

print (mydata)
#mydata = pd.read_csv('agaricus-lepiota.data')

#set1, set2 = tp.divideset(mydata,10,'e')

#print tp.uniquecounts(mydata)

#print tp.entropy(mydata)

#print tp.entropy(set1)
#print tp.entropy(set2)

#costruito a cazzo di cane perche buildtree itera sulle prime n-1 colonne,
# ma in questo cazzo di dataset il target si trova sulla prima colonna
tree = tp.buildtree(mydata)

tp.drawtree(tree,jpeg= 'mushrooms.jpg')

print (tp.mdclassify(['x','y','y','t','a','f','c','b','n','e','c','s','s','w','w','p','w','o','p','k','s','m'], tree))

#i risultati sono sballati e non veritieri ma questa e' la logica