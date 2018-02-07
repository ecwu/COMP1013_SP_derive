import sys
if __name__ == '__main__':
    a_bool = bool(0)
    an_int = 0
    a_float = float(0)
    a_complex = complex(0, 0)
    a_str = ''
    a_tuple = ()
    a_list = []
    a_dict = {}
    a_set = set()
    an_iterator = iter([1, 2, 3])

    print("Number of bytes used to store a bool type variable is: %d\n" % (sys.getsizeof(a_bool)))
    print("Number of bytes used to store an integer type variable is: %d\n" % (sys.getsizeof(an_int)))
    print("Number of bytes used to store a float type variable is: %d\n" % (sys.getsizeof(a_float)))
    print("Number of bytes used to store a complex type variable is: %d\n" % (sys.getsizeof(a_complex)))
    print("Number of bytes used to store a string type variable is: %d\n" % (sys.getsizeof(a_str)))
    print("Number of bytes used to store a tuple type variable is: %d\n" % (sys.getsizeof(a_tuple)))
    print("Number of bytes used to store a list type variable is: %d\n" % (sys.getsizeof(a_list)))
    print("Number of bytes used to store a dict type variable is: %d\n" % (sys.getsizeof(a_dict)))
    print("Number of bytes used to store a set type variable is: %d\n" % (sys.getsizeof(a_set)))
    print("Number of bytes used to store an iterator type variable is: %d\n" % (sys.getsizeof(an_iterator)))
