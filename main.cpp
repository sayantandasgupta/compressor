#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string readFile(string filePath) {
    ifstream file;

    file.open(filePath);

    if(file) {
        string fileData;
        file >> fileData;

        return fileData;
    }

    file.close();
    return "";
}

int main() {
    
    string path_to_file, file_data;

    cout<<"Enter file path: ";
    cin>>path_to_file;

    file_data = readFile(path_to_file);

    cout<<file_data[0]<<endl;

    return 0;
}