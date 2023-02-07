// @active_botane every day
#include <bits/stdc++.h>
#define endl '\n'
#define all(x) x.begin(), x.end()
typedef long long ll;
typedef long double ld;
using namespace std;


int main() {
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	
	vector <int> num(2000);
    queue <pair<int, int>> qu;
    qu.push({1, 6});
    qu.push({2, 6});
    qu.push({3, 6});

    int now = 1;
    while (now < 1500){
        int np = qu.front().first;
        int d = qu.front().second;
        for (int i = 0; i <= min(d, 4); ++i){
            num[now] = np;
            now++;
            d--;
        }
        
        qu.pop();
        if (d == 0) qu.push({np, 6});
        else qu.push({np, d});
    }

    cout << num[111] << " " << num[211] << " " << num[311] << endl;
 
	cerr << "Time: " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl;
	return 0;
}
