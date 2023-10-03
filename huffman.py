# Huffman Coding
from tabulate_cell_merger.tabulate_cell_merger import tabulate
import ast


class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right


class Huffman:
    def __init__(self):
        self.input = ""
        self.table = [["Karakter", "Frekuensi", "Kode", "Panjang kode", "Jumlah bit"]]
        self.output = ""

    def encode(self):
        self.input = input("Masukkan string yang ingin di-encode: ")
        print()

        if len(self.input) > 0:
            freq = {}
            for char in self.input:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1

            # Create tree
            nodes = [Node(freq, char) for char, freq in freq.items()]
            while len(nodes) > 1:
                nodes.sort(key=lambda x: x.freq)
                left = nodes.pop(0)
                right = nodes.pop(0)
                parent = Node(left.freq + right.freq, left=left, right=right)
                nodes.append(parent)

            codes = {}

            def huffmanCode(node, curr_code):
                if node:
                    if node.char:
                        codes[node.char] = curr_code
                    huffmanCode(node.left, curr_code + "1")
                    huffmanCode(node.right, curr_code + "0")

            huffmanCode(nodes[0], "")

            # Fill table
            for char, freq in freq.items():
                code = codes[char]
                self.table.append([char, freq, code, len(code), freq * len(code)])

            for char in self.input:
                self.output += codes[char]
            tabulate(self.table)
            print("Hasil encoding:", self.output)
            print("Jumlah bit awal:", len(self.input) * 8)
            print("Jumlah bit akhir:", len(self.output))

            option = input("Apakah kamu ingin menyimpan tabelnya?(Y/n) ")
            if option.lower() == "y" or option == "":
                open("huffman.txt", "a").write(str(self.table))
        else:
            print("String tidak boleh kosong!")

    def decode(self):
        self.input = input("Masukkan string yang ingin di-decode: ")
        print()

        if len(self.input) > 0:
            try:
                with open("huffman.txt", "r") as file:
                    self.table = ast.literal_eval(file.read())
                tabulate(self.table)
                curr_code = ""
                codes = dict([(row[2], row[0]) for row in self.table[1:]])
                for i in self.input:
                    curr_code += i
                    if curr_code in codes:
                        self.output += codes[curr_code]
                        curr_code = ""
                print("Hasil decoding:", self.output)
                print("Jumlah bit awal:", len(self.input))
                print("Jumlah bit akhir:", len(self.output * 8))
            except:
                print("String tidak valid atau data tabel kosong!")
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
