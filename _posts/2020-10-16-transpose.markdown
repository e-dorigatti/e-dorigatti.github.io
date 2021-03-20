---
title: "Who cares about transposes?"
layour: post
date: 2020-10-16 09:00:00 +0200
markdown: kramdown
highlighter: rouge
categories: Math
---

<style>
.hlbox {
    background-color: #aec6cf;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    margin-top: 30px;
    margin-bottom: 30px;
    padding: 30px;
    border-radius: 15px;
    width: 70%;
}

</style>

Exchanging rows and columns of a matrix is hardly an inspiring operation. Yet in linear algebra we frequently take the transpose of a matrix. Why is that?

<!-- more -->

To understand why the transpose is so important, we first need to understand two fundamental spaces associated with a matrix, the row space and the column space. To see why these two spaces are so important, let us work our way through an example.

## The column space
Consider the following matrix:

$$
A=\b{u}\t{\b{v}}=\vv{1}{3}\cdot\vh{2}{1}=\mq{2}{1}{6}{3}
$$

What does the linear transformation associated with $A$ look like? In other words, what is $A\b{x}$? By using the definition of $A$ in terms of $\b{u}$ and $\b{v}$, we see that:

$$
A\b{x}=\b{u}\cdot(\d{v}{x})
$$

Since $\d{v}{x}$ is a scalar (a number), $A\b{x}$ is just $\b{u}$ stretched by a certain amount, precisely $\d{v}{x}$.

Let's take some points and see where $A$ maps them:



![png](/images/transpose/output_3_0.png){: .center-image}



Each point in the grid is connected to the point that $A$ maps it to. There are a few interesting things to notice:

 1. The destination points all lie on a line parallel to $\b{u}$,
 2. Several points are mapped to the same location on the line, and
 3. The points that are mapped to the same location seem to be organized in rows that are parallel to the dotted line.

We showed the first point above. Every vector transformed by $A$ is "squashed" onto $\b{u}$. Any point that cannot be reached by stretching $\b{u}$, cannot be reached by transforming another point with $A$. Vice-versa, any point that can be reached by stretching $\b{u}$, can be reached by transforming a certain point with $A$.

The column space of $A$ is:

$$
\b{C}(A)=a\cdot\vv{2}{6}+b\cdot\vv{1}{3}=(a+2b)\cdot\vv{1}{3}=(a+2b)\cdot\b{u}
$$

For all possible choices of $a,b\in\mathbb{R}$. In English, the column space of $A$ contains all points that can be reached by stretching $\b{u}$. Does this sound familiar? It should!

<p class="hlbox">
 The column space of a matrix contains all vectors that result from multiplying a vector with that matrix.
</p>

## The row space

The third observation is the most interesting, let's focus on some examples:





![png](/images/transpose/output_6_0.png){: .center-image}



That seems to be the case: the points that are mapped to the same location seem to be organized in rows that are parallel to the dotted line. How can we find what the dotted line is?

Suppose we have two vectors $\b{x}$ and $\b{y}$ that are mapped to the same point, i.e. $A\b{x}=A\b{y}$. By plugging in the definition of $A$ we get

$$
\b{u}\d{v}{x}=\b{u}\d{v}{y}
$$

Since both of these vectors are parallel to $\b{u}$, we can discard it to obtain:

$$
\d{v}{x}=\d{v}{y}
$$

or, equivalently,

$$
\t{\b{v}}(\b{x}-\b{y})=0
$$

This means that $\b{x}$ and $\b{y}$ are mapped to the same point when the vector joining them, $\b{x}-\b{y}$ is orthogonal to $\b{v}$. And, vice-versa, if two vectors are mapped to the same point, then their difference is orthogonal to $\b{v}$.

Another way to look at this is that, given a vector $\b{x}$, we can find another vector $\b{y}$ that is mapped to the same point by $A$ simply by adding to $\b{x}$ a vector, say $\b{v}^\perp$, that is perpendicular to $\b{v}$. As a compact formula:

$$
A(\b{x}+\b{v}^\perp)=A\b{x}+A\b{v}^\perp=A\b{x}+\b{u}(\t{\b{v}}\b{v}^\perp)=A\b{x}+\b{u}\cdot 0=A\b{x}
$$

This vector $\b{v}^\perp$ corresponds exactly to the dotted line in the plot above!

Now, given any vector $\b{x}$, there is an unique way to decompose it into a component that is parallel to $\b{v}$ and a component that is orthogonal to it:

$$
\b{x}=a\cdot\b{v}+b\cdot\b{v}^\perp
$$





![png](/images/transpose/output_8_0.png){: .center-image}





And transforming such a vector with $A$ gives:

$$
A(a\cdot\b{v}+b\cdot\b{v}^\perp)=a(\t{\b{v}}\b{v})\cdot\b{u}
$$

Let's walk through a numerical example to see this more clearly.

First, given $\b{v}=\t{\vert 2,1\vert }$, its perpendicular is $\b{v}^\perp=\t{\vert -1,2\vert }$, since $2\cdot(-1)+1\cdot2=0$. Consider now a vector $\b{x}=\t{\vert 4,0\vert }$, we can write it in terms of $\b{v}$ and $\b{v}^\perp$:

$$
\b{x}=\vv{4}{0}=a\cdot\b{v}+b\cdot\b{v}^\perp
=\frac{8}{5}\cdot\vv{2}{1}-\frac{4}{5}\cdot\vv{-1}{2}
=\frac{1}{5}\left(\vv{16}{8}+\vv{4}{-8}\right)
$$

How to find those two numbers? Trivially, from the relation between dot-product and projections:

$$
\d{x}{v}=\d{v}{v}\cdot\d{x}{x}\cdot\cos\alpha
$$

Which means that the projection of $\b{x}$ onto $\b{v}$ and $\b{v}^\perp$ are given by:

$$
a=\frac{\d{x}{v}}{\d{v}{v}}=\frac{4\cdot 2+0\cdot1}{2\cdot 2+1\cdot 1}=\frac{8}{5}
$$

$$
b=\frac{\d{x}{v^\perp}}{\d{v}{v}}=\frac{4\cdot(-1)+0\cdot 2}{(-1)\cdot(-1)+2\cdot 2}=-\frac{4}{5}
$$

Consider now a second vector $\b{y}=\t{\vert 5,2\vert }$, by an entirely analoguous reasoning we find that

$$
\b{y}=\vv{5}{-2}=c\cdot\b{v}+d\cdot\b{v}^\perp=\frac{8}{5}\cdot\vv{2}{1}-\frac{8}{5}\cdot\vv{-1}{2}
$$



![png](/images/transpose/output_11_0.png){: .center-image}



Since $\b{x}$ and $\b{y}$ have the same component along $\b{v}$, as per our discussion above, we should have that $A\b{x}=A\b{y}$. Indeed:

$$
A\b{x}=\mq{2}{1}{6}{3}\cdot\vv{4}{0}=4\cdot\vv{2}{6}+0\cdot\vv{1}{3}=\vv{8}{24}
$$

$$
A\b{y}=\mq{2}{1}{6}{3}\cdot\vv{5}{-2}=5\cdot\vv{2}{6}-2\cdot\vv{1}{3}=\vv{8}{24}
$$

As we showed above, this happens because $A$ transforms the component parallel to $\b{v}$, and discards the component orthogonal to it. Let us verify this for $\b{x}$:

$$
A\cdot a\b{v}=\frac{8}{5}\cdot\mq{2}{1}{6}{3}\cdot\vv{2}{1}=\frac{8}{5}\cdot\vv{4+1}{12+3}=\vv{8}{24}
$$

$$
A\cdot b\b{v^\perp}=-\frac{4}{5}\cdot\mq{2}{1}{6}{3}\cdot\vv{-1}{2}=-\frac{4}{5}\cdot\vv{-2+2}{-6+6}=\vv{0}{0}
$$

As you can see, the result is in $A$'s column space, i.e. it is a stretched version of $\b{u}$. In fact:

$$
\vv{8}{24}=8\cdot\vv{1}{3}=\left(\frac{8}{5}\cdot 5\right)\cdot\vv{1}{3}=(a\cdot\d{v}{v})\cdot\b{u}
$$

As proved above.

Visually, these three vectors all go to the same place via $A$:



![png](/images/transpose/output_13_0.png){: .center-image}



The key take-away  of this discussion is that, as long as you stay on the blue line, different inputs are always mapped to different outputs. In other words, restricted to the blue and red lines, $A$ is injective, and therefore invertible!




![png](/images/transpose/output_15_0.png){: .center-image}



We already know that the red line is called _column space_ of $A$, and, similarly, the blue line is $\b{R}(A)$, the _row space_ of $A$.


<p class="hlbox">
  The row space of a matrix contains all vectors that are mapped to a different result by the matrix.
</p>

If a vector $\b{x}$ is outside of $\b{R}(A)$, we can find a corresponding vector $\b{y}$ in $\b{R}(A)$ such that $A\b{x}=A\b{y}$.

And, since we are fixing terms for core concepts,


<p class="hlbox">
 The null space of a matrix contains all vectors that are orthogonal to the row space.
</p>

Which is, in our example, none other than $\b{v}^\perp$.

## Okay, but I wanted to know about the transpose!

Alright, let's get to it! What does $\t{A}\b{x}$ look like?

$$
\t{A}\b{x}=\t{\left(\b{u}\t{\b{v}}\right)}\b{x}=\b{v}\cdot\left(\t{\b{u}}\b{x}\right)
$$

Remember that at the beginning we found that


$$
A\b{x}=\b{u}\cdot(\d{v}{x})
$$

They look remarkably similar! In fact, $\b{u}$'s and $\b{v}$'s roles are reversed. Obviously, $\b{C}(\t{A})=\b{R}(A)$ and $\b{R}(\t{A})=\b{C}(A)$, since we swap rows and columns, row space and column space are also swapped. But what does this mean? $\t{A}$ moves vectors parallel to $\b{u}$ onto vectors parallel to $\b{v}$, exactly the opposite of $A$.




![png](/images/transpose/output_18_0.png){: .center-image}



## So is the transpose just an inverse?

Well not exactly, but you can actually think of it like that (with some caution)! While a matrix maps vectors from its row space to its column space, its transpose goes in the reverse direction, from column space to row space.

What is missing for the transpose to be an actual inverse? Mathematically, we want to find out when

$$
\t{A}A\b{x}=\b{x}
$$

For $\b{x}$ in $\b{R}(A)$, i.e. $\b{x}=a\b{v}$. As we have seen before, $A(a\b{v})=a(\d{v}{v})\b{u}$, and, by symmetry, $\t{A}(b\b{u)}=b(\d{u}{u})\b{v}$. Substituting, we get:

$$
\t{A}A(a\b{v})=\t{A}\left(a(\d{v}{v})\b{u}\right)=a(\d{v}{v})(\d{u}{u})\b{v}
$$

Therefore, $\t{A}$ inverts $A$ when $\d{v}{v}\cdot\d{u}{u}=1$.

<p class="hlbox">
 Since $A$ introduces a certain amount of stretching, $\t{A}$ inverts $A$ (restricted on the row space) when it introduces a corresponding shrinkage.
</p>

Using our running example, to make sure the transpose is also the inverse, we simply need to rescale $\b{u}$ and $\b{v}$ to have unit length:

$$
\b{\bar{u}}=(\d{u}{u})^{-1/2}\b{u}=\frac{1}{\sqrt{10}}\cdot\vv{1}{3}
$$

$$
\b{\bar{v}}=(\d{v}{v})^{-1/2}\b{v}=\frac{1}{\sqrt{5}}\cdot\vv{2}{1}
$$

And the corresponding matrix is:

$$
\bar{A}=\b{\b{\bar{u}}}\t{\b{\bar{v}}}=\frac{1}{\sqrt{(\d{u}{u})(\d{v}{v})}}\b{u}\t{\b{v}}=\frac{1}{\sqrt{50}}\mq{2}{1}{6}{3}
$$

Now, $\bar{A}$ and $\t{\bar{A}}$ move things around but do not stretch them, i.e. they leave vector lengths unchanged, as long as we live and die inside $\b{R}(A)$ and $\b{C}(A)$. Vectors outside $\b{R}(A)$ are still stretched, because they are projected onto $\b{R}(A)$ before being launched into $\b{C}(A)$. This is why $\t{\bar{A}}\bar{A}\neq I$, because the trick does not work outside its row space.



![png](/images/transpose/output_20_0.png){: .center-image}



See? Blue things are not stretched.

## Does this work in higher dimensions?

Absolutely! It's harder to visualize and to understand, but it works in the same way. There is an additional requirement, though: the basis vectors we use must be pairwise orthogonal. Look, $A=CR$, so we are using two matrices $C$ and $R$ to denote bases for the column space and row space respectively. Everything works exactly the same: there will be some $R^\perp$ so that $\b{x}=\t{R}\b{a}+{(\t{R})}^\perp \b{b}$ and $A\b{x}=CR\t{R}\b{a}$. Transposing, $\t{A}A(\t{R}\b{a})=\t{R}(\t{C}C)(R\t{R})\b{a}$, which means that $\t{A}=A^{-1}$ if and only if $\t{C}C=R\t{R}=I$.

Let's take:

$$
R=\frac{1}{\sqrt{10}}\cdot\mq{1}{3}{3}{-1}
$$

$$
C=\frac{1}{\sqrt{5}}\cdot\mq{-2}{1}{1}{2}
$$

Which give us:

$$
A=\frac{1}{\sqrt{50}}\mq{1}{7}{-7}{1}
$$

Even though $A$ is a $2\times 2$ matrix, like before, it has a higher rank (two) compared to the example we used at the beginning (which was rank one). The rank indicates the dimensionality of $\b{R}(A)$ and $\b{C}(A)$: before they were a single vector (dimension one), while now they are planes (dimension two). Since $A$ is now full rank (i.e., its rank corresponds to the number of rows/columns), it does not squash different vectors into the same point.

Orthogonal rows and columns and the normalization constant make $A$ a very peculiar transformation:


![png](/images/transpose/output_23_0.png){: .center-image}



A rotation!

**Orthogonal matrix:** A matrix $Q$ is called orthogonal if $\t{Q}=Q^{-1}$. The matrix $A$ above is orthogonal. Orthogonal matrices are rotations: they do not introduce stretching. If $Q$ rotates in a certain way, $Q^T$ undoes the rotation.

## Conclusion

The transpose equals the inverse only for full rank matrices with orthogonal rows and columns. The idea of the transpose as an inverse, however, still works with matrices that are not full rank **if**

 1. You only consider vectors in the row/column spaces, and
 2. The matrix does not stretch or shrink vectors.

Even in absence of these conditions, it is useful to think of the transpose as a way to go back from where you started, although not exactly in the same location.

This blog post can be downloaded as a Jupyter notebook from [here](/attachments/transpose.ipynb). The notebook also includes the code to generate the pictures above.

## Afterword

Only now I realize that this post is probably filled with trivialities. It traces the journey I made on a paper notebook trying to answer the question that is now the title of the post, because I really could not understand the purpose of transposes. Although I found nothing that I didn't know before starting, doing these computations and drawings by hand clarified and connected several basic concepts that I studied but never understood.
