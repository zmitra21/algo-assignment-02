# CMPS 2200 Assignment 02
## Answers

**Name:**Zack Mitra


Place all written answers from `assignment-02.md` here for easier grading.

1. **Asymptotic notation**

    a) $T(n)=2T(n/3)+1$
.  
    .  At every level k, there are 2^k levels
    .  Each problem has a size of n/3^k
    .  If we assume recursion ends when n/3^k = 1   the levels k = log_3(n)
      Using geo-series gives 2^i --> 2^i+1
      Substitute the depth in
      T(n) = 2^log_3(n) = n^log_3(2)
      T(n) is in O(n^log_3(2))
.  
.   
.  
    b) $T(n)=5T(n/4)+n$
.   .  At level k, there are 5^k problems, each of size n/4^k
    .  this gives us n(5/4)^k
    .  With depth size log_4(n) = k
    geo-series inc.
    n(5/4)^log_4(n)
    Which reduces to n^(log_4(5))
      T(n) is in O(n^log_4(5))
.  
.  
.  
    c) $T(n)=7T(n/7)+n$
.   .  At level k, there are 7^k problems, each of size n/7^k
    .  this gives us 7^k (n/7^k) = n
    .  now the summation gives us the depth of the algo
    which is log_7(n) = k multiplied by the work at each level which is n
    Therefore, T(n) is in O(nlog_7(n))
.  
.  
.  
    d) $T(n)=9T(n/3)+n^2$
.    .  At level k, there are 9^k subproblems, each of size n/3^k
    .  assuming recursion ends when n/3^k =1 k = log-3(n)
    .  9^k(n/3^k)^2 = n^2
    Summation gives n^2(log_3(n) + 1)
    From this we know,
    T(n) is in O(n^2log_3(n)) 
.  
.  
.  
    e) $T(n)=8T(n/2)+n^3$
.  .  Same type of sequence as the last question but n^3 instead of n^2 work
    .  Therefore,
    .  T(n) is in O(n^3(log(n)))
.  
.  
.  
    f) $T(n)=49T(n/25)+n^{3/2}\log n$
.  
    .  At level k there are 49^k subproblems, each of size n/25^k
    .  When substituing the work in the whole equation is:
    .  49^k (n/25^k)^3/2 log(n/25^k)
    Which then gives:
    n^3/2(49/125)^klog(n/25^k)
    Since the geometric term is less than 1 we know as k inc. the term dec.
    Therefore:
    T(n) is in O(n^3/2(log(n))
.  
.  
.  
    g) $T(n)=T(n-1)+2$
.    .  Expanding the recurrence we can see the pattern
    .  T(n-1) + 2 --> T(n-2) + 2 --> T(n-3) + 2k
    .  Recursion ending when n-k = 1 so n-1 = k
    Replacing k in the expression gives:
    T(n) = T(1) + 2(n-1)
    Therefore:
    T(n) is in O(n)
.  
.  
.  
    h) $T(n)= T(n-1)+n^c$, with $c\geq 1$
.  Expanding out T(n-1) = T(n-2) + (n-1)^c
.  This then gives T(n) = T(n-2) + (n-1)^c + n^c
. This continues as we solve T(n-2) then T(n-3) till our base case is reached T(1) which is constant
.  Next we sum as i goes to n for i^c which gives n^c for the work per term while there are n terms fully expanding which is n^(c+1)
Therefore, T(n) is in O(n^c+1)
    i) $T(n)=T(\sqrt{n})+1$
.  When expanding at each level we go from n^1/2 then to n^1/4 then n^1/8 which gives n^1/2^k
.  When assuming the recursion stops at n = 2 we can solve (using log rules and algebra) to get us k levels, k = loglog(n). 
.  Since the work per level is constant (1) we get the runtime 
.  From this, T(n) is in O(log(log(n)))
   
2. **Algorithms Comparison**
Algo A says T(n) = 5T(n/2) + n
Algo B says T(n) = 2T(n-1) + 1
Algo C says T(n) = 9T(n/3) + n^2

Solving algo A we follow the same process in assuming recursion goes to 1. n/2^k = 1 giving k = logn
With problems of 5^k of size (n/2^k) we summate that and use log rules giving O(n^2.322)
Algo B is solved differently as we must expand the recursive factor.
With a base case n-k = 1 we get k = n-1
2^k problems per level by expanding out T(n-1) = 2T(n-2) + 1 and putting it back to the original expression which continues k times till our base case
Therefore: T(n) = 2^k(T(n-k)) + 2^k - 1
Our recursion factor collapses to T(1) which is constant and then we have T(n) ~ 2^n-1
Therefore:
T(n) is in O(2^n)
Solving Algo C we can go back to the way of solving it regularly
Our problems per level are 9^k and assuming the size converges to 1 we have n/3^k = 1 as n/3^k is the problem size not including the work
The depth then is log_3(n) = k
Meanwhile our work expression is given by 9^k(n/3^k)^2
We can simplify this to (1)^k(n^2) which the 1 term is constant at 1 for any k
Now our summation is to k on the summation times n^2 which gives us n^2(log_3(n))
Therefore:
T(n) is in O(n^2(log_3(n)))

I would chose algorithm C because it has the slowest growing runtime meaning the time to run the program is the shortest out of the three. 