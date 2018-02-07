from scanf import *
if __name__ == '__main__':
    percentage, ch1, ch2, number = scanf("%d%c%c%d", input())
    print("%s%% %c%c %s is %f" % (percentage, ch1, ch2, number, number*(percentage/100)))
