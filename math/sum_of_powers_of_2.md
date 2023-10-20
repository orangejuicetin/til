# Binary representation proof

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

And if we subtract 1 from this, we get:

$$
1\underbrace{0.....0}_\text{n+1} - 1 = \underbrace{11.....1}_\text{n+1}
$$

Voilà! We've arrived at the answer of $2^{n+1} - 1 = \sum_{k=0}^n 2^k$
