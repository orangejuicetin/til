# Intuition of variance

$$
Var[X] = E[(X - E[X])^2]
$$

more intuitively, the expected squared distance from the mean. Why squared? It's not intuitive, but Gauss introduced it because it gives us nice properties (differentiable everywhere so we can apply Analysis to it, ties it into Chebyshev's inequality, etc.), and because if we didn't square it, the expected value would just be 0!

The alternate definition comes from continuing this expansion to derive the other well-known form:

$$
\begin{aligned}
&=& E[(X - E[X])^2] \\
&=& E[(X^2 - 2X(E[X]) + (E[X])^2)] \\
&=& E[(X^2)] - 2 E[X]E[X] + (E[X])^2 \\
&=& E[(X^2)] - 2 (E[X])^2 + (E[X])^2 \\
Var[X]&=& E[(X^2)] - (E[X])^2\\
\end{aligned}
$$
