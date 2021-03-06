import sys, os

cmdqidong = '/usr/sbin/tomcat start'
cmdjiance = 'ps -ef | grep tomcat |grep -v grep'

def main():
    """ A demo daemon main routine, write a datestamp to
        /tmp/daemon-log every 10 seconds.
    """
    import time
    while 1:
        res = os.popen(cmdjiance).read()
        if res:
            # print(res)
			pass
        else:
            os.popen(cmdqidong)
        time.sleep(10)


if __name__ == "__main__":
    # do the UNIX double-fork magic, see Stevens' "Advanced
    # Programming in the UNIX Environment" for details (ISBN 0201563177)
    try:
        pid = os.fork()
        if pid > 0:
            # exit first parent
            sys.exit(0)
    except OSError as e:
        print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1)
    # decouple from parent environment
    os.chdir("/")
    os.setsid()
    os.umask(0)
    # do second fork
    try:
        pid = os.fork()
        if pid > 0:
            # exit from second parent, print eventual PID before
            print("Daemon PID %d" % pid)
            sys.exit(0)
    except OSError as e:
        print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1)
    # start the daemon main loop
    main()