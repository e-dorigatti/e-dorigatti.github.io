---
layout: post
title:  "A gentle introduction to natural language and genomics"
date:   2019-09-02 12:00:00 +0200
categories: jekyll update
---


During the research I am conducting for my next project I stumbled upon the
intriguing idea of applying tools developed for Natural Language Processing
(NLP) to bioinformatics. After all, the comparison seems to hold up: you can
think of the DNA as a collection of books (genes), each of which contains
several chapters (proteins) related to a certain topic.

The project I just mentioned will deal with protein classification (or
regression), which is analogous to sentence classification in NLP. That field
was turned upside down in the last years due to the introduction of Deep
Learning, and, in particular, of distributed word representations; going from
words/sentences/documents to amino acids/proteins/genes is not such a big leap,
conceptually. 

Since I want this blog to be useful to non-technical people as well, I will
devote this article to a brief, high-level and to-the-point overview of what is
going on, written in plain English (a bit like [this](https://xkcd.com/1133/)).
Of course, it will be far from exhaustive, because (a) otherwise it would
require a book or two and (b) the Internet is already full of beginner-level
introductory material. I just want non-technical readers to leave this page
feeling like they have the main intuition and understanding of what is going on.
(addendum: I initially planned this to be a just a few paragraphs before the
technical material, but it turned out much longer than I had expected, so it is
now its own blog post).

## Natural language and Genomics
I first start by trying to convince you that Natural Language Processing and
Genomics (the study of DNA) are similar in several ways, and this allows us to
use the same tools, which I will describe in the next section.

So what are these two disciplines about? NLP is about teaching computers how to
read, however this is not approached holistically, rather there are several
tasks that are studied independently. Examples of these tasks are sentiment
analysis (deciding whether a text conveys positive or negative emotions, useful
for automated analysis of Amazon reviews or to predict the stock market based on
tweets), summarization (extracting a few key sentences out of a long text,
useful), question answering (where the answer is to be found in a given text),
translation, sarcasm detection, and many more. The focus of Genomics is,
instead, the study of genes; the main tasks are finding the function of proteins
and their structure once folded, how they interact with each other, how genes
affect the way we look, and so on. Very briefly, a gene is a strand of DNA, a
sequence of amino acids that encode a protein. Proteins are produced by copying
the corresponding gene, and, once produced, they fold in a 3D structure; this
structure is what allows the proteins to fulfill its purpose.

Even though NLP and Genomics are concerned with very different tasks, the way
these tasks are approached can be similar, because we realized that DNA behaves
similarly to a language and has a similar structure. For example, in both cases
there are long range dependencies. Subject and object can be at the opposite
ends of a sentence, but they must be linked to understand the meaning of that
sentence. Similarly, some amino acids, the words of DNA, can be far apart in the
DNA sequence, but once protein encoded by that sequence is produced and folded,
those amino acids end up sticking to each other to keep the protein structure
together. Understanding these long range dependencies and the 3D structure of
proteins helps us understand what their functions are and how they relate to
each other. Synonyms are another common feature between natural language and
DNA; some amino acids can be replaced with others without altering the folding
(and the function) of the resulting protein, while others are fundamental and
cannot be changed without changing the protein. Moreover, there are certain
sequences of amino acids that are found in many different genes, and that fold in
the same way, while other combinations of amino acids are instead very rare.
Actually, amino acids are actually composed by three bases (C,T,A,G) each; this
means that there is some redundancy, since several triplets all map to the same
amino acid. There are also combinations to indicate the beginning and ending of a
protein.

There is much more that we know, and even more that we do not yet know, about
genes and proteins. With these simple examples, I hope to have convinced you
that the DNA and, say, the English language, work similarly. To recap: the
letters of DNA are the four bases, and every word is a group of three bases. A
protein is like a sentence, and a gene is a document. Genes are grouped in
chromosomes, which are like books, and all the chromosomes in an organism are
like an encyclopedia that documents its functioning up to the tiniest detail.

## A brief history of word vectors in NLP
We now look at how computers understand natural language, confident that the
same methods work for genes, too. The only thing computers know are numbers;
audio, images, text, for a computer everything is just a bunch of numbers.
Therefore, if we want to make a computer intelligent, we have to find ways of
representing things with numbers. Once we have done that, we can use
mathematical formulas to describe the process of learning: this means that a
computer's knowledge is encoded in numbers, and said computer thinks by
transforming these numbers with math.

This blog post talks about different ways of transforming the words of English,
German, and any other _natural_ language, into numbers, so that computers can
try to understand text. In particular, I will describe several works that
applied these methods to amino acids and proteins instead of words and documents.
As it turns out, they work in very similar ways. For example, they both have
_syntactic_ rules that say which sequences of tokens (words or amino acids) are
valid sentences/proteins, and they both require understanding dependencies
between distant tokens, e.g. what is the subject and what is the object versus
which amino acids will stick together when the protein folds itself. And the
similarities do not stop here. So it is not surprising that linguistics tools
have been applied to genomics (the study of DNA) ever since they were developed
back in the eighties.

I am going to conclude this section with a brief history of the different
methods to transform words into numbers. In fact, we associate every word with a
list of numbers, which we call _vector_, and we want every word to have the same
number of numbers, because this is much simpler to deal with in math. Initially,
the size of the vector was the same as the size of the vocabulary, and every
position in this vector corresponds to a word; the vector associated to a
certain word is then full of zeroes except in the position of that word, in
which we put a one. For example, if we use alphabetical order, the first word is
_a_, so the vector for _a_ is 1 followed by a lot of zeroes. The second word is
_able_, so the vector for able is 0, then 1, then a lot of zeroes. And so on.
Since there are too many words, we only consider the first few tens of thousands
of most frequent words (what a native person knows).

This method, called one-hot or sparse encoding, has two main drawbacks: first,
the resulting vectors are very very big, and second all words have the same
distance: either two differences or none (if they are the same word). This is
very bad, because in mathematics distances can be used in a lot of interesting
ways; intuitively, we want the vector for _huge_ to be closer (more similar) to
_massive_'s vector than to _tiny_'s.

A more advanced way of assigning vectors to words is TF-IDF, which means "term
frequency-inverse document frequency", and reflects the two factors that
influence the vectors. In this case, we need a collection of documents, such as
pages of Wikipedia to start with; TF-IDF then tries to find out which words are
"important" in a given page. The idea is very simple: a word is important for a
given page if it appears frequently in it, and not very frequently everywhere
else. For example, the word _the_ appears very frequently everywhere, so it is
not very important (it does not convey any meaning); the word _Stockholm_
appears almost 400 times in its Wikipedia page, and not very frequently in most
of the other six million articles written in English, so we can reasonably
conclude that the page titled _Stockholm_ talks about _Stockholm_ (duh). If you
now do this for every other article, you have a list of TF-IDF scores of the
word _Stockholm_, and that is its vector. Now two words are similar if they are
important in the same pages and not very important in different pages. This is
the heart of the _distributional hypothesis_, an assumption that underlies much
of NLP: words that appear in the same context tend to have have the same
meaning.

And finally now we leap to the the first technique, called continuous bag of
words (CBOW), that sparked the current state of the art, the so-called
_distributed representations_. These vectors live in what we call a _vector
space_, which means that they can be added or subtracted (element by element),
stretched or contracted, and still result in a vector for a word. The most
famous example of this is that _v(king)-v(man)+v(woman)=v(queen)_, with
_v(word)_ being the vector for a certain word. This kind of analogies holds up
for a lot of other categories, as well: _v(Paris)-v(France)+v(Tokyo)=v(Japan)_,
_v(Einstein)-v(scientist)+v(Picasso)=v(artist)_,
_v(go)-v(went)=v(capture)-v(captured)_ and so on (keep in mind it is not _exact_
equality, and sometimes you get another vector that is closer than what you'd
expect). If you consider each number in a vector as the distance to move in a
certain direction, you find that every vector corresponds to a point in space
(suppose you always start at the same spot). What these analogies mean, is that
in order to go from _v(king)_ to _v(queen)_ you have to move in the same
direction and for the same distance that you need to reach _v(woman)_ starting
from _v(man)_; essentially, there is a direction associated with gender, a
direction associated with capital-state, one for scientist-artist, one for
present-past, and so on.

The vector for a word is constructed by asking the computer to compute it by
combining the vectors of surrounding words using only those operations; the
computer initially starts with random vectors and changes them so that this task
can be accomplished. If you have ever learned a foreign language at school, I am
sure you remember those fill-the-blank exercises: "Mary bought _____ at the
supermarket". After seeing millions of sentences and billions of words, the
computer is able to finally understand their meaning.

By using word vectors and combining them in disparate ways, computers can then
learn to translate between languages, answer to our questions, search things we
ask for, and much more. This is, pretty much, how we teach computers to read in
2019.
