#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string findMedian(vector<int> &arr)
{
    sort(arr.begin(), arr.end());
    int middle = arr.size() / 2;
    if (arr.size() % 2 == 0)
        return to_string((arr[middle] + arr[middle - 1]) / 2);
    else
        return to_string(arr[middle]);
}

string MovingMedian(int arr[], int arrLength)
{
    int window = arr[0];
    string result = "";
    int start = 0;
    vector<int> bank;
    for (int i = 1; i < arrLength; ++i)
    {

        if (bank.size() - start == window)
            start++;
        bank.push_back(arr[i]);

        vector<int> temp;
        for (int j = start; j < bank.size(); ++j)
        {
            temp.push_back(bank[j]);
        }
        result += findMedian(temp) + ",";
    }
    result.pop_back();
    return result;
}

int main(void)
{

    // keep this function call here
    int A[] = coderbyteInternalStdinFunction(stdin);
    int arrLength = sizeof(A) / sizeof(*A);
    cout << MovingMedian(A, arrLength);
    return 0;
}