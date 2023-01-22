#include <iostream>
#include <cmath>
using namespace std;
int main()
{
      long double n, m, a,temp;

  //  cout << "enter the numbers\n";
    cin >> n >> m >> a;
cout.precision(22);
    if (m < n) {
        temp = m;
        m = n;
        n = temp;
    }
    if (a >= m) {
        cout << ceil(m / a);
    }
    else {
        cout << ceil(m / a) * ceil(n / a);
    }
//printf("without extra_space:%d\n left land:%d\n tile should be added:%d\n &d on m and %d on n", (n / a) * (m / a), (n * m) - (a * a) * (n / a) * (m / a) , 0);
     long c1 = 0, c2 =0, i = 0;
   
        return 0;// ((n * m) % (a * a) == 0) ? (n / a) * (m / a) : c1 * c2;
}
