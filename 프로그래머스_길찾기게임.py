import sys
sys.setrecursionlimit(10**6) # 파이썬 재귀 limit 늘려주는 코드

# y좌표가 가장 큰 노드
def find_root(nodes):
    return max(nodes, key=lambda x:x[2])

# 루트를 중심으로(x좌표) 두 노드로 나눔, nodes는 x좌표로 정렬된 리스트
def divide_nodes(nodes, y):
    for i, node in enumerate(nodes):
        if y == node[2]:
            # root를 제외하고 두 리스트로 분리
            return nodes[:i], nodes[i + 1:]

def solution(nodeinfo):
    nodes = [(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    root, tree = -1, {}
    
    def make_tree(nodes, p):
        if not nodes: return
        i, x, y = find_root(nodes)
        if p == -1:
            nonlocal root
            root = i
        else:
            tree[p].append(i)
        tree[i] = []
        x_nodes = sorted(nodes, key=lambda x:x[1])
        left_nodes, right_nodes = divide_nodes(x_nodes, y)
        make_tree(left_nodes, i)
        make_tree(right_nodes, i)
    
    make_tree(nodes, -1)
    
    pre_list = []
    def preorder(parent):
        pre_list.append(parent)
        for child in tree[parent]:
            preorder(child)
    
    post_list = []
    def postorder(parent):
        for child in tree[parent]:
            postorder(child)
        post_list.append(parent)
    
    preorder(root)
    postorder(root)
    
    answer = [pre_list, post_list]
    return answer