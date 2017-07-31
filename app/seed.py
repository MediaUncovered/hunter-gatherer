from jobs.tasks import Queuer
from crawler import model

print("started")

print("Creating database")
model.init()

session = model.session()
print("Inserting Moscow Times")
moscow_times_source = model.Source(name="Moscow Times")
session.add(moscow_times_source)
session.commit()

print("Seeding first task")
q = Queuer()

# q.que(
#     "MOSCOW_DAY",
#     u"http://old.themoscowtimes.com/sitemap/free/1992/12/2.html",
#     moscow_times_source.id)

# q.que(
#     "MOSCOW_YEAR",
#     u"http://old.themoscowtimes.com/sitemap/free/1992.html",
#     moscow_times_source.id)

q.que("MOSCOW_ALL",
      u"http://old.themoscowtimes.com/sitemap/",
      moscow_times_source.id)

print("DONE")
