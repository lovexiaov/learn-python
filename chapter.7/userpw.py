"""
    create new user, and stored
"""
__author__ = 'weixy6'

db = {}


def newuser():
    """create new user"""
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            print 'name taken, try another!'
            continue
        else:
            pwd = raw_input('password:')
            db[name] = pwd
        break


def olduser():
    name = raw_input('login:')
    pwd = raw_input('password:')
    passwd = db.get(name)
    if pwd == passwd:
        print 'login success!', name
    else:
        print 'login failure'


def showmenu():
    prompt = """
(N)ew user login
(O)ld user login
(Q)uit
Enter choice:
"""
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print 'You picked: [%s]' % choice
            if choice not in 'noq':
                print 'invalid option, try again:'
            elif choice == 'n':
                newuser()
            elif choice == 'o':
                olduser()
            else:
                done = True
                chosen = True


if __name__ == '__main__':
    showmenu()
