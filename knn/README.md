<h1 id="-knn-">什么是KNN算法</h1>
<p>KNN算法是一种非常特别的机器学习算法，因为它没有一般意义上的学习过程。它的工作原理是利用训练数据对特征向量空间进行划分，并将划分结果作为最终算法模型。存在一个样本数据集合，也称作训练样本集，并且样本集中的每个数据都存在标签，即我们知道样本集中每一数据与所属分类的对应关系。</p>
<p>输入没有标签的数据后，将这个没有标签的数据的每个特征与样本集中的数据对应的特征进行比较，然后提取样本中特征最相近的数据（最近邻）的分类标签。</p>
<p>一般而言，我们只选择样本数据集中前k个最相似的数据，这就是KNN算法中K的由来，通常k是不大于20的整数。最后，选择k个最相似数据中出现次数最多的类别，作为新数据的分类。</p>
<h2 id="knn-">KNN算法实现</h2>
<p>导包<br>import numpy as np<br>用于矩阵的各种操作<br>import operator as opt<br>字典排序，也可以使用zip函数和匿名函数<br>from sklearn.datasets import load_iris<br>获取数据集</p>
<p>代码<br>这个实例返回的是鸢尾花的特征值</p>
<pre><code>def kNN(testData,dataSet,labels, k):
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
</code></pre><h3 id="-">实例化</h3>
<p>从sklearn数据库获取鸢尾花的数据，作为训练集，对新的无标签品种分类<br>完整代码</p>
<pre><code>import numpy as np
import operator as opt
from sklearn.datasets import load_iris

def createDataSet():
    # 创建训练集
    iris = load_iris()
    group = iris.data
    labels = iris.target
    labels_names = iris.target_names
    return group, labels,labels_names

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

if __name__ == &#39;__main__&#39;:
    group,labels,labels_names = createDataSet()
    newInput = np.array([4,5,7,1])
    k = kNN(newInput,group,labels,10)#返回的k值是特征值
    print(labels_names[k])
</code></pre><h3 id="-">可视化</h3>
<p>导包 import matplotlib.pyplot as plt<br>实现代码，实现泡泡图，加入鸢尾花的三个特征变量<br>之前的createDataSet函数增加features和features_name,分别是特征变量的转置和数据名称</p>
<pre><code>def Visual(features, feature_names, labels):
    plt.scatter(features[0],features[1],alpha=0.2,s=100*features[3],c=labels)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.show()
</code></pre><p>另外单纯实现散点图，以两个特征表示鸢尾花的分类情况，将绘画面板分为6份，对其分别定位和绘制，标签为手动输入，feature_names参数不需要传入</p>
<pre><code>def Visual(features, labels):
    plt.subplot(231)
    plt.scatter(features[0],features[1],alpha=0.2,c=labels)
    plt.title(&quot;sepal length and sepal width&quot;,fontsize=8)
    plt.subplot(232)
    plt.scatter(features[0],features[2],alpha=0.2,c=labels)
    plt.title(&quot;sepal length and patal length&quot;,fontsize=8)
    plt.subplot(233)
    plt.scatter(features[0],features[3],alpha=0.2,c=labels)
    plt.title(&quot;sepal length and petal width&quot;,fontsize=8)
    plt.subplot(234)
    plt.scatter(features[1],features[2],alpha=0.2,c=labels)
    plt.title(&quot;sepal width and petal length&quot;,fontsize=8)
    plt.subplot(235)
    plt.scatter(features[1],features[3],alpha=0.2,c=labels)
    plt.title(&quot;sepal width and petal width&quot;,fontsize=8)
    plt.subplot(236)
    plt.scatter(features[2],features[3],alpha=0.2,c=labels)
    plt.title(&quot;petal length and petal width&quot;,fontsize=8)
    plt.show()
</code></pre>
