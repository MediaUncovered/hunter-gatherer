import re


def run(arguments):
    print("paginate %r" % arguments)
    pattern = arguments.get("paginate_pattern")
    page = arguments.get("paginate_page")
    url = re.sub(r"{page}", "%i" % page, pattern)

    result = {
        "paginate_pattern": pattern,
        "paginate_page": page + 1,
        "url": url,
    }
    return [result]
