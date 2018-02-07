if __name__ == '__main__':
    raw = input("Please input two integers\n")
    n1, n2 = raw.split()
    n1, n2 = [int(n1), int(n2)]
    print("%d / %d = %.2f\n" % (n1, n2, (n1*1.0)/(n2*1.0)))
