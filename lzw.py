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
        self.input = "ITETEBEBE"
        print()

        if len(self.input) > 0:
            self.table.append(["P", "C", "Output", "Add to dictionary"])
            self.table.append(["", "", "Index", "Index", "String"])

            _P = self.input[0]
            for i in range(len(self.input)):
                P = _P
                C = "EOF" if len(self.input) == i + 1 else self.input[i + 1]
                isInDict = False
                if _P + C in self.dict:
                    _P += C
                    isInDict = True
                else:
                    self.output += str(self.dict.index(_P)) + " "
                    if C != "EOF":
                        self.dict.append(_P + C)
                        _P = C
                OI = "" if isInDict else self.dict.index(P)
                ADI = "" if isInDict or C == "EOF" else len(self.dict) - 1
                ADS = "" if isInDict or C == "EOF" else self.dict[len(self.dict) - 1]
                self.table.append(
                    [
                        P,
                        C,
                        OI,
                        ADI,
                        ADS,
                    ]
                )
            tabulate(self.table, {(0, 3): 2}, {(0, 0): 2, (0, 1): 2})
            print("Hasil decoding:", self.output)
            print("Jumlah byte awal:", len(self.input))
            print("Jumlah byte akhir:", len(self.output.split(' ')) - 1)
        else:
            print("String tidak boleh kosong!")

    def decode(self):
        # self.input = input("Masukkan string yang ingin di-decode: ")
        self.input = "9 20 5 28 2 5 31".split(" ")
        print()

        if len(self.input) > 0:
            # try:
            self.table.append(
                ["PW string", "CW", "", "P", "C", "Output", "Add to dictionary"]
            )
            self.table.append(["", "Index", "String", "", "", "", "Index", "String"])
            PWS = "NULL"
            for i in range(len(self.input)):
                CWI = int(self.input[i])
                CWS = self.dict[CWI]

                P = CWS
                C = "" if i == 0 else PWS
                O = CWS[0]
                # P = "" if i == len(self.input) else CWS
                # C = "" if i == 0 or i == len(self.input) else PWS
                # O = "" if i == len(self.input) else CWS[0]

                self.table.append(
                    [
                        PWS,
                        CWI,
                        CWS,
                        "" if P else P,
                        C,
                        O,
                        "" if P + C in self.dict else len(self.dict),
                        "" if P + C in self.dict else P + C,
                    ]
                )
                if P + C not in self.dict:  # and i != len(self.input)
                    self.dict.append(P + C)
                PWS = CWS
            tabulate(
                self.table,
                {(0, 1): 2, (0, 6): 2},
                {(0, 0): 2, (0, 3): 2, (0, 4): 2, (0, 5): 2},
            )
        # except:
        #     print("String tidak valid")
        else:
            print("String tidak boleh kosong!")


if __name__ == "__main__":
    # try:
    huffman = Huffman()
    option = 1
    # option = int(input("1. Encode\n2. Decode\nApa yang ingin kamu lakukan? "))
    if option == 1:
        huffman.encode()
    elif option == 2:
        huffman.decode()
    else:
        print("!!!")
# except:
#     print("Input harus angka!")
