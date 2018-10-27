# HackerRank-Python-Solutions
Solutions for HackerRank in Python
/*
// Sample code to perform I/O:

#include <iostream>

using namespace std;

int main() {
	int num;
	cin >> num;										// Reading input from STDIN
	cout << "Input number is " << num << endl;		// Writing output to STDOUT
}

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ll int a,i;
    cin>>a; 
    ll int n[a],s=0;

    for(i=0;i<a;i++)
    {
        cin>>n[i];
        s=s+n[i];
    }
    
    cout<<s;
    return 0;
    
}
