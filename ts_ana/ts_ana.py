# coding=utf-8

if __name__ == "__main__":
    with open("/Users/tianyu/mlog.txt", "r") as inputFile:
        count_total = 0
        count_ts = 0
        list_ts = []
        while True:
            line = inputFile.readline()
            if not line:
                break
            else:
                count_total += 1
                if len(line.split(",")[1].split(".")) == 4:
                    if line.split(",")[1].split(".")[2] not in list_ts and line.split(",")[1].split(".")[1] != "SYSTEM":
                        list_ts.append(line.split(",")[1].split(".")[2])
                        count_ts += 1
                # else:
                #     print(line.split(",")[1])
        print(count_total)
        print(count_ts)
        print(list_ts)
