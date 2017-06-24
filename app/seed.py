from jobs.tasks import Queuer

q = Queuer()
q.que("MOSCOW_ALL", u"http://old.themoscowtimes.com/sitemap/")
