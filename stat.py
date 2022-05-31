import json

with open("output.json", encoding="utf-8") as f:
    feeds = json.load(f)

types = {}
for feed in feeds:
    if not feed["type"] in types.keys():
        types[feed["type"]] = 0
    types[feed["type"]] += 1

for k, v in types.items():
    print(f"{k:<24}\t{v}")
