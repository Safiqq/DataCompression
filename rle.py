# Run Length Encoding


class RLE:
    def __init__(self):
        self.input = ""
        self.output = ""

    def encode(self):
        self.input = input("Masukkan string yang ingin di-encode: ")
        print()

        if len(self.input) > 0:
            prev = self.input[0]
            count = 0
            for i in range(0, len(self.input)):
                if self.input[i] == prev:
                    count += 1
                    if i == len(self.input) - 1:
                        self.output += f"{count}{prev}"
                else:
                    self.output += f"{count}{prev}"
                    prev = self.input[i]
                    count = 1
                    if i == len(self.input) - 1:
                        self.output += f"{count}{prev}"
            print("Hasil encoding:", self.output)
            print("Jumlah byte awal:", len(self.input))
            print("Jumlah byte akhir:", len(self.output))
        else:
            print("String tidak boleh kosong!")

    def decode(self):
        self.input = input("Masukkan string yang ingin di-decode: ")
        print()

        if len(self.input) > 0:
            if len(self.input) % 2 == 0:
                i = 0
                err = False
                while i < len(self.input):
                    try:
                        _ = int(self.input[i])
                    except:
                        err = True
                        print("String tidak valid!")
                    i += 2
                if not err:
                    for i in range(0, len(self.input), 2):
                        self.output += self.input[i + 1] * int(self.input[i])
                    print(self.output)
            else:
                print("String tidak valid!")
        else:
            print("String tidak boleh kosong!")


if __name__ == "__main__":
    try:
        rle = RLE()
        option = int(input("1. Encode\n2. Decode\nApa yang ingin kamu lakukan? "))
        if option == 1:
            rle.encode()
        elif option == 2:
            rle.decode()
        else:
            print("!!!")
    except:
        print("Input harus angka!")
