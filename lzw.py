# Lempel-Ziv-Welch
from tabulate_cell_merger.tabulate_cell_merger import tabulate


class LZW:
    def __init__(self):
        self.input = ""
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
        self.input = input("Masukkan string yang ingin di-encode: ")
        print()

        if len(self.input) > 0:
            try:
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
                        if C != "EOF":
                            self.dict.append(_P + C)
                            _P = C
                    OI = "" if isInDict else self.dict.index(P)
                    ADI = "" if isInDict or C == "EOF" else len(self.dict) - 1
                    ADS = (
                        "" if isInDict or C == "EOF" else self.dict[len(self.dict) - 1]
                    )
                    self.table.append(
                        [
                            P,
                            C,
                            OI,
                            ADI,
                            ADS,
                        ]
                    )
                    if not isInDict:
                        self.output += str(OI)
                        if not C == "EOF":
                            self.output += " "
                tabulate(self.table, {(0, 3): 2}, {(0, 0): 2, (0, 1): 2})
                print("Hasil encoding:", self.output)
                print("Jumlah byte awal:", len(self.input))
                print("Jumlah byte akhir:", len(self.output.split(" ")))
            except:
                print("String tidak valid!")
        else:
            print("String tidak boleh kosong!")

    def decode(self):
        self.input = input("Masukkan string yang ingin di-decode: ")
        print()

        if len(self.input) > 0:
            try:
                self.table.append(
                    ["PW string", "CW", "", "P", "C", "Output", "Add to dictionary"]
                )
                self.table.append(
                    ["", "Index", "String", "", "", "", "Index", "String"]
                )
                PWS = "NULL"
                for i in range(len(self.input)):
                    CWI = int(self.input[i])
                    CWS = self.dict[CWI]

                    P = "" if PWS == "NULL" else PWS
                    C = CWS[0]
                    O = CWS
                    ADI = "" if P + C in self.dict else len(self.dict)
                    ADS = "" if P + C in self.dict else P + C

                    self.table.append(
                        [
                            PWS,
                            CWI,
                            CWS,
                            P,
                            C,
                            O,
                            ADI,
                            ADS,
                        ]
                    )
                    self.output += O + " "
                    if P + C not in self.dict:
                        self.dict.append(P + C)
                    PWS = CWS
                self.table.append([PWS, "EOF", "", "", "", "", "", ""])
                tabulate(
                    self.table,
                    {(0, 1): 2, (0, 6): 2},
                    {(0, 0): 2, (0, 3): 2, (0, 4): 2, (0, 5): 2},
                )
                print("Hasil decoding:", self.output)
                print("Jumlah byte awal:", len(self.input))
                print("Jumlah byte akhir:", len(self.output.replace(" ", "")))
            except:
                print("String tidak valid!")
        else:
            print("String tidak boleh kosong!")


if __name__ == "__main__":
    try:
        lzw = LZW()
        option = int(input("1. Encode\n2. Decode\nApa yang ingin kamu lakukan? "))
        if option == 1:
            lzw.encode()
        elif option == 2:
            lzw.decode()
        else:
            print("!!!")
    except:
        print("Input harus angka!")
