<h1 id="-">哲学家就餐问题</h1>
<h2 id="-">问题描述</h2>
<p>场景：5个哲学家，5把叉子，5盘意大利面（意大利面很滑，需要两把叉子才能拿起）大家围绕桌子，进行思考与进食的活到</p>
<p>哲学家的活动方式为：要么放下左右手刀叉进行思考，要么拿起刀叉开始吃饭（刀叉拿起时，必须拿两把，而且只能左右手依次拿，先左手拿左边，后右手拿右边，或者先右手拿右边，左边拿左边）。其只有这两种交替状态。</p>
<p>哲学家们面临的问题为：如何安排哲学家们一致的行动逻辑，保证他们至少有人且尽可能两个人能同时拿到两把叉子开始吃饭，而不会发生“死锁”，“饥饿”，“干等”的状态。需要注意的是，大家想吃饭的时机是随机的，想思考的时机也是随机的，这个不受控制，不可能由“你”来安排哲学家们哪几个先吃，哪几个后吃，他们不受你控制，但你要赋予他们一种性格，或者说思考方式，保证他们自主的思考，自主的解决问题。</p>
<h3 id="-">死锁模拟</h3>
<p>原理：死锁：大家都同时想吃饭，结果同时拿起左手边叉子，发现同时右边没有叉子，然后各怀私心，僵持者希望有人能放下他左手边叉子，然后抢夺之，开始吃意大利面，结果大家都没放。。。<br>导包</p>
<pre><code>import threading
from time import sleep
import random
</code></pre><p>创建Fork类，定义锁的获取和释放</p>
<pre><code>class Fork():
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()

    def pickup(self):
        self._lock.acquire()

    def putdown(self):
        self._lock.release()
</code></pre><p>创建哲学家类<br>继承threading.Thread类，定义哲学家以及左右刀叉，模拟拿起刀叉，进食，放下刀叉，思考行为<br>哲学家拿起左右刀叉的时候可以开始进食。最开始我是以两个哲学家进行模拟，认为更容易产生死锁，但是几乎不会停止。认为是哲学家思考的时间太长，导致思考的时间已经足够另外一个哲学家拿起刀叉开始进食，我将思考时间去掉，很快完成死锁，但并不符合常理，这种情况几乎成为单线循环，若另外一个线程开始，就会形成死锁。即便最后使用5个哲学家进行模拟，也改变不了单线循环，最后我将时间调到很小，大概5秒或者10秒就会形成死锁。</p>
<pre><code>class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index  
        self.leftFork = forks[self.index]
        self.rightFork = forks[(self.index + 1) % numForks]

    def run(self):
        while True:
            self.leftFork.pickup()
            self.rightFork.pickup()
            self.dining()
            self.rightFork.putdown()
            self.leftFork.putdown()
            self.thinking()

    def dining(self):
        print(&quot;Philosopher&quot;, self.index, &quot; starts to eat.&quot;)
        sleep(random.uniform(1,3)/1000)
        print(&quot;Philosopher&quot;, self.index, &quot; finishes eating and leaves to think.&quot;)

    def thinking(self):
        sleep(0.00000000000000000001)
</code></pre><p>主函数<br>创建叉子和哲学家实例，开启所有进程，捕捉异常并引发异常</p>
<pre><code>if __name__ == &#39;__main__&#39;:
    forks = [Fork(idx) for idx in range(numForks)]
    philosophers = [Philosopher(idx) for idx in range(numPhilosophers)]
    for philosopher in philosophers:
            philosopher.start()

    try:
        while True: sleep(0.1)
    except Exception as e:
        raise e
</code></pre><h3 id="-">死锁解决</h3>
<p>要拿起刀叉就两个一起拿，判断是不是左右刀叉都可以使用，这个方法就不想用AND信息集了，我想复习。在fork类中加入key值，判断是否可以使用，在一个函数返回key值，想要使用的时候判断是不是都可以使用.这个方法是有问题的，思考时间设置为0的时候基本会秒锁，但是这样改了代码之后时间会很久，比如说我把这个README写完就停了。<br>run函数更改如下</p>
<pre><code>def run(self):
        while True:
            if self.leftFork.ke()==0 and self.rightFork.ke()==0:
                self.leftFork.pickup()
                self.rightFork.pickup()
                self.dining()
                self.rightFork.putdown()
                self.leftFork.putdown()
                self.thinking()
</code></pre><p>fork类更改</p>
<pre><code>class Fork():
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()
        self.key = 0

    def ke(self):
        return self.key

    def pickup(self):
        self.key = 1
        self._lock.acquire()

    def putdown(self):
        self.key = 0
        self._lock.release()
</code></pre>`
