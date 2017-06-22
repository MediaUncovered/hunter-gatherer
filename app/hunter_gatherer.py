from jobs.queue import Queuer

queuer = Queuer()
for x in range(0, 2000):
    print("%d" % x)
    queuer.queue(None)
