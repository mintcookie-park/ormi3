#include <iostream>
#include <string>
using namespace std;

int main() {
	string L, R;
	int min = 0;
	
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> L >> R;

	// 1. 두 숫자의 자릿수가 다른 경우 : 값 = 0
	if (L.size() != R.size()) {
		cout << 0;
	}

	// 2. 두 숫자의 자릿수가 같은 경우
	else {
		for (int i = 0; i < L.size(); i++) {
			// 해당 자리의 값이 같지 않으면 for문 종료
			if (L[i] != R[i]) {
				break;
			}

			// 해당 자리의 숫자가 8로 같은 경우
			// 8이 무조건 하나 있는 것이므로 min++
			if (L[i] == R[i] && L[i] == '8') {
				min++;
			}
		}

		cout << min;

	}

	return 0;
}