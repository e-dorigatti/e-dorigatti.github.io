---
title: "A tricky question"
layout: post
date: 2020-05-26 09:00:00 +0200
markdown: kramdown
highlighter: rouge
categories:
 - Riddles
 - Linear Programming
 - Python
---

A few ~~days~~ months ago (took me a while to wrap this up) I stumbled upon this
question on the internet:

> Which answer in this list is the correct answer to _this_ question?
>
>  1. All of the below,
>  2. None of the below,
>  3. All of the above,
>  4. One of the above,
>  5. None of the above, or
>  6. None of the above.

<!-- more -->

This can be answered easily by formalizing the answers, and analyzing each one
in turn. We hope to find inconsistencies that allow us to rule out each answer,
except for the right one. In other words, if we fix some assumptions (i.e., a
that certain answer is correct), and manage to find a contradiction in the
subsequent reasoning, we can be sure that these assumptions cannot be all
correct simultaneously. [This
technique](https://en.wikipedia.org/wiki/Proof_by_contradiction) was developed
by Aristotle, and is frequently used in proofs in math and logic.

Let me use the letters $A$ through $F$ to denote boolean variables associated
with each answer, so that a variable is true if and only if the corresponding
answer is correct. We can now translate the anwers in the language of logic:

$$
\begin{align*}
A &\Leftrightarrow B \land C\land D \land E \land F \\
B &\Leftrightarrow \lnot C \land\lnot D \land\lnot E \land\lnot F \\
C &\Leftrightarrow A \land B \\
D &\Leftrightarrow A \lor B \lor C \\
E &\Leftrightarrow \lnot A \land\lnot B \land\lnot C \land\lnot D \\
F &\Leftrightarrow \lnot A \land\lnot B \land\lnot C \land\lnot D \land\lnot E
\end{align*}
$$

Where $\lnot$ means _not_, $\land$ means _and_, $\lor$ means _or_ and
$\Leftrightarrow$ means _if and only if_. Let's now analyze each answer, looking
for inconsistencies. If we assume $A$ is true, then both $B$ and $C$ must be
true. However, $B$ asserts that $C$ is false! This contradicts $A$, therefore
$A$ cannot be true. Now suppose that $B$ is true. Because of it, $D$ is false.
However, $\lnot D=\lnot A \land \lnot B \land \lnot C$ (because of [De Morgan's
Law](https://en.wikipedia.org/wiki/De_Morgan%27s_laws)), i.e. if $D$ is false
then $B$ must also be false, which is inconsistent with our assumption. We can
easily rule out $C$, as we concluded that both $A$ and $B$ are false, and this
allows us to exclude $D$ as well. We now know that $A$, $B$, $C$ and $D$ are
false, which is exactly what answer $E$ tells us. Finally, $F$ asserts that all
others are wrong, which is not true since we have seen that $E$ is true.

Therefore, the correct answer is the fifth one.

Note that we could simplify the reasoning a bit if we assume that only one
answer is correct, which seem to be implied by the question. This would allow us
to discard $A$ and $C$ straight away, because they assert that more than one
answer is correct.

I am now going to show you how to formulate this question as an integer linear
program and write a Python program to find the solution for us.

## As an integer linear program
A linear program, in general, is an optimization problem of the following form:

$$
\begin{align*}
\text{Maximize}
 & \quad c_1x_1+\ldots+c_nx_n \\
\text{Subject to}
 & \quad a_{11}x_1+\ldots+a_{1n}x_n\leq b_1 \\
 & \quad\ldots \\
 & \quad a_{m1}x_1+\ldots+a_{mn}x_n\leq b_m
\end{align*}
$$

If the unknowns are constrained to be integers, we obtain an _integer_ linear
program (ILP, from now on), where the term _linear_ highlights the fact that
both the objective and the constraints are linear forms. It is important to keep
in mind that only the $x$'s are allowed to change, while $a$'s, $b$'s and $c$'s
must be fixed.

If we use the integers 0 and 1 to denote false and true variables, we can
express logical statements as numerical formulas:

$$
\begin{align*}
A \land B &\Leftrightarrow x_A\cdot x_B\geq 0.5 \\
A \land B \land C &\Leftrightarrow x_A+x_B+x_C - 2.5 \geq 0 \\
A \lor B \lor C &\Leftrightarrow x_A+x_B+x_C - 0.5 \geq 0 \\
\lnot A &\Leftrightarrow 0.5-x_A \geq 0
\end{align*}
$$

Where we use $x_A$, $x_B$ and $x_C$ to indicate the number associated to $A$,
$B$ and $C$. We also use 2.5 and 0.5 instead of 3 and 1 to avoid numerical
issues. Even though the general ILP formulation shown above does not contain
products between variables, it is possible to express the product of _two binary
variables_ in a suitable way (see at the end of the post to know how). This is
unfortunately not possible for more than two variables.

From these, we can obtain useful equivalences for negations:

$$
\begin{align*}
\lnot(A \land B \land C) &\Leftrightarrow 2.5-x_A-x_B-x_C \geq 0 \\
\lnot(A \lor B \lor C) &\Leftrightarrow 0.5-x_A-x_B-x_C \geq 0 \\
\end{align*}
$$

Finally, a last useful equality is to convert the _if and only if_ part to a
simpler equivalent in terms of only _and_, _or_, and _not_:

$$
A\Leftrightarrow B \equiv (A\land B)\lor (\lnot A\land \lnot B)
$$

Now, the main idea is to use a separate constraint to encode each answer in an
ILP. Since all constraints must be satisfied for a solution to be valid, the ILP
solver is forced to avoid selecting an answer that would generate a
contradiction, because this would violate one of the other constraints. Pretty
much like what we did above.

Consider the third answer:

$$
C\Leftrightarrow A\land B
$$

we first remove the _if and only if_:

$$
(C \land (A\land B))\lor(\lnot C\land\lnot(A\land B))
$$

Then we convert this to a constraint using the rules above:

$$
x_C\cdot(x_A+x_B-1,5) + (1-x_C)\cdot(1.5-x_A-x_B)\geq 0
$$

The other answers are converted in the same way. Try to do a few yourself to
make sure you get it.

*Really, try.*

The ILP is below. For clarity, I will not simplify the expressions nor linearize
the binary products, but it should be done, eventually. We also use a dummy
variable $q$ as our objective since, strictly speaking, there is nothing to
maximize here.

$$
\begin{align*}
\text{Maximize}\quad
 & q \\
\text{Subject to}\quad
 & x_A (x_B+x_C+x_D+x_E+x_F-4.5) \\
 & \qquad +(1-x_A)(4.5-x_B+x_C+x_D+x_E+x_F)\geq 0 \\
 & x_B (0.5-x_C-x_D-x_E-x_F) \\
 & \qquad (1-x_B)(x_C+x_D+x_E+x_F-0.5)\geq 0\\
 & x_C(x_A+x_B-1.5) \\
 & \qquad (1-x_C)(1.5-x_A-x_B)\geq 0 \\
 & x_D(x_A+x_B+x_C-0.5) \\
 & \qquad (1-x_D)(0.5-x_A-x_B-x_C)\geq 0 \\
 & x_E(0.5-x_A-x_B-x_C-x_D) \\
 & \qquad (1-x_E)(x_A+x_B+x_C+x_D-0.5)\geq 0 \\
 & x_F(0.5-x_A-x_B-x_C-x_D-x_E) \\
 & \qquad (1-x_F)(x_A+x_B+x_C+x_D+x_E)\geq 0 \\
 & x_A,x_B,x_C,x_D,x_E,x_F\in\{0,1\} \\
 & q\in\mathbb{R}
\end{align*}
$$

## Finding a solution in Python
It is now very easy to encode and solve this model in Python with the help of
[pyomo](https://www.pyomo.org/). Pyomo is actually just a frontend towards
external ILP solvers (I use [Gurobi](https://www.gurobi.com/)), but it offers a
very pythonic interface. Importantly, it takes care of tricks such as the
linearization trick for products of two binary variables, simplifies and removes
redundant constraints, and much more. Here is the code:

```python
import pyomo.environ as aml
from pyomo.opt import SolverFactory

# this is an empty model
model = aml.ConcreteModel()

# we create a binary variable for each answer
model.A = aml.Var(domain=aml.Binary, initialize=0)
model.B = aml.Var(domain=aml.Binary, initialize=0)
model.C = aml.Var(domain=aml.Binary, initialize=0)
model.D = aml.Var(domain=aml.Binary, initialize=0)
model.E = aml.Var(domain=aml.Binary, initialize=0)
model.F = aml.Var(domain=aml.Binary, initialize=0)

# we now create one constraint for each answer
# the parameter to the lambda is the model itself,
# through which we can access the variables

model.Answer1 = aml.Constraint(rule=lambda m: (
    m.A * (m.B + m.C + m.D + m.E + m.F - 4.5)
    + (1 - m.A) * (4.5 - m.B - m.C - m.D - m.E - m.F)
) >= 0)

model.Answer2 = aml.Constraint(rule=lambda m: (
    m.B * (0.5 - m.C - m.D - m.E - m.F
    ) + (1 - m.B) * (m.C + m.D + m.E + m.F - 0.5)
) >= 0)

model.Answer3 = aml.Constraint(rule=lambda m: (
    m.C * (m.A + m.B - 1.5)
    + (1 - m.C) * (1.5 - m.A - m.B)
) >= 0)

model.Answer4 = aml.Constraint(rule=lambda m: (
    m.D * (m.A + m.B + m.C - 0.5)
    + (1 - m.D) * (0.5 - m.A - m.B - m.C)
) >= 0)

model.Answer5 = aml.Constraint(rule=lambda m: (
    m.E * (0.5 - m.A - m.B - m.C - m.D)
    + (1 - m.E) * (m.A + m.B + m.C + m.D - 0.5)
) >= 0)

model.Answer6 = aml.Constraint(rule=lambda m: (
    m.F * (0.5 - m.A - m.B - m.C - m.D - m.E)
    + (1 - m.F) * (m.A + m.B + m.C + m.D + m.E - 0.5)
) >= 0)

# this is the dummy objective
model.Objective = aml.Objective(
    rule=lambda m: 1,
    sense=aml.maximize
)

# we now obtain the interface to the gurobi solver
solver = SolverFactory('gurobi')

# solve the model
solver.solve(model)

# and print the values of the variables in the solution
print('    '.join(
    '{}: {:+}'.format(var, getattr(model, var).value)
    for var in 'ABCDEF'
))

```

As you can see, the constraints are specified exactly as in the almost-formal
ILP formulation above. It is also possible to have indexed variables (like
arrays) and use `sum` (the built-in) to express sums over elements of an
iterable. It does not feel like doing math at all.

This script eventually outputs

```
A: +0.0    B: -0.0    C: +0.0    D: -0.0    E: +1.0    F: +0.0
```

As expected.

## Linearizing products of binary variables
As promised, this is how we can linearize the product of two binary variables.
Assume we want to express the constraint $z=x\cdot y$, with $x$, $y$ and $z$
binary variables. This can be done as follows:

$$
\begin{align*}
z &\leq x \\
z &\leq y \\
z &\geq x + y - 1
\end{align*}
$$

Where the first two constraints ensure that $z$ is zero whenever either one of
$x$ and $y$ are zero, while the third constraints makes sure that $z$ is one
when both $x$ and $y$ are one. This can be extended to sums of product pairs by
introducing an auxiliary variable for each product pair. Consider this
constraint:

$$
x_7=\underbrace{x_1x_2}_{z_1}+\underbrace{x_3x_4}_{z_2}+\underbrace{x_5x_6}_{z_3}
$$

In an ILP, it should be replaced by these eleven:

$$
\begin{align*}
\text{Equality for }x_7 & \left\{\begin{array}{l}
x_7\geq z_1+z_2+z_3 \\
x_7\leq z_1+z_2+z_3
\end{array}\right. \\

z_1 \text{ for the first product} & \left\{ \begin{array}{l}
z_1\leq x_1 \\
z_1\leq x_2 \\
z_1\geq x_1+x_2-1
\end{array}\right. \\

z_2 \text{ for the second product} & \left\{\begin{array}{l}
z_2\leq x_3 \\
z_2\leq x_4 \\
z_2\geq x_3+x_4-1
\end{array}\right. \\

z_3 \text{ for the third product} & \left\{\begin{array}{l}
z_3\leq x_5 \\
z_3\leq x_6 \\
z_3\geq x_5+x_6-1 \\
\end{array}\right. \\
\end{align*}
$$

Fortunately, most modern ILP solvers can perform this substitution for us.

