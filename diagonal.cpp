#include<iostream>
using namespace std;
class Diagonal{
private:
int *A;
int n;
public:
Diagonal(){
    n=2;
    A=new int[2];
}
Diagonal(int n){
    this->n=n;
    A=new int[n];
}
~Diagonal(){
    delete[]A;
}
void set(int i,int j,int x);
int Get(int i,int j);
void Display();
};
void Diagonal::set(int i,int j,int x){
    if(i==j)
    A[i-1]=x;}
int Diagonal::Get(int i,int j){
    if(i==j)
    return A[i-1];
    return 0;
    }
void Diagonal::Display(){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(i==j)
            cout<<A[i]<<" ";
            else{
                cout<<"0"<<" ";
            }
        }cout<<endl;
    }
}
int main(){
    int x,n;
    cout<<"Enter the size of the array\n";
    cin>>n;
    Diagonal d(n);
    cout<<"Enter the element"<<endl;
    for(int i=1;i<=n;i++){
        cin>>x;
         d.set(i,i,x);
    }
    // d.set(1,1,5);
    // d.set(2,2,6);d.set(3,3,7);d.set(4,4,9);
    d.Display();
    return 0;
}