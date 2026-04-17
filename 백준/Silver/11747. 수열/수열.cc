#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<int> a(N);
    for(int i = 0; i < N; i++) cin >> a[i];

    const int LIMIT = 1000;
    vector<bool> seen(LIMIT + 1, false);

    for(int i = 0; i < N; i++) {
        int num = 0;
        for(int j = i; j < N; j++) {
            num = num * 10 + a[j];
            if(num > LIMIT) break;
            seen[num] = true;
        }
    }

    for(int i = 0; i <= LIMIT; i++) {
        if(!seen[i]) {
            cout << i;
            break;
        }
    }
}