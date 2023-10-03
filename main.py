from rle import RLE
from huffman import Huffman
from lzw import LZW

try:
    code = int(input("1. RLE\n2. Huffman\n3. LZW\nApa yang ingin kamu lakukan? "))
    if code in range(1, 4):
        option = int(input("1. Encode\n2. Decode\nApa yang ingin kamu lakukan? "))
        if code == 1:
            if option == 1: RLE().encode()
            elif option == 2: RLE().decode()
            else: print("!!!")
        if code == 2:
            if option == 1: Huffman().encode()
            elif option == 2: Huffman().decode()
            else: print("!!!")
        if code == 3:
            if option == 1: LZW().encode()
            elif option == 2: LZW().decode()
            else: print("!!!")
        else:
            print("!!!")
    else:
        print("!!!")
except:
    print("Input harus angka!")
