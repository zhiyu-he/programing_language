#include <iostream>
#include <vector>
#include <unordered_map>

int main()
{
    std::vector<std::string> v = {"str1", "str2"};
    v.push_back("str3");

    for(std::string str : v) {
        std::cout << str << '\n';
    }

    std::unordered_map<std::string, std::string> m = {
        {"key1", "val1"},
        {"key2", "val2"}
    };
    m["key3"] = "val3";
    for(auto& n : m) {
        std::cout << "key: [" << n.first << "] Value: [" << n.second << "]\n";
    }
    auto target = m.find("keyn");
    if (target != m.end()) {
        std::cout << "Found" << '\n';
    } else {
        std::cout << "Not Found\n";
    }
}
