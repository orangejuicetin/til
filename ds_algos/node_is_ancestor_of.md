# Node is ancestor of \_\_\_\_

Did as a mock interview question with @jab and I thought it was a wonderful question to kind of discuss all kinds of tradeoffs to make and branches (hah) you could go down to code it up.

Reminder to self to be able to identify quicker areas where you could've optimized (originally came up with storing a list of ancestors when in reality you only need to track just your parent and recurse upwards in order to find if ancestry is there).

```python
# Problem:
# Implement the following API:
# TreeNode.is_ancestor_of(self, other) -> bool:
#     pass

from __future__ import annotations # deferred evaluation of type hints !!
import collections

class TreeNode:


    def __init__(self, parent: TreeNode):
        self.children = []
        self.parent = parent
        self.depth = parent.depth + 1


    def is_ancestor_of(self, other: TreeNode) -> bool:
        # q = collections.deque(self.children)
        # while q:
        #     node = q.popleft()
        #     if other == node:
        #         return True
        #     else:
        #         for child in node.children:
        #             q.append(child)
        # return False
        if other.depth < self.depth:
            return False

        if other.parent is None:
            return False
        if other.parent is self:
            return True
        else:
            return self.is_ancestor_of(other.parent)

```

A last follow up after getting to this step however was Josh asking me if there was a way to improve it to $O(1)$ time as well as $O(n)$ space (currently takes $O(\log n)$ and $O(n)$ space). Stumping me for a bit, thought I could maybe take the path-compression approach from union-find but realized it doesn't handle the case of siblings/separate subtrees very well.
