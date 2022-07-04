# THIS IS TO CHECK/PRINT HOW MANY POSSIBLE COMBINATIONS CAN A
#     - 10 DIGITS
#     - 26 LETTERS
#     - 31 CHARACTER CODES

import time
import threading

#   digitizer(length)
#   this is to print/write the possible combinations of a certain length provided by the user
#   includes time elapsed
#   start - beginning of a thread
#   end - th# itself
#   size - the quantity of numbers
#   length - length of characters


def digitizer(start, end, size, length):
    combination_list = []
    while start < end:
        digit_to_append = f"{(int(length)-len(str(start)))* '0'  + str(start)}"
        start += 1
        print(digit_to_append)


def main():
    time_start = time.time()
    length = input("LENGTH: ")
    size = (10 ** int(length)) - 1
    size_downscale = (10 ** int(length)) / 4  # 1 LENGTH = 10 DIGITS/CHARACTERS

    th1 = size_downscale
    th2 = th1 + size_downscale
    th3 = th2 + size_downscale
    th4 = (th3 + size_downscale) - 1

    thread1 = threading.Thread(target=digitizer, args=(0, th1, size, length))
    thread2 = threading.Thread(target=digitizer, args=(int(th1), int(th2), size, length))
    thread3 = threading.Thread(target=digitizer, args=(int(th2), int(th3), size, length))
    thread4 = threading.Thread(target=digitizer, args=(int(th3), int(th4), size, length))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    time_end = time.time()
    print(time_end - time_start)

main()