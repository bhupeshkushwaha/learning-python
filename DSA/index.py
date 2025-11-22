"""Simple entry script for the DSA folder demonstrating the k_length_apart function."""
from k_length_apart import k_length_apart


def main():
    arr = [1,0,0,0,1,0,0,1]
    k = 2
    print("Array:", arr)
    print("k:", k)
    print("Result:", k_length_apart(arr, k))


if __name__ == '__main__':
    main()
