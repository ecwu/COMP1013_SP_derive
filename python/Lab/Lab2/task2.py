import sys
if __name__ == '__main__':
    percentage = int(input('Percentage:(%)\n'))
    n = int(input('Number:\n'))

    print("%s%% %c%c %s is %f" % (percentage, 'o', 'f', n, n*(percentage/100)))
    sys.exit()
