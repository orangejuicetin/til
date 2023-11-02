# Ackermann function

I mentioned the inverse of this function in the other TIL I wrote concerning [union-find](/ds_algos/union_find.md), but the Ackermann function is an _insane_ function that basically grows incredibly quickly, with its inverse subsequently growing extraordinarily slowly.

$\exists$ many different definitions for this function, but in CLRS it's defined recursively using functional-iteration notation as:

$$
A_k(j) =
\begin{cases}
j + 1 & \text{if}\ k = 0 \\
A_{k-1}^{(j+1)}(j) & \text{if}\ k \geq 1
\end{cases}
$$

for $j \geq 1$ and $k \geq 0$

Which is confusing to read, but to put it in perspective for you, if we just set $j = 1$ and solely iterate $k$:

$$
\displaylines{
  A_0(1) = 1 \\
  A_1(1) = 3 \\
  A_2(1) = 7 \\
  A_3(1) = 2047 \\
  A_4(1) \gg 10^{80}
}
$$

Where $10^{80}$ is the estimated number of _atoms in the observable universe_ (!!!)

The inverse of this function that we used in the analysis of runtime for union-find is $\alpha(n) = min\{k : A_k(1) \geq n\}$, i.e. $\alpha(n) = 4$ for $2048 \leq n \leq A_4(1)$, so for all practical purposes $\alpha(n) \leq 4$ (unless you're working with some galactic inputs in [galactic algorithms](https://en.wikipedia.org/wiki/Galactic_algorithm) !\_!) and it gives us wonderful abilities to bound union-find's runtime to linear.
