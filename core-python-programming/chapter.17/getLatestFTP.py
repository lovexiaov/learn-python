import ftplib
import os
import socket

__author__ = 'weixy6'

HOST = '10.100.8.93'
DIRN = 'tmp'
FILE = 'hello.txt'


def main():
    try:
        f = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror), e:
        print 'ERROR: cannot reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.login(user='uftp', passwd='uftp')
        # f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "uftp"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Change to "%s"' % DIRN

    try:
        f.retrbinary('RETR %s' % FILE, file(FILE, 'wb').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CWD' % FILE
    f.quit()
    return


if __name__ == '__main__':
    main()
