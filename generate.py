import os
import json
import time

from jinja2 import Environment, FileSystemLoader


def datetime_format(value, fmt="%Y-%m-%d %H:%M:%S", offset_hours=0):
    from datetime import datetime
    return datetime.utcfromtimestamp(value + offset_hours * 3600).strftime(fmt)


def json_encode(value, ensure_ascii=False, indent=4):
    return json.dumps(value, ensure_ascii=ensure_ascii, indent=indent)


def strip_hashtag(value):
    return value.strip('#')


def lf2br(value):
    return value.replace('\n', '<br/>')


with open("output.json", encoding="utf-8") as f:
    feeds = json.load(f)
page_size = 50
total_pages = len(feeds) // page_size
if (len(feeds) % page_size) != 0:
    total_pages += 1
pages = []
for i in range(total_pages):
    pages.append(feeds[i * page_size:(i + 1) * page_size])

env = Environment(loader=FileSystemLoader("templates/"))
env.filters["datetime_format"] = datetime_format
env.filters["json_encode"] = json_encode
env.filters["strip_hashtag"] = strip_hashtag
env.filters["lf2br"] = lf2br
layout = env.get_template("layout.jinja2")
os.makedirs("dist", exist_ok=True)
build_time = int(time.time())

for i in range(len(pages)):
    current_page_feeds = pages[i]
    p = i + 1
    with open(f"dist/page_{p}.html", "w+", encoding="utf-8") as f:
        f.write(layout.render(feeds=current_page_feeds, page=p, index=i,
                              total_pages=total_pages, build_time=build_time))
