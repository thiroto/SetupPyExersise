import os

def echolist():
    r = []

    #print "in mod" + os.path.basename(__file__)
    #print "in mod" + os.path.abspath(__file__)
    #print "in mod" + os.path.abspath(os.path.dirname(__file__))
    #print "in mod" + os.getcwd()

    modp = os.path.abspath(os.path.dirname(__file__))
    filep = "moduledata/hellolist.txt"
    path = os.path.join(modp, filep)
    
    f = open(path)

    for x in f.readlines():
        r.append(x)

    return r

if __name__ == '__main__':
    print echolist()
