from crawler import model
from crawler.storage import PostGresArchiver

session = model.session()
archiver = PostGresArchiver(session)
articles = archiver.all()

count_total = 0
count_title = 0
for article in articles:
    print("Article: \n%s\n%s" % (article.title, article.url))
    count_total += 1
    if article.title is not None:
        count_title += 1

print("%d out of %d articles are (sucessfully) processed" % (count_title, count_total))
