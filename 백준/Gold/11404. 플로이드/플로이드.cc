#include <bits/stdc++.h>
using namespace std;
#define INF 10000001

int dp[101][101];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++){
            if (i != j) dp[i][j] = INF;

        }

    for (int i = 0; i < m ; i++){
        int a,b,c;
        cin >> a >> b >> c ;
        dp[a][b] = min(dp[a][b],c);
    }

    for (int q = 1; q <= n; q++){
        for (int w = 1; w <= n; w++){
            for (int e = 1; e <= n; e++){
                dp[w][e] = min(dp[w][e], dp[w][q] + dp[q][e]);
            }
        }
    }


    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            cout << (dp[i][j] != INF ? dp[i][j] : 0)  << " ";
        cout << '\n';
    }
}
