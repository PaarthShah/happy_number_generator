// Happy Number Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <unordered_set>

using std::string;
using std::to_string;
using std::vector;
using std::unordered_set;
using std::cout;
using std::endl;

int sum_of_squares(int n)
{
    // Square all of the digits in n, and return their sum.
    string s = to_string(n);
    int sum = 0;
    for (auto it = s.cbegin(); it != s.cend(); ++it)
    {
        // (*it - '0') is the integer at this iterator.
        sum += pow((*it - '0'), 2);
    }
    return sum;
}

bool is_happy_build_cache(int n, unordered_set<int> &happy_set, unordered_set<int> &sad_set, vector<int> &happy_list)
{
    // Cache the initial number. Check whether the sum of the squares of the number's digits is known to be happy or sad.
    // Repeat if not known, or update the appropriate happy/sad cache if known or determined.
    unordered_set<int> cycle;
    cycle.insert(n);
    while (true)
    {
        n = sum_of_squares(n);
        cycle.insert(n);
        if (sad_set.contains(n))
        {
            sad_set.merge(cycle);
            return false;
        }
        if (happy_set.contains(n))
        {
            happy_set.merge(cycle);
            return true;
        }
    }
}

bool is_happy_use_cache(int n, unordered_set<int>& sad_set)
{
    // Check whether the sum of the squares of the number's digits is known to be sad.
    // If it is sad, add the number to the sad cache.
    // If it isn't sad, it must necessarily be happy since the sad cache is guaranteed to contain all sad numbers < n at this point of execution.
    int next = sum_of_squares(n);
    if (sad_set.contains(next))
    {
        sad_set.insert(n);
        return false;
    }
    else
        return true;
}

int main()
{   
    // A happy number is any number n where sum_of_squares(n) is a happy number. The base happy number is 1.
    // A sad number is any number n that is not happy, ie goes into an infinite loop that never reaches 1.

    // Initialize cache with trivial seed.
    unordered_set<int> happy_set({ 1 });
    unordered_set<int> sad_set({ 4 });
    vector<int> happy_list;
    int iterated_number = 1;

    // Smallest integer solution to the equation 81x <= 10^(x) - 1: x = 3.
    // QED: sum_of_squares(n) < n for all n >= 10^2 = 99

    // Build up cache for all two-digit numbers.
    for (; iterated_number <= 99; iterated_number++)
    {
        if (is_happy_build_cache(iterated_number, happy_set, sad_set, happy_list))
        {
            happy_list.push_back(iterated_number);
            cout << happy_list.size() << ":\t" << iterated_number << endl;
        }
    }
    // Use the cache of sad numbers to determine the happiness of all other numbers, building it up further as needed.
    for (; happy_list.size() < 10000; iterated_number++)
    {
        if (is_happy_use_cache(iterated_number, sad_set))
        {
            happy_list.push_back(iterated_number);
            cout << happy_list.size() << ":\t" << iterated_number << endl;
        }
    }
}
