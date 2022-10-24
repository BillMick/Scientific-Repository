# include <iostream>
using namespace std;
int main()
{
    string crc, encoded;
    cout << "Received Message = ";
    getline(cin, encoded);
    cout << "Generator = ";
    getline(cin, crc);
    for(int i = 0; i <= encoded.length() - crc.length();)
    {
        for(int j = 0; j < crc.length(); j++)
            encoded[i+j] = encoded[i+j] == crc[j]? '0' : '1';
        for( ; i < encoded.length() && encoded[i] != '1'; i++);
    }
    for(char i : encoded.substr(encoded.length() - crc.length()))
        if(i != '0')
        {
            cout << "Error in communication ..." << "\n";
            return 0;
        }
    cout << "No error !" << "\n";
    return 0;
}