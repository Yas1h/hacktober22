#include <bits/stdc++.h>
using namespace std;

void tower_of_hanoi(int n, char from, char to, char aux)
{
    if (n == 0){
    return;
    }

    tower_of_hanoi(n - 1, from, aux, to);

    cout << n <<" "<< from <<" "<< to << endl;

    tower_of_hanoi(n - 1, aux, to, from);
}

int main()
{
    int disks;

    cout << "Enter the number of disks: ";
    cin >> disks;

    tower_of_hanoi(disks, 'A', 'C', 'B');
    return 0;
}
