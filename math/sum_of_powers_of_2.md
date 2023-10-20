# Sum of Powers of 2, binary intuition

$$
\sum_{k=0}^n 2^k = 2^{n+1} - 1
$$

doesn't seem too intuitive at first, and even after doing the induction proof, the intuition still doesn't come through, but what really helped make it click for me was thinking of it in terms of binary. If we turn this sum into a binary representation, we just get:

$$
\underbrace{11.....1}_\text{n+1}
$$

where the very first 1 represents:

$$
\underset{2^n}{\underline{1}}1.....1
$$

etc., etc., and this represents our sum. How could we arrive at this otherwise? Well, $2^{n+1}$ is:

$$
1\underbrace{0.....0}_\text{n+1}
$$

where that first 1 is:

$$
\underset{\scriptscriptstyle{2^{n+1}}}{\underline{1}}0.....0
$$

And if we subtract 1 from this? We get:

$$
\underbrace{11.....1}_\text{n+1}
$$

Voilà! We've arrived at the answer of

$$
2^{n+1} - 1 = \sum_{k=0}^n 2^k
$$

Applications: helps us count number of total nodes in a complete binary tree, and reason about why if we take away all the leaves (of which there are at most $2^n$ in this case since the max height is $k = n$), we have half the original nodes remaining, i.e. the leaves make up _half_ the nodes of the tree (!!)
