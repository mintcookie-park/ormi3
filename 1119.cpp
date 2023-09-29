#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
vector<int> v[50];
bool visited[50];
int dfs(int now){
    int ret = 1;
    for(int next : v[now]){
        if(visited[next]) continue;
        visited[next]=true;
        ret+=dfs(next);
    }
    return ret;
}
int main(){
    int N;cin>>N;
    if(N==1){
        cout<<"0"<<"\n";return 0;
    }
    int cnt = 0;
    for(int i=0;i<N;i++){
        string a;cin>>a;
        for(int t=0;t<a.length();t++){
            if(a[t]=='Y'){
                v[i].push_back(t);cnt++;
            }
        }
    }
    fill(visited,visited+50,false);
    cnt/=2;
    vector<int> s;
    for(int i=0;i<N;i++){
        if(!visited[i]){
            visited[i]=true;
            s.push_back(dfs(i));
        }
    }
    
    int sum = 0;
    for(int a : s){
        sum+=a-1;
        if(a==1){
            cout<<"-1"<<"\n";return 0;
        }
    }
    if(s.size()-1<=cnt-sum){
        cout<<s.size()-1<<"\n";
    }else{
        cout<<"-1"<<"\n";
    }
}