data = []

with open("output3.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        # remove hidden null bytes
        line = line.replace("\x00", "").strip()

        parts = line.split()

        if len(parts) < 2:
            continue

        count = int(parts[-1])
        asin = "".join(parts[:-1]).replace(" ", "")

        data.append((asin, count))

top10 = sorted(data, key=lambda x: x[1], reverse=True)[:10]

for asin, count in top10:
    print(asin, count)