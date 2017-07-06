from jobs.tasks import Queuer
from crawler import model

print("started")

print("Creating database")
model.seed()

print("Seeding first task")
q = Queuer()
q.que("MOSCOW_ALL", u"http://old.themoscowtimes.com/sitemap/")
print("DONE")
