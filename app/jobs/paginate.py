import re


def run(arguments):
    print("paginate %r" % arguments)
    pattern = arguments.get("paginate_pattern")
    page = arguments.get("paginate_page")
    source_id = arguments.get("source_id")
    url = re.sub(r"{page}", "%i" % page, pattern)

    result = {
        "paginate_pattern": pattern,
        "paginate_page": page + 1,
        "url": url,
        "source_id": source_id,
    }
    return [result]
