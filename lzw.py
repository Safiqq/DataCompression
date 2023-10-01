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
        self.input = "LOSSLESSLOSSLESS"
        print()

        if len(self.input) > 0:
            self.table.append(["P", "C", "Output", "Add to dictionary"])
            self.table.append(["", "", "Index", "Index", "String"])

            P = self.input[0]
            for i in range(len(self.input)):
                _P = P
                C = "EOF" if len(self.input) == i + 1 else self.input[i + 1]
                checker = False
                if P + C in self.dict:
                    P += C
                    checker = True
                else:
                    self.output += str(self.dict.index(P)) + " "
                    if C != "EOF":
                        self.dict.append(P + C)
                        P = C
                self.table.append(
                    [
                        _P,
                        C,
                        "" if checker else self.dict.index(_P),
                        "" if checker or C == "EOF" else len(self.dict) - 1,
                        "" if checker or C == "EOF" else self.dict[len(self.dict) - 1],
                    ]
                )
            tabulate(self.table, {(0, 3): 2}, {(0, 0): 2, (0, 1): 2})
            print("Hasil decoding:", self.output)
            print("Jumlah byte awal:", len(self.input))
            print("Jumlah byte akhir:", len(self.output) - 1)
        else:
            print("String tidak boleh kosong!")

    def decode(self):
        # self.input = input("Masukkan string yang ingin di-decode: ")
        self.input = "ABABBABCAB"
        print()

        if len(self.input) > 0:
            try:
                self.table.append(
                    ["PW string", "CW", "", "P", "C", "Output", "Add to dictionary"]
                )
                self.table.append(
                    ["", "Index", "String", "", "", "", "Index", "String"]
                )
                tabulate(
                    self.table,
                    {(0, 1): 2, (0, 6): 2},
                    {(0, 0): 2, (0, 3): 2, (0, 4): 2, (0, 5): 2},
                )
            except:
                print("String tidak valid")
        else:
            print("String tidak boleh kosong!")


if __name__ == "__main__":
    # try:
    huffman = Huffman()
    option = int(input("1. Encode\n2. Decode\nApa yang ingin kamu lakukan? "))
    if option == 1:
        huffman.encode()
    elif option == 2:
        huffman.decode()
    else:
        print("!!!")
# except:
#     print("Input harus angka!")
