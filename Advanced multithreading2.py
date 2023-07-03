# threading.Thead 的 join方法解释

# 简单总结一下join会阻塞线程，是子线程运行结束前等待，函数参数是等待每个子进程的时间（秒）

'''
1.子线程不使用join方法

join方法主要是会阻塞主线程，在子线程结束运行前，主线程会被阻塞等待。这里用一个例子来说明：
'''
# encoding=utf8
'''
import threading
import time


def now():
	return '%.3f' % time.time()


def test(n):
	print('start %s at: %s' % (n, now()))
	time.sleep(n)
	print('end %s at: %s' % (n, now()))


def main():
	print('start main at: %s' % now())
	threadpool = []
	for i in range(1, 4):
		th = threading.Thread(target=test, args=(i,))
		threadpool.append(th)
	for th in threadpool:
		th.start()
		# for th in threadpool:
		th.join()
	print('main end at: %s' % now())


if __name__ == '__main__':
	main()
'''
'''
在上面的例子中，每个子线程都会执行test方法，为了方便看结果，使每个子线程的sleep时间不同。

当前只是调用了每个子线程的start方法，并没有调用join方法，此时运行结果：

	start main at: 1521721709.912
	start 1 at: 1521721709.913
	start 2 at: 1521721709.913
	start 3 at: 1521721709.913
	main end at: 1521721709.913
	end 1 at: 1521721710.913
	end 2 at: 1521721711.913
	end 3 at: 1521721712.913

通过结果可以看出，主线程完成第一次打印后（start main at: 1521721709.912），其他子线程同时开始，但是主线程并没有等待子线程结束才结束，
主线程继续执行第二次打印（main end at: 1521721709.913），接着其他子线程因为各自sleep的时间不同而相继结束。

2.子线程使用join方法

下面再看一下使用join方法后的结果（将上面注释掉的部分取消）：

	start main at: 1521722097.382
	start 1 at: 1521722097.382
	start 2 at: 1521722097.382
	start 3 at: 1521722097.382
	end 1 at: 1521722098.382
	end 2 at: 1521722099.382
	end 3 at: 1521722100.383
	main end at: 1521722100.383

不难看出，主线程阻塞等待子线程完成后，自己才结束运行。

3.join方法的timeout参数

然后可以给在join函数传一个timeout参数的，看看它的作用是什么，这里修改了一下代码：

	# encoding=utf8
	 
	import threading
	import time
	 
	def now():
		return  '%.3f' % time.time()
	 
	def test(n):
		while 1:
			print str(n) * 6
			time.sleep(5)
	 
	def main():
		print 'start main at: %s' % now()
		threadpool = []
		for i in xrange(1, 3):
			th = threading.Thread(target=test, args=(i, ))
			threadpool.append(th)
		for th in threadpool:
			th.start()
		for th in threadpool:
			th.join(5)
		print 'main end at: %s' % now()
	if __name__ == '__main__':
		main()

这里设置每个线程的timeout都是5，运行部分结果如下：

	start main at: 1521723210.825
	111111
	222222
	222222
	111111
	main end at: 1521723220.825
	111111
	222222
	111111
	222222
	......

因为每个子线程执行的是一个while循环，实际上是会一直运行下去的（两个子线程一直打印111111,222222），如果不给join方法设置timeout，
那么主线程会一直等下去，永远不会执行最后的“print 'main end at: %s' % now()”语句，但是上面的代码设置了timeout为5秒，
通过执行结果可以看出，主线程一共等待了10秒后结束了自己的运行。所以可以知道，join方法的timeout参数表示了主线程被每个子线程阻塞等待的时间。

4.说说setDaemon

使用join方法是为了让主线程等待子线结束后再做其他事情，setDaemon方法正好相反，它是为了保证主线程结束的时候，整个进程就结束，
不会等待所有子线程执行完才结束。修改一下上面的代码：
'''
# encoding=utf8
'''
import threading
import time


def now():
    return '%.3f' % time.time()


def test(n):
    time.sleep(n)
    print('%s has ran' % (str(n) * 6))


def main():
    print('start main at: %s' % now())
    threadpool = []
    for i in range(2):
        th = threading.Thread(target=test, args=(i,))
        threadpool.append(th)
    for th in threadpool:
        th.setDaemon(True)
        th.start()
    print('main end at: %s' % now())


if __name__ == '__main__':
    main()
'''
'''
以下是运行结果：
	start main at: 1521726104.773
	000000 has ran
	main end at: 1521726104.773
'''
