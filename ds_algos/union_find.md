# Union-find

Starting this here since it feels like all my leetcode is going to waste if I don't take some notes...

Used union-find in [#721, Accounts Merge](https://leetcode.com/problems/accounts-merge/) as a clever way around my much clunkier solution of just manually iterating through and comparing emails using lists of sets. In this case we use this data structure:

```python
class UnionFind:
  def __init__(self, n):
    self.rank_of = [1] * n # "height" of a given node in our union-find tree
    self.parent_of = list(range(n))

  # path compression, optimization one of union-find data structure
  def find(self, u):
    if not u == self.parent[u]:
      self.parent[u] = self.find(self.parent[u])
    return self.parent[u]

  def union(self, u, v):
    root_u = self.parent[u]
    root_v = self.parent[v]

    if self.rank_of[root_u] == self.rank_of[root_v]:
      self.parent_of[root_u] = root_v
      self.rank_of[root_v] += 1
    # in the latter two cases, no need to increase rank since one is already greater
    elif self.rank_of[root_u] > self.rank_of[root_v]:
      self.parent_of[root_v] = root_u
    else:
      self.parent_of[root_u] = root_v
```

And this simple DS that just takes a few minutes to code helps immensely with our ability to separate into connected components or in this case, disjoint sets of email owners. Since we $O(\log n)$ lookup times with `find` and `union` takes $O(1)$ time,
