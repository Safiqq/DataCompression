# Data Compression Algorithms

This repository contains three data compression algorithms implemented in Python:

1. **Run Length Encoding (RLE)**

    Examples:
    * *BBBBEEEEEEEECCCCDAAAAA* -> *4B8E4C1D5A*
    * *121111134444113335111133* -> *11211531441233511432* 
    * *WWWWWWWWWWWWKWWWWWWWWWWWWKKKWWWWWWWWWWWWWWWWWWWWWWWWKWWWWWWWWWWWWWW* -> *12W1K12W3K24W1K14W*

2. **Huffman Coding**

    Examples:
    * *AAAABBDCCAAAEEEBBBCDDAABCCDAAA* -> *111100000001000100111101101101100000000000101001011000001001010111*
    * *LOSSLESS* -> *01001110100011*
    * *AAAABBDCCAAAEEEBBBCDDAABC* -> *00000000101001111110000000100100101010101101101100001011*

3. **Lempel-Ziv-Welch (LZW)**

    Examples:
    * *ITETEBEBE* -> *9 20 5 28 2 5 31*
    * *LOSSLESSLOSSLESS* -> *12 15 19 19 12 5 29 27 33 32 19*
    * *ARIFINADALAHMAHASISWA* -> *1 18 9 6 9 14 1 4 1 12 1 8 13 37 1 19 9 19 23 1*

## Requirements
1. Python (3.x recommended)
2. tabulate_cell_merger

## Usage
You can use these scripts to perform data compression and decompression:
```
python rle.py
```
```
python huffman.py
```
```
python lzw.py
```

or you can run the main program instead by:

```
python main.py
```