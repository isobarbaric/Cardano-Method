# cardano-method

[![release](https://img.shields.io/badge/dynamic/json.svg?label=release&url=https://pypi.org/pypi/cardano-method/json&query=%24.info.version&colorB=blue)](https://pypi.org/project/cardano-method/)

A fast, reliable Python library to solve cubic equations of all kinds. You can test out `cardano-method` [in your browser](https://replit.com/@Vndom/CardanoMethod-Playground#main.py).

- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Underlying Mathematics](#underlying-mathematics)

## How It Works

`cardano-method` implements Gerolamo Cardano's famous method of solving cubic equations - 'Cardano's Method'. Split amongst various stages of processing, this library **mirrors the steps described in Cardano's Method** to solve for the roots of a cubic equation.

For a more detailed explanation of the specifics, please refer to the [succeeding section](#underlying-mathematics) discussing the underlying mathematics.

## Installation
```
$ pip install cardano-method
```

## Usage
```python
from cardano_method import CubicEquation

a = CubicEquation([1, 3, 4, 4])

print(a.answers)
# [(-2+0j), (-0.5+1.322875j), (-0.5-1.322875j)]
```

Note that the ``answers`` attribute contains a list of [`complex`](https://docs.python.org/3/library/cmath.html#module-cmath) objects representing the zeroes of the cubic equation.

## Underlying Mathematics

Let's say the original cubic was $p(x)$:

$$p(x) = \sum_{i=0}^3 a_ix^i = a_3x^3 + a_2x_2 + a_1x_1 + a_0$$

Cardano Method is applied to a depressed cubic polynomial. Depressed polynomials are those where the coefficient of the $x^{n-1}$ term is zero.

We can use context from Vieta's relations to construct this depressed polynomial,
$$\Rightarrow p\left(x-\frac{a_2}{3a_3}\right) = q(x) = a_3x^3 + x\left(a_1-\frac{a_2^2}{3a_3}\right) + \left[\frac{2a_2^3}{27a_3^2} - \frac{a_1a_2}{3a_3} + a_0\right]$$

Notice how the the $x^2$ term is absent from the expansion, i.e. the coefficient of $x^2$ is 0.

From here, to simplify things a bit, let's introduce some variables: (after dividing away to leave a coefficient of 1)
$$3H = \frac{\left(a_1-\frac{a_2^2}{3a_3}\right)}{a_3} \text{ and } G = \frac{\left[\frac{2a_2^3}{27a_3^2} - \frac{a_1a_2}{3a_3} + a_0\right]}{a_3}$$

Here, we make an interesting construction. Assume some arbitrary $x$ is a root of $q$. Then, let $x = u^{\frac{1}{3}} + v^{\frac{1}{3}}$. Attempting to recreate the original polynomial with this root:
$$x^3 = (u^\frac{1}{3} + v^\frac{1}{3})^3$$
$$x^3 = u+v+3u^\frac{1}{3}v^\frac{1}{3}(u^\frac{1}{3}+v^\frac{1}{3})$$
$$\Rightarrow x^3-3u^\frac{1}{3}v^\frac{1}{3}x-(u+v) = 0$$

Equating the final polynomial to the original polynomial, we get $uv = -H^3$, $u+v = -G$. Solving for $u, v$ with a quadratic equation, we can go back to our original $x = u^{\frac{1}{3}} + v^{\frac{1}{3}}$ and find the following roots for our polynomial:

$$\{\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}} - \frac{H}{\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}} - \frac{a_2}{3a_3},  \sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}\omega - \frac{H\omega^2}{\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}} - \frac{a_2}{3a_3}, \\ 
\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}\omega^2 - \frac{H\omega}{\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}} - \frac{a_2}{3a_3} \}$$

If this looks complicated, don't worry - we agree too! The CardanoMethod package's ``CubicEquation`` handles all of this on the back-end and abstracts away all of the complex math.
