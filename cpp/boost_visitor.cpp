#include <boost/variant.hpp>
#include <string>
#include <iostream>


struct output : public boost::static_visitor<>
{
    void operator() (double d) const { std::cout << d << '\n'; }
    void operator() (char c) const { std::cout << c << '\n'; }
    void operator() (std::string s) const { std::cout << s << '\n';  }
};

struct output2 : public boost::static_visitor<>
{
    template <typename T>
    void operator() (T t) const { std::cout << t << '\n'; }
};

class output3 : public boost::static_visitor<>
{
public:
    output3(const std::string name, std::vector<std::string>& a): name_(name), v_(a) {}

    void operator() (double d) const { std::cout << d << '\t' << name_ << '\n'; }
    void operator() (std::string s) const { v_.push_back(s); }
    void operator() (char c) const {std::cout << c << '\t' << name_ << '\n'; }

private:
    std::string name_;
    std::vector<std::string>& v_;
};

int main()
{
    std::vector<std::string> vv;
    vv.reserve(1);
    std::string name = "output3";

    boost::variant<double, char, std::string> v;
    v = 3.14;
    std::cout << boost::get<double>(v) << '\n';
    boost::apply_visitor(output{}, v);
    boost::apply_visitor(output2{}, v);
    boost::apply_visitor(output3(name, vv), v);

    v = 'A';
    std::cout << boost::get<char>(v) << '\n';
    boost::apply_visitor(output{}, v);
    boost::apply_visitor(output2{}, v);
    boost::apply_visitor(output3(name, vv), v);


    v = "Boost";
    std::cout << boost::get<std::string>(v) << '\n';
    boost::apply_visitor(output{}, v);
    boost::apply_visitor(output2{}, v);
    boost::apply_visitor(output3(name, vv), v);


    return 0;
}
