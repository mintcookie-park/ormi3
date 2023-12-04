#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int arr[101][101];
    bool visit[101][101];
    int side[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
    for(int i=0;i<picture.size();i++)
    {
        for(int j=0;j<picture[i].size();j++)
        {
            arr[i][j]=picture[i][j];
            visit[i][j]=false;
        }
    }
    
    queue<pair<int,int>> q;
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(visit[i][j]==false&&arr[i][j]!=0)
            {
                number_of_area++;
                int area=1;
                q.push(make_pair(i,j));
                visit[i][j]=true;
                while(!q.empty())
                {
                    int y=q.front().first; int x=q.front().second;
                    q.pop();
                    for(int k=0;k<4;k++)
                    {
                        int ny=y+side[k][0];
                        int nx=x+side[k][1];
                        if(ny>=0&&nx>=0&&ny<m&&nx<n&&visit[ny][nx]==false
                          &&arr[y][x]==arr[ny][nx])
                        {
                            visit[ny][nx]=true;
                            q.push(make_pair(ny,nx));
                            area++;
                        }
                    }
                    
                }
                max_size_of_one_area=max(max_size_of_one_area,area);
                
            }
        }
    }
     
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}