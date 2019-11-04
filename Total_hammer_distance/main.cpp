#include <iostream>
#include <vector>

int total_hammer_distance(std::vector<int> & array);


int main() {
    std::cout << "Hello, World!" << std::endl;


    std::vector<int> a;

    a = {12,14,15,17};
    total_hammer_distance(a);

    return 0;

}


int total_hammer_distance(std::vector<int> & array)

{
  long long int result=0;

    int ones[31];

    for(int i=0;i <31 ;i++)
    {ones[i]=0;}

    for(std::vector<int>iterator:: it=array.begin(); it!=array.end();++it)
    {

        for(int i = 0; (1 << i) <= it; i++) //i is the position of the bit
            if((1 << i) & *it)//to see if the bit at i-position is a 1
                ones[i]++;
    }

    for(int i=0;i<31;i++)
    {
        result+=ones[i]*(array.size()-ones[i]);
    }

  return result;

};