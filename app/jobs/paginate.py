import re


def run(arguments, database=None):
    print("paginate %r" % arguments)
    pattern = arguments.get("paginate_pattern")
    page = arguments.get("paginate_page", 0)
    page_max = arguments.get("paginate_page_max", 0)
    source_id = arguments.get("source_id")

    url = re.sub(r"{page}", "%i" % page, pattern)
    ended = page >= page_max

    result = {
        "paginate_pattern": pattern,
        "paginate_page": page + 1,
        "url": url,
        "source_id": source_id,
    }
    return (ended, [result])
