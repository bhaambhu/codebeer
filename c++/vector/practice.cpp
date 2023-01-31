#include <iostream>
#include <vector>

using namespace std;
int main() {
  // cout << "Hello World";
  vector<int> a(5,1);
  auto it = a.insert(a.begin(),2);

  vector<int> b(3,2);
  
  for (auto i:a){
    cout << i << " ";
  }
  cout<< endl;
  cout << "a.size: "<< a.size() << endl;
  cout << "a.capacity: "<< a.capacity() << endl;
  cout << "a.maxsize: "<< a.max_size() << endl;
}