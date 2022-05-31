import sys
import time
import json
import requests
import datetime
import http.cookiejar as cj

end_date = input("输入截止日期（yyyy-MM-dd）：")
end_timestamp = int(time.mktime(datetime.datetime.strptime(end_date, "%Y-%m-%d").timetuple()))
cookies = cj.MozillaCookieJar()
cookies.load("bilibili.com_cookies.txt")


def get_feeds(offset=None):
    url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?type=all"
    if offset is not None:
        url += "&offset=" + offset
    res = requests.get(url, cookies=cookies)
    return res.json()


feeds = []
current_offset = None
last_feed_time = 0
while True:
    paged_feed = get_feeds(current_offset)
    if paged_feed["code"] != 0:
        print("错误")
        print(paged_feed)
        sys.exit(0)
    current_offset = paged_feed["data"]["offset"]
    for f in paged_feed["data"]["items"]:
        last_feed_time = f["modules"]["module_author"]["pub_ts"]
        feeds.append(f)
    last_feed_time_str = datetime.datetime.fromtimestamp(last_feed_time).strftime("%Y-%m-%d %H:%M:%S")
    print(f"获取了 {len(feeds)} 条动态，最后一条更新于 {last_feed_time_str} UTC，offset={current_offset}")
    if last_feed_time < end_timestamp:
        print("获取完成")
        break
    time.sleep(1)

with open(f"output.json", "w+", encoding="utf-8") as f:
    f.write(json.dumps(feeds, ensure_ascii=False, indent=4))
