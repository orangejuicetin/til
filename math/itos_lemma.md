# Itô's Lemma

Essental to Black-Scholes, and didn't realize there was a whole branch of calculus named after Kiyosi Itô that extends calculus to stochastic processes. The Itô stochastic integral is the core concept:

$$
Y_t = \int_0^t H_s dX_s
$$

In this case, the integrands/integrators are all stochastic processes. Itô's Lemma is then specifically meant to be the stochastic calculus counterpart to the _chain rule_.
