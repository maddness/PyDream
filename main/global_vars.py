def change_global():
    # shitty idea but OK..
    global glob
    glob = 20


glob = 10
print 'before change ' + str(glob)

change_global()

print 'after change ' + str(glob)

