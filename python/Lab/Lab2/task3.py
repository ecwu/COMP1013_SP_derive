if __name__ == '__main__':
    raw = input("Please input two integers\n")
    n1, n2 = raw.split()
    n1, n2 = [int(n1), int(n2)]
    print("%d + %d = %d\n" % (n1, n2, n1 + n2))
    print("%d - %d = %d\n" % (n1, n2, n1 - n2))
    print("%d * %d = %d\n" % (n1, n2, n1 * n2))
    print("%d / %d = %d\n" % (n1, n2, n1 / n2))
    print("%d %% %d = %d\n" % (n1, n2, n1 % n2))

