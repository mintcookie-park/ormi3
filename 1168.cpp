#include <iostream>

using namespace std;

int n, k;

int segment[300000];

int init(int start, int end, int node)
{
	if (start == end) 
		return segment[node] = 1;
	
	int mid = (start + end) / 2;
	return segment[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
}

int get_num_and_update(int start, int end, int node, int index)
{
	segment[node]--;
	if (start == end) 
		return start;
	
	int mid = (start + end) / 2;
	if (index > segment[node * 2]) 
		return get_num_and_update(mid + 1, end, node * 2 + 1, index - segment[node * 2]);
	else 
		return get_num_and_update(start, mid, node * 2, index);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> n >> k;

	init(1, n, 1);
	int idx = k - 1;
	cout << "<";
	for (int i = 1; i <= n; i++) {
		int get_idx = get_num_and_update(1, n, 1, idx + 1);
		
		if (i != n) 
			cout << get_idx << ", ";
		else 
			cout << get_idx;

		if (segment[1] == 0)
			break;

		idx += k - 1;
		idx %= segment[1];
	}
	cout << ">";
	return 0;
}