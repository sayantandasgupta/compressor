#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

string readFile(string filePath) {
    ifstream file;

    file.open(filePath);

    if(file.is_open()) {
        string fileData;
        string x;

        while(file) {
            getline(file, x);
            fileData += x;
        }
        
        return fileData;
    }

    file.close();
    return "";
}

map<char, long> countCharFrequency(string fileData) {
    map<char, long> res;
    long len = fileData.length();

    for(long i=0;i<len;i++) {
        res[fileData[i]]++;
    }

    return res;
}

int main() {
    
    string path_to_file, file_data;
    map<char, long> char_frequency;

    cout<<"Enter file path: ";
    cin>>path_to_file;

    file_data = readFile(path_to_file);

    char_frequency = countCharFrequency(file_data);

    
    cout<<"X frequency: "<<char_frequency.find('X')->second<<endl;
    cout<<"t frequency: "<<char_frequency.find('t')->second<<endl;

    return 0;
}