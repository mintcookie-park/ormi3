#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> data) {
    int answer = 0;
    
    sort(data.begin(),data.end());
    
    for(int i=0;i<n;i++) {
        int x = data[i][0];
        int y = data[i][1];
        
        for(int j=i+1;j<n;j++) {
            int nx = data[j][0];
            int ny = data[j][1];
            
            if(x==nx || y==ny) {
                continue;
            }
            
            int maxY = y > ny ? y : ny;
            int minY = y > ny ? ny : y;
            
            bool tf = true;
            for(int k=i+1;k<j;k++) {
                int tx = data[k][0];
                int ty = data[k][1];
                
                if(tx>x && tx<nx && ty>minY && ty<maxY) {
                    tf = false;
                    break;
                }
            }
            
            if(tf) {
                answer++;
            }
        }
    }
    
    return answer;
}