import os

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


def main():

    file_path = input("Enter file path: ")

    file_data = readFile(file_path)

    char_frequency = countCharFrequency(fileData=file_data)

    # print(char_frequency)
    print(f"X frequency : {char_frequency['X']}, t frequency : {char_frequency['t']}")


if __name__ == "__main__":
    main()