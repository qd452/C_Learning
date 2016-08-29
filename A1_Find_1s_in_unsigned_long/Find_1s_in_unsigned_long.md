# Find_1s_in_unsigned_long

## Table of Contents

[TOC]

## I. Understanding of the Problem

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



## II. Google Keywords

1. find 1's in unsigned long
2. http://www.geeksforgeeks.org/count-set-bits-in-an-integer/
3. 

## III. Literature Review

[todo-qd]: Some IEEE paper or whatever stuff

## IV. Aiming to Solve the Problem

### 1. Difference Between the Two Subtle Approach

### 2. Make a function which is more Faster than Above Two

#### Deterministic (CLK)

[todo-qd] how to prove: in python can use `timeit` to do the timing analysis

## V. Summary
[todo-qd]

## VI. Further Work

[todo-qd]