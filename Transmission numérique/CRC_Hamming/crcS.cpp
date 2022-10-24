# include <iostream>
using namespace std;

int main()
{
    string msg, crc, encoded = "";
    cout << "Message = ";
    getline(cin, msg);
    cout << "Generator = ";
    getline(cin, crc);
    int m = msg.length(), n = crc.length();
    encoded += msg;
    for(int i = 1; i<= n-1; i++)
    encoded += '0';
    cout << 'encoded = ' << ' ' + encoded << '\n'
    for(int i = 0; i <= encoded.length()-n; )
    {
        for(int j = 0; j < n; j++)
            encoded[i+j] = encoded[i+j] == crc[j]? '0':'1';
        for(;i<encoded.length() && encoded[i] != '1'; i++);
    }
    cout << "CRC = " << encoded.substr(encoded.length()-n+1) << "\n";
    cout << "Message sent = " << msg + ' ' + encoded.substr(encoded.length()-n+1) << "\n";
    
    return 0;
}