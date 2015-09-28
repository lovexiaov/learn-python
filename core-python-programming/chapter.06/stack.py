"""
    this demo simulate a FILO stack
"""
__author__ = 'weixy6'

stack = []


def pushit(data):
    stack.append(data)


def popit():
    if len(stack) == 0:
        print 'there is no data to pop'
    else:
        stack.pop()


def viewstack():
    print stack


def showMenu():
    pr = '''Use Introduction:
    p(U)sh
    p(O)p
    sho(W)
    (Q)uit
    '''
    print pr


if __name__ == '__main__':
    showMenu()

    while True:
        action = raw_input("please choice an action:\n").upper()
        if action == 'U':
            pushit(raw_input('input something:').strip())
        elif action == 'O':
            popit()
        elif action == 'W':
            viewstack()
        elif action == 'Q':
            break
        else:
            print 'invalid action!!!'
