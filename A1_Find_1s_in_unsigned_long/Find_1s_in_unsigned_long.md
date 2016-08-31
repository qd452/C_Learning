# FIND_1<sub>S</sub>_IN_UNSIGNED_LONG - Hamming weight

## TABLE OF CONTENTS

<!-- MarkdownTOC -->

- [I. UNDERSTANDING OF THE PROBLEM][i-understanding-of-the-problem]
    - [1. Basic Type definition][1-basic-type-definition]
    - [2. Naive Approach][2-naive-approach]
- [II. GOOGLE KEYWORDS][ii-google-keywords]
- [III. LITERATURE REVIEW][iii-literature-review]
    - [Hamming Weight][hamming-weight]
- [IV. Aiming for Better Solutions][iv-aiming-for-better-solutions]
    - [1. Difference Between the Two Subtle Approaches][1-difference-between-the-two-subtle-approaches]
        - [a. Ternary `if else` operator & `for` loop][a-ternary-if-else-operator--for-loop]
        - [b. logical negation operator `!` & `while` loop][b-logical-negation-operator---while-loop]
    - [2. A Function which is Faster than Above Two][2-a-function-which-is-faster-than-above-two]
    - [a. Brian Kernighan’s Algorithm][a-brian-kernighan’s-algorithm]
    - [b. Using Lookup table][b-using-lookup-table]
    - [3. Deterministic \(CLK\)][3-deterministic-clk]
            - [Timing Complexity][timing-complexity]
- [V. SUMMARY][v-summary]
- [VI. FUTURE WORK][vi-future-work]

<!-- /MarkdownTOC -->


<a name="i-understanding-of-the-problem"></a>
## I. UNDERSTANDING OF THE PROBLEM

<a name="1-basic-type-definition"></a>
### 1. Basic Type definition

``` 
unsigned long var; // 32-bit, 4-bytes
```

- [Range of values in C Int and Long 32 - 64 bits](Range of values in C Int and Long 32 - 64 bits)
> *No, int in C is not defined to be 32 bits. int and long are not defined to be any specific size at all. The only thing the language guarantees is that sizeof(char)<=sizeof(short)<=sizeof(long).*
>*Theoretically a compiler could make short, char, and long all the same number of bits. I know of some that actually did that for all those types save char.*
>*This is why C now defines types like uint16_t and uint32_t. If you need a specific size, you are supposed to use one of those.*

- [64-bit Data models](https://en.wikipedia.org/wiki/64-bit_computing#64-bit_data_models)

- According to [C++ standard](http://en.cppreference.com/w/cpp/language/types), `unsigned long` must be at least 32-bit.

<a name="2-naive-approach"></a>
### 2. Naive Approach

I **really** should have started to process my code from LSB instead of MSB...

<a name="ii-google-keywords"></a>
## II. GOOGLE KEYWORDS

1. find 1's in unsigned long
2. [GeeksforGeeks](http://www.geeksforgeeks.org/count-set-bits-in-an-integer/)
3. [codereview.stackexchange](http://codereview.stackexchange.com/questions/38182/counting-number-of-1s-and-0s-from-integer-with-bitwise-operation)
4. [**How to count the number of set bits in a 32-bit integer?**](http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer/109025#109025)
5. [C++ Operators](http://www.cplusplus.com/doc/tutorial/operators/)
6. [How does logical negation work in C?](http://stackoverflow.com/questions/2319766/how-does-logical-negation-work-in-c)
7. **Deterministic system**: In mathematics and physics, a deterministic system is a system in which no randomness is involved in the development of future states of the system.[1] A deterministic model will thus always produce the same output from a given starting condition or initial state<sup>[wiki][1]</sup>
8. [Big-Theta notation](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-big-theta-notation)
9. [What is the difference between Θ(n) and O(n)?](http://stackoverflow.com/questions/471199/what-is-the-difference-between-%CE%98n-and-on)
10. [More on Big O and Big Omega and Big Theta](http://stackoverflow.com/questions/14095510/could-anyone-explain-big-o-versus-big-omega-vs-big-theta)


<a name="iii-literature-review"></a>
## III. LITERATURE REVIEW

<a name="hamming-weight"></a>
### Hamming Weight


[todo-qd]: Some IEEE paper or whatever stuff

<a name="iv-aiming-for-better-solutions"></a>
## IV. Aiming for Better Solutions

<a name="1-difference-between-the-two-subtle-approaches"></a>
### 1. Difference Between the Two Subtle Approaches

<a name="a-ternary-if-else-operator--for-loop"></a>
#### a. Ternary `if else` operator & `for` loop

```
for (i = 0; i < 32; i++) {
        cnt += (var & 0x01) ? 1 : 0;
        var >>= 1;
    }
```

In this approach, the iteration logic is using `for` loop to iterate through the entire bits (32-bit) of the input variable, which could be inefficient in the case of the input variable is smaller than 0x80000000 (the rightmost set bit is not the MSB).

And `?:` is a ternary operator that is part of the syntax for a basic conditional expression in C/C++. The `conditions` is evaluated true or fals as a Boolean expression *(no built-in type of `bool` in C)* 

*`variable = condition ? value_if_true : value_if_false`*

> **Note**: In C++ there are conditional assignment situations where use of the if-else statement is impossible, since this language explicitly distinguishes between initialization and assignment. In such case it is always possible to use a function call, but this can be cumbersome and inelegant. For example, to pass conditionally different values as an argument for a constructor of a field or a base class, it is impossible to use a plain if-else statement; in this case we can use a conditional assignment expression, or a function call. Bear in mind also that some types allow initialization, but do not allow assignment, or even that the assignment operator and the constructor do totally different things. <sup>[wiki][2]</sup>

<a name="b-logical-negation-operator---while-loop"></a>
#### b. logical negation operator `!` & `while` loop

```
    while (var) {
        cnt += !!(var & 0x01);
        var >>= 1;
    }
```

In terms of the algorithm efficiency, `while` is an improvement in this case compared to loop through all the bits; the looping basically stops when it hits the the rightmost set bit of `var`. 

And the logical negation operator (!) reverses the meaning of its operand. **To be noted** that in C++, the operand is implicitly converted to type **bool**. The result is **true** if the converted operand is **false**; the result is **false** if the converted operand is true. The result is of type **bool**.<sup>[MSDN][2]</sup>

So in this case, in C, `!e` can be replaced by `((e)?:0:1)`. Therefore, `!!e` can be replaced by `((e)?1:0)`, which is actually equivalent with the first approach of using ternary `if else` operator.

<a name="2-a-function-which-is-faster-than-above-two"></a>
### 2. A Function which is Faster than Above Two

<a name="a-brian-kernighan’s-algorithm"></a>
### a. Brian Kernighan’s Algorithm

```
while (var) {
        var &= (var - 1);
        cnt++;
    }
```

The Subtle part regarding this algorithm is that it can actually loop through the from rightmost to the leftmost while skipping through non-set bits. So in the case of `var = 9;`, it only requires 2 loops while for the subtle approach 2, it still need 4 loops (from leftmost to the rightmost). 

<a name="b-using-lookup-table"></a>
### b. Using Lookup table

We can count bits in **O(1)** time using lookup table. Please see http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetTable for details.

<a name="3-deterministic-clk"></a>
### 3. Deterministic (CLK)

<a name="timing-complexity"></a>
##### Timing Complexity

- **Subtle Approach 1 (Ternary and for loop)**: Linear -> O(N)

- **Subtle Approach 2 (logical negation and while)**: Logarithmic -> Theta(log(N)) (Theta of log(N))

- **Brian Kernighan’s Algorithm**: Logarithmic -> O(log(N))

- **Lookup table**: Constant -> O(1)


<a name="v-summary"></a>
## V. SUMMARY

1. Through these two subtle code, my knowledge on C/C++ get brushed up and realized the importance of understanding the fundamental knowledge of the language.
2. Hamming weight problem 
3. O(n) represents upper bound. Θ(n) means tight bound. Ω(n) represents lower bound.

<a name="vi-future-work"></a>
## VI. FUTURE WORK

1. To [check the type in C](http://stackoverflow.com/questions/6280055/how-do-i-check-if-a-variable-is-of-a-certain-type-compare-two-types-in-c). Generally unlike in `Python`, I could directly use `type()` to check the type, I could *however check the size of a variable using the `sizeof()` function. This may help me determine the type of data.* This may help me get a deeper understanding of the all the operators *(`+=`, `!!`, `?:` etc)* and their difference in C and C++.
2. [Memory usage](http://algs4.cs.princeton.edu/14analysis/)
3. Timing Analysis from the code level. How to prove: in python can use `timeit` to do the timing analysis. Need to include all the test cases.



[1]: https://en.wikipedia.org/wiki/Deterministic_system
[2]: https://en.wikipedia.org/wiki/%3F:#C.2B.2B
[3]: https://msdn.microsoft.com/en-us/library/1k6w8551.aspx