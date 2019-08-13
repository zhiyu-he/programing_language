#include<stdio.h>
#include<sstream>
#include<string>
#include<iostream>

int main() {
    std::shared_ptr<int> p =  std::make_shared<int>();
    std::stringstream ss;
    ss << p;
    std::string out = ss.str();
    std::cout << out;
    return 0;
}
