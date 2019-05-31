#include <iostream>
#include <boost/any.hpp>
#include <string>
#include <typeinfo>

int main()
{
    boost::any a = 1;
    std::cout << boost::any_cast<int>(a) << '\n';
    a = 3.14;
    std::cout << boost::any_cast<double>(a) << '\n';
    a = true;
    std::cout << boost::any_cast<bool>(a) << '\n'; // print 1
    std::cout << std::boolalpha << boost::any_cast<bool>(a) << '\n';
    
    try 
    {
        a = 1;
        std::cout << boost::any_cast<float>(a) << '\n';
    }
    catch (boost::bad_any_cast &e)
    {
        std::cerr << e.what() << '\n';
    }
    
    // Checking type of currently stored value
    a = 123;
    if (!a.empty())
    {
        const std::type_info &ti = a.type();
        std::cout << "ti: " << ti.hash_code() << '\n';
        std::cout << "int: " << typeid(int).hash_code() << '\n';
        std::cout << "long long : " << typeid(long long).hash_code() << '\n';
        std::cout << "long: " << typeid(long).hash_code() << '\n';
        std::cout << "int64_t: " << typeid(int64_t).hash_code() << '\n';
        std::cout << "uint64_t: " << typeid(uint64_t).hash_code() << '\n';
        std::cout << "float: " << typeid(float).hash_code() << '\n';
        std::cout << "double: " << typeid(double).hash_code() << '\n';
        std::cout << "str: " << typeid(std::string).hash_code() << '\n';

        std::cout << "vecotr<int64_>: " << typeid(std::vector<int64_t>).hash_code() << '\n';
        std::cout << "vecotr<uint64_>: " << typeid(std::vector<uint64_t>).hash_code() << '\n';
    }

    
    a = 1;
    int *i = boost::any_cast<int>(&a);
    std::cout << *i << '\n';
    return 0;

}
