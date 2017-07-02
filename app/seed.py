from jobs.tasks import Queuer

print("started")
q = Queuer()
q.que("MOSCOW_ALL", u"http://old.themoscowtimes.com/sitemap/")
