import treepredict as tp

if __name__ == '__main__':

    print("ESERCIZIO SU IRIS DATASET\n")

    train_data=[]
    test_data=[]

    mydata = tp.aprifile("iris.txt")

    train_data, test_data = tp.createdataset2(mydata, 60, [])


    print("TRAIN DATA : \n")

    print(train_data,"\n")


    print("TEST DATA: \n")

    print(train_data)

    iris_tree = tp.buildtree(train_data)


    tp.drawtree(iris_tree, "iris_tree.jpeg")

    tp.fperformance(mydata)