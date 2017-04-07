from sklearn import tree


# features = [[0,0,1],[0,0,2],[0,0,3],[0,0,4],[0,0,5],     [0,1,0],[0,2,0],[0,3,0],[0,4,0],[0,5,0],        [1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0]]

features = [[1],[1],[1],[1],[1],    [2],[2],[2],[2],[2],    [3],[3],[3],[3],[3]]
labels = ['green', 'green','green','green','green',      'blue','blue','blue','blue','blue',             'red','red','red','red','red']

my_tree = tree.DecisionTreeClassifier()
my_tree.fit(features,labels)
print my_tree.predict([[4]])
