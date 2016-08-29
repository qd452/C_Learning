# FIND_1S_IN_UNSIGNED_LONG - Hamming weight

## TABLE OF CONTENTS

[TOC]

## I. UNDERSTANDING OF THE PROBLEM

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

### 2. Naive Approach

I **really** should have started to process my code from LSB instead of MSB...

## II. GOOGLE KEYWORDS

1. find 1's in unsigned long
2. [GeeksforGeeks](http://www.geeksforgeeks.org/count-set-bits-in-an-integer/)
3. [codereview.stackexchange](http://codereview.stackexchange.com/questions/38182/counting-number-of-1s-and-0s-from-integer-with-bitwise-operation)
4. **[How to count the number of set bits in a 32-bit integer?]**(http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer/109025#109025)
4. **Deterministic system**: In mathematics and physics, a deterministic system is a system in which no randomness is involved in the development of future states of the system.[1] A deterministic model will thus always produce the same output from a given starting condition or initial state<sup>[wiki][1]</sup>

## III. LITERATURE REVIEW

### Hamming Weight


[todo-qd]: Some IEEE paper or whatever stuff

## IV. Aiming for Better Solutions

### 1. Difference Between the Two Subtle Approaches

### 2. A Function which is Even More Faster than Above Two

#### Deterministic (CLK)

[todo-qd] how to prove: in python can use `timeit` to do the timing analysis

## V. SUMMARY

[todo-qd]

## VI. FUTURE WORK

[todo-qd]



[1]: https://en.wikipedia.org/wiki/Deterministic_system