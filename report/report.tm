<TeXmacs|1.0.7.14>

<style|generic>

<\body>
  <doc-data|<doc-title|Kernel Methods>|<doc-author-data|<author-name|François-Xavier
  Thomas>>|<\doc-subtitle>
    Homework 3
  </doc-subtitle>||>

  <section|Exercise 1>

  The 2-SVM problem is written as follows :

  <\equation*>
    min<rsub|f\<in\>H<rsub|K>,b\<in\>\<bbb-R\>><around*|{|<frac|1|n>*<big|sum><rsub|i=1><rsup|n>
    L<around*|(|f<around*|(|x<rsub|i>|)>+b,y<rsub|i>|)>+\<lambda\>*<around*|\<\|\|\>|f|\<\|\|\>><rsup|2>|}>
  </equation*>

  With :

  <\equation*>
    L<around*|(|u,y|)>=max<around*|(|1-u*y,0|)><rsup|2>
  </equation*>

  ...which can be re-written using slack variables :

  <\eqnarray*>
    <tformat|<table|<row|<cell|>|<cell|>|<cell|<choice|<tformat|<table|<row|<cell|min<rsub|f\<in\>H<rsub|K>;b\<in\>\<bbb-R\>;\<xi\>\<in\>\<bbb-R\><rsup|n>>
    <around*|{|<frac|1|n>*<big|sum><rsub|i=1><rsup|n>
    \<xi\><rsub|i>+\<lambda\>*<around*|\<\|\|\>|<rsup|>f|\<\|\|\>><rsup|2>|}>>>|<row|<cell|\<xi\><rsub|i>\<geqslant\>L<around*|(|f<around*|(|x<rsub|i>|)>+b,y<rsub|i>|)>>>>>>>>|<row|<cell|>|<cell|\<Leftrightarrow\>>|<cell|<choice|<tformat|<table|<row|<cell|min<rsub|f\<in\>H<rsub|K>;b\<in\>\<bbb-R\>;\<xi\>\<in\>\<bbb-R\><rsup|n>>
    <around*|{|<frac|1|n>*<big|sum><rsub|i=1><rsup|n>
    \<xi\><rsub|i>+\<lambda\>*<around*|\<\|\|\>|<rsup|>f|\<\|\|\>><rsup|2>|}>>>|<row|<cell|\<xi\><rsub|i>\<geqslant\><around*|(|1-y<rsub|i>*<around*|(|f<around*|(|x<rsub|i>|)>+b|)>|)><rsup|2>>>|<row|<cell|\<xi\><rsub|i>\<geqslant\>0>>>>><eq-number>>>>>
  </eqnarray*>

  Then, in the RKHS <math|H<rsub|k>>, from the representer theorem, we can
  write <math|<wide|f|^>> as :

  <\equation*>
    <wide|f|^>=<big|sum><rsub|i=1><rsup|n>\<alpha\><rsub|i>*K<rsub|x<rsub|i>>
  </equation*>

  ...which can replace <math|f> in (1) :

  <\eqnarray*>
    <tformat|<table|<row|<cell|<around*|(|1|)>>|<cell|\<Leftrightarrow\>>|<cell|<choice|<tformat|<table|<row|<cell|min<rsub|\<alpha\>\<in\>\<bbb-R\><rsup|n>;b\<in\>\<bbb-R\>;\<xi\>\<in\>\<bbb-R\><rsup|n>>
    <around*|{|<frac|1|n>*<big|sum><rsub|i=1><rsup|n>
    \<xi\><rsub|i>+\<lambda\>\<alpha\><rsup|T>K
    a|}>>>|<row|<cell|\<xi\><rsub|i>-<around*|(|y<rsub|i>*<around*|(|<big|sum><rsub|j=1><rsup|n>a<rsub|j>*K<around*|(|x<rsub|i>,x<rsub|j>|)>+b|)>-1|)><rsup|2>\<geqslant\>0>>|<row|<cell|\<xi\><rsub|i>\<geqslant\>0>>>>>>>>>
  </eqnarray*>

  Introducing the Lagrange multipliers <math|\<mu\>> and <math|\<nu\>>, we
  get :

  <\eqnarray*>
    <tformat|<table|<row|<cell|L<around*|(|\<alpha\>,b,\<xi\>,\<mu\>,\<nu\>|)>>|<cell|=>|<cell|<frac|1|n>*<big|sum><rsub|i=1><rsup|n>
    \<xi\><rsub|i>+\<lambda\>\<alpha\><rsup|T>K
    \<alpha\>-<big|sum><rsub|i=1><rsup|n>\<mu\><rsub|i>*<around*|(|\<xi\><rsub|i>-<around*|(|y<rsub|i>*<around*|(|<big|sum><rsub|j=1><rsup|n>a<rsub|j>*K<around*|(|x<rsub|i>,x<rsub|j>|)>+b|)>-1|)><rsup|2>|)>-<big|sum><rsub|i=1><rsup|n>\<nu\><rsub|i>*\<xi\><rsub|i>>>|<row|<cell|>|<cell|=>|<cell|<frac|1|n>*<big|sum><rsub|i=1><rsup|n>
    \<xi\><rsub|i>+\<lambda\>\<alpha\><rsup|T>K
    \<alpha\>-<big|sum><rsub|i=1><rsup|n>\<mu\><rsub|i>*<around*|[|\<xi\><rsub|i>-y<rsub|i><rsup|2><around*|(|<big|sum><rsub|j=1><rsup|n>a<rsub|j>*K<around*|(|x<rsub|i>,x<rsub|j>|)>+b|)><rsup|2>+2*y<rsub|i>*<around*|(|<big|sum><rsub|j=1><rsup|n>a<rsub|j>*K<around*|(|x<rsub|i>,x<rsub|j>|)>+b|)>-1|]>-<big|sum><rsub|i=1><rsup|n>\<nu\><rsub|i>*\<xi\><rsub|i>>>|<row|<cell|>|<cell|=>|<cell|<frac|1|n>*<big|sum><rsub|i=1><rsup|n>
    \<xi\><rsub|i>+\<lambda\>\<alpha\><rsup|T>K
    \<alpha\>-<big|sum><rsub|i=1><rsup|n>\<mu\><rsub|i>*<around*|[|\<xi\><rsub|i>-y<rsub|i><rsup|2><around*|(|<big|sum><rsub|j,k=1><rsup|n>a<rsub|j>*a<rsub|k>*K<around*|(|x<rsub|i>,x<rsub|j>|)>*K<around*|(|x<rsub|i>,x<rsub|k>|)>+2*b*<big|sum><rsub|j=1><rsup|n>a<rsub|j>*K<around*|(|x<rsub|i>,x<rsub|j>|)>+b<rsup|2>|)>+2*y<rsub|i>*<around*|(|<big|sum><rsub|j=1><rsup|n>a<rsub|j>*K<around*|(|x<rsub|i>,x<rsub|j>|)>+b|)>-1|]>-<big|sum><rsub|i=1><rsup|n>\<nu\><rsub|i>*\<xi\><rsub|i>>>>>
  </eqnarray*>

  This function is convex and is minimized when its gradient is null :

  <\equation*>
    \<nabla\><rsub|\<alpha\>>L=2*\<lambda\>*K
    \<alpha\>-K<around*|(|2-b*Y|)>*Y*\<mu\>+\ 
  </equation*>

  ...where <math|Y=Diag<around*|(|y<rsub|i>|)><rsub|i>>.

  <section|Exercise 2>

  For the implementation, I used the <verbatim|sklearn> Python library with
  <verbatim|matplotlib> for visualization.

  I first experimented with the RBF kernel, which was the default, with
  different values of <math|C> and <math|\<gamma\>> (the <math|\<gamma\>>
  value came from <verbatim|sklearn>'s implementation, see :
  <hlink|<verbatim|http://scikit-learn.org/stable/modules/svm.html>|>) :

  <\equation*>
    k<rsub|RBF><around*|(|x,y|)>=exp <around*|(|-\<gamma\>*<around*|\<langle\>|x\|y|\<rangle\>>|)>
  </equation*>

  <center|<image|RBF_Kernel.png|23%|||>>

  Then, I tried in order other kernels, to see if their results were better
  than RBF, in order : polynomial then sigmoid. Most of the time, they all
  performed worse than RBF :

  <\eqnarray*>
    <tformat|<table|<row|<cell|k<rsub|POLY><around*|(|x,y|)>>|<cell|=>|<cell|<around*|[|\<gamma\>*<around*|\<langle\>|x\|y|\<rangle\>>|]><rsup|d>>>|<row|<cell|k<rsub|SIGMOID><around*|(|x,y|)>>|<cell|=>|<cell|tanh
    <around*|(|\<gamma\>*<around*|\<langle\>|x\|y|\<rangle\>>|)>>>>>
  </eqnarray*>

  <\center>
    <image|Polynomial_Kernel.png|23%|||>

    <image|Sigmoid_Kernel.png|23%|||>
  </center>

  Then, to have different points of view, I compared these results with one
  another :

  <center|<image|All_Kernels.png|23%|||>>

  We can see that the RBF kernel really performs better than the others on
  most cases, with the Polynomial, Sigmoid and Linear Kernels not far away,
  in terms of performance.

  <subsection|Multi-class strategies>

  All these classifications were executed with the ``one-vs-one'' multiclass
  scheme. Simply put :

  <\itemize>
    <item>Generate one classifier for each class pair (we have to generate
    <math|K\<times\><dfrac|K-1|2>> classifiers, with <math|K> being the
    number of classes).

    <item>Each classifier will vote for his predicted class. Let's say that
    classifier <math|C> chooses class <math|a> between <math|a,b> : it will
    then vote for <math|a>.

    <item>The predicted class is the class with the maximum number of votes.
  </itemize>

  There are other multi-class classification strategies available, such as
  the ``one-vs-all'' strategy, or others based on error-correcting codes, but
  I didn't have time to test them thoroughly.
</body>

<\initial>
  <\collection>
    <associate|sfactor|4>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|auto-1|<tuple|1|?>>
    <associate|auto-2|<tuple|2|?>>
    <associate|auto-3|<tuple|2.1|?>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Exercise
      1> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Exercise
      2> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>