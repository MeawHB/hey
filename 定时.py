import datetime
import os


dotime = [(14, 26), (14, 27)]  # [小时，分钟]
docommand ="echo 'sx'"


def do():
    val = os.system(docommand)
    # print("val1:%s" % val)
    if val == 0:
        print("运行成功")
    else:
        print("失败啦")
    time.sleep(66)


def main():
    ifdo = False
    while True:
        while True:
            now = datetime.datetime.now()
            # print(now)
            # print("now %s:%s" % (now.hour, now.minute))
            for h, m in dotime:
                if now.hour == h and now.minute == m:
                    ifdo = True
                    break
            if ifdo == True:
                break
            time.sleep(18)
            # print("h:m  %s:%s" % (h, m))
        do()
        ifdo = False


if __name__ == '__main__':
    main()
