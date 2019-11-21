
import math
# no three diverse
temp = dict({"A":30,"B":1,"C":10})
na = temp["A"]//2
temp_A = ["AA"]*na
if temp["A"]%2==1:
    temp_A.extend(["A"])
    na+=1
temp_B = [""]*na
for i in range(temp["B"]):
    temp_B[i%na]+="B"

i=i%na+1
for j in range(i,i+temp["C"]):
    temp_B[j%na]+="C"
ans = ""
for i in range(len(temp_A)):
    ans+=temp_A[i]
    ans += temp_B[i]

num = temp["A"]-2-2*(temp["B"]+temp["C"])
if num>0:
    ans = ans[:-num]
else:
    ans=ans
print(ans)


"""
# C++
// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#include <vector>
#include <string>



string solution(int A, int B, int C) {
    // write your code in C++14 (g++ 6.2.0)
    //std:;string s="0";
    //map<string, int> dict ;
    //for (int i=0)
    
    int m=std::max({A,B,C});
    m=m%2+m/2;
    std::vector<std::string> ans ("", m);
    int j = 0;
    for(int i=0;i<A;++i)
    {
        ans[j%m]+="a";
    }
    
    for(int i=0;i<B;++i)
    {
        ans[j%m]+="b";
    }
    
    for(int i=0;i<C;++i)
    {
        ans[j%m]+="c";
    }
    std::string res;
    
    for(int i=0;i<m;++i)
    {
        res+=ans[i];
    }
    int m2=3*m-2-2*(A+B+C);
    if (m2>0)
        return res.substr(0, res.size()-m2);
    else
        return res;
    
    
}

"""



