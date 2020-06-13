import treepredict as tp

if __name__ == '__main__':

    print("ESERCIZIO SU MUSHROOMS DATASET\n")


    train_data=[]
    test_data=[]

    print("ALL DATASET:\n")
    mydata= tp.aprifile("mushrooms_final.txt")

    train_data, test_data = tp.createdataset2(mydata, 3250, [])

    print("TRAIN DATA : \n")

    print(train_data, "\n")

    print("TEST DATA: \n")

    print(train_data)

    mushrooms_tree = tp.buildtree(train_data)

    tp.drawtree(mushrooms_tree, "mushrooms_tree.jpeg")

    tp.fperformance(mydata)