from parse import *
if __name__ == '__main__':

    percentage = int(input('Percentage:(%)\n'))
    n = int(input('Number:\n'))
    #aw = input()
    #(percentage, ch1, ch2, n) = [t(s) for t, s in zip((int, str, str, int), raw.split())]
    #r = parse("{:n}{:1}{:1}{:n}\n", raw)
    print("%s%% %c%c %s is %f" % (percentage, 'o', 'f', n, n*(percentage/100)))
