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

And this simple DS that just takes a few minutes to code helps immensely with our ability to separate into connected components or in this case, disjoint sets of email owners.

```python
'''
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
'''
def merge_accounts(accounts: List[List[str]]) -> List[List[str]]:
  uf = UnionFind(len(accounts))
  owner_of = {}

  for i, (_, *emails) in enumerate(emails):
    for email in emails:
      if email in owner_of: # i.e. we've encountered this email before (!! means there's a similarly named owner with this common email in it, merge those accounts)
        uf.union(i, owner_of[email])
      owner_of[email] = i

  # need this so we can use .append()
  combined_owners = defaultdict(list)
  for email, owner in owner_of.items():
    combined_owners[uf.find(owner)].append(email)

  return [[accounts[i][0]] + sorted(emails) for i, emails in combined_owners.items()]

```

Since union-find gives us very great bounds on runtime due to the inverse Ackermann function $\alpha(n)$ in $O(m \ \alpha(n))$, where $m$ is the total number of `find`, `union` operations combined (in textbooks there's typically a separate `make-set` operation but we initialize everything here to be its own set in the array to start in `__init__`), then we can say that this algorithm is linear in the number of email accounts, $O(m)$.
