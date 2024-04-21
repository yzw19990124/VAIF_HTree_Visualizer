import json
from collections import defaultdict as dd

ret = dd(list)
group_num = 0

with open("pythia_logs_full", "r") as logs:
    line = logs.readline()
    while line:
        if line[:5] == "Group":
            group_num += 1
        if line[:4] == "http":
            temp_lst = line.split(":")
            ret[f"Group_{group_num}"].append(line.strip("\n"))

        line = logs.readline()

print("parsing done, writing to json.")
with open("parsed.json", "w") as output:
    json.dump(ret, output)

print("write done.")

        