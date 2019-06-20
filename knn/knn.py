import matplotlib.pyplot as plt
import numpy as np
import operator as opt
from sklearn.datasets import load_iris

def createDataSet():
    # 创建训练集
    iris = load_iris()
    group = iris.data
    labels = iris.target
    feature_names = iris.feature_names
    labels_names = iris.target_names
    features = iris.data.T
    return features,feature_names,group, labels,labels_names
	
def kNN(testData,dataSet,labels, k):
    #计算欧式距离
    distSquareMat = np.square(dataSet - testData)#计算差值并平方
    distSquareSums = distSquareMat.sum(axis=1)#跨列求和
    distances = np.sqrt(distSquareSums)#根号计算
    sortedIndices = distances.argsort()#索引排序
    indices = sortedIndices[:k]#取前k
    classCount = {}#记录出现次数
    for i in indices:
        label = labels[i]
        classCount[label] = classCount.get(label, 0) + 1
    sortedCount = sorted(classCount.items(), key=opt.itemgetter(1), reverse=True)#字典排序
    return sortedCount[0][0]

def Visual(features, feature_names, labels):
    plt.scatter(features[0],features[1],alpha=0.2,s=100*features[3],c=labels)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.show()

if __name__ == '__main__':
    features,feature_names,group,labels,labels_names = createDataSet()
    newInput = np.array([4,5,7,1])
    Visual(features, feature_names, labels)
    k = kNN(newInput,group,labels,5)
    print(labels_names[k])


