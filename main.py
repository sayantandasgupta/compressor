import os
import heapq

from huffmantree import HuffmanTree

def readFile(filePath : str) -> str:

    if os.path.exists(filePath):
        with open(filePath) as file:
            fileData = file.readlines()

        
        fileData = ''.join(fileData)
        return fileData
    
    else:
        print("Could not open file. File does not exist in given path")
        return ""
    

def countCharFrequency(fileData : str) -> dict:

    freq = {}

    for c in fileData:
        freq[c] = freq.get(c, 0) + 1

    return freq

def buildHuffTree(heap):
    
    temp1, temp2, temp3 = None, None, None

    while len(heap) > 1:
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)

        temp3 = HuffmanTree(temp1, temp2, temp1.weight() + temp2.weight())

        heapq.heappush(heap, temp3)

    return temp3

def main():

    # file_path = input("Enter file path: ")

    # file_data = readFile(file_path)

    # char_frequency = countCharFrequency(fileData=file_data)

    test_dict = {
        'C' : 32,
        'D' : 42,
        'E' : 120,
        'K' : 7,
        'L' : 42,
        'M' : 24,
        'U' : 37,
        'Z' : 2
    }

    # heap = [HuffmanTree(key, value) for key, value in char_frequency.items()]

    heap = [HuffmanTree(key, value) for key, value in test_dict.items()]

    heapq.heapify(heap)

    tree = buildHuffTree(heap=heap)

    print(f"{tree.root.left.root.element} : {tree.root.left.weight()}")




if __name__ == "__main__":
    main()