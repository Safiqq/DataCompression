# Lempel-Ziv-Welch
from tabulate_cell_merger.tabulate_cell_merger import tabulate


class Huffman:
    def __init__(self):
        self.input = ""
        # self.input = input("Masukkan string yang ingin di-encode: ")
        self.dict = [
            "EOF",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        self.table = []
        self.output = ""

    def encode(self):
        # self.input = input("Masukkan string yang ingin di-encode: ")
        self.input = "ABABBABCAB"
        print()

        if len(self.input) > 0:
            self.table.append(["P", "C", "Output", "Add to dictionary"])
            self.table.append(["", "", "Index", "Index", "String"])
            tabulate(self.table, {(0, 3): 2}, {(0, 0): 2, (0, 1): 2})
        else:
            print("String tidak boleh kosong!")

    def decode(self):
        # self.input = input("Masukkan string yang ingin di-decode: ")
        self.input = "ABABBABCAB"
        print()

        if len(self.input) > 0:
            try:
                self.table.append(["PW string", "CW", "", "P", "C", "Output", "Add to dictionary"])
                self.table.append(["", "Index", "String", "", "", "", "Index", "String"])
                tabulate(self.table, {(0, 1): 2, (0, 6): 2}, {(0, 0): 2, (0, 3): 2, (0, 4): 2, (0, 5): 2})
            except:
                print("String tidak valid")
        else:
            print("String tidak boleh kosong!")


if __name__ == "__main__":
    try:
        huffman = Huffman()
        option = int(input("1. Encode\n2. Decode\nApa yang ingin kamu lakukan? "))
        if option == 1:
            huffman.encode()
        elif option == 2:
            huffman.decode()
        else:
            print("!!!")
    except ValueError:
        print("Input harus angka!")
