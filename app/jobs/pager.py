import re


def run(arguments):
    print("pager %s" % arguments)
    pattern = arguments.get("pager_pattern")
    page = arguments.get("pager_page")
    url = re.sub(r"{page}", "%i" % page, pattern)


    return {
        "pager_pattern": pattern,
        "pager_page": page + 1,
        "url": url,
    }
