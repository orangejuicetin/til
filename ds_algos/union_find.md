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

## 11/15/23

Another problem that fits the bill, this time a LC Hard with [#2092](https://leetcode.com/problems/find-all-people-with-secret/description/) figuring out how many people know a given secret at the end. The confusing part of this is where the `meetings` list of lists can have one person in multiple different meetings at once and multiple items with the same timestamp in various ordreings.

This is where union-find comes in for us to be able to find which disjoint-sets of people are in cahoots with each other at a given time. And at each time, we can check if there's any overlap with one of those sets and who already is in the know for a given secret, and add them appropriately to the growing set of people `who_knows`.

```python
import collections

class UnionFind:
    def __init__(self):
        self.parents = {}
        self.rank = {}

    def insert(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.rank[x] = 0

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        self.insert(x)
        self.insert(y)
        if (xp := self.find(x)) != (yp := self.find(y)):
            if self.rank[xp] > self.rank[yp]:
                self.parents[yp] = xp
            else:
                self.parents[xp] = yp
                if self.rank[xp] == self.rank[yp]:
                    self.rank[yp] += 1

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # sort meetings by last timestamp (O n lg n)
        who_knows = set([0, firstPerson])
        meetings_at = collections.defaultdict(list)
        for a, b, time in meetings:
            meetings_at[time].append((a, b))
        meetings_at = sorted(meetings_at.items())
        for _, pairings in meetings_at:
            uf = UnionFind()
            for a, b in pairings:
                uf.union(a, b)

            groups = collections.defaultdict(set)
            for person in uf.parents:
                groups[uf.find(person)].add(person)
            for group in groups.values():
                if group & who_knows:
                    who_knows.update(group)

        return list(who_knows)

```

This union-find implementation was also slightly different for the last one in which we didn't instantiate the array of `rank` right away since we didn't have a static number – in this case we can dynamically insert members.
