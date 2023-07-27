def count_balanced_strings(n, d):
    MOD = 10**9 + 7
    dp = [1]*26
    for _ in range(n-1):
        dp_new = [0]*26
        for j in range(26):
            for k in range(max(0, j-d), min(26, j+d+1)):
                dp_new[j] = (dp_new[j] + dp[k]) % MOD
        dp = dp_new
    return sum(dp) % MOD


def count_balanced_strings(n, d):
    MOD = 10**9 + 7
    dp = [1]*26
    for _ in range(n-1):
        dp_new = [0]*26
        for j in range(26):
            for k in range(max(0, j-d), min(26, j+d+1)):
                dp_new[j] = (dp_new[j] + dp[k]) % MOD
        dp = dp_new
    return sum(dp) % MOD


class UnionFind:
    def __init__(self, n):
        # Initially, each node is its own parent (i.e., each node forms its own disjoint set)
        self.parent = list(range(n))

        # The rank of a node is a measure of the depth of the tree rooted at that node.
        # It is used for balancing the trees to optimize the operations.
        self.rank = [0] * n

        # Keep track of the number of disjoint sets (initially, each node is its own set, so the count is n)
        self.count = n

    def find(self, x):
        # If x is not the parent of itself, then it means x is not the representative of its set (i.e., it is not the root of the tree).
        # So we recursively call find on its parent until we find the representative of the set (the root of the tree).
        # Along the way, we update each node's parent to the representative of the set (this is called "path compression" and it speeds up future operations).
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the representatives (roots of the trees) for x and y
        px, py = self.find(x), self.find(y)

        # If x and y are in different sets, then we need to merge the sets
        if px != py:
            # The tree with the higher rank becomes the parent of the other tree
            # This keeps the trees as balanced as possible, which ensures that operations are efficient
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[px] = py
                # If the ranks are equal, then it doesn't matter which tree becomes the parent
                # But we need to increase the rank of the resulting tree, because its depth has increased
                if self.rank[px] == self.rank[py]:
                    self.rank[py] += 1
            # Since we've merged two sets, the number of disjoint sets has decreased by one
            self.count -= 1


def solve(n, k, edges):
    # Sort edges in decreasing order of weight
    edges.sort(key=lambda x: -x[2])

    uf = UnionFind(n)
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            if uf.count == k:
                return w
    return -1


# Test the function
print(solve(4, 2, [(0, 1, 1), (1, 2, 2), (2, 3, 3)]))  # Expected output: 2
# Expected output: 1
print(solve(5, 1, [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4)]))


print(count_balanced_strings(2, 1))  # Expected output: 52
print(count_balanced_strings(3, 1))  # Expected output: 78
print(count_balanced_strings(4, 1))  # Expected output: 104
print(count_balanced_strings(2, 2))  # Expected output: 78
