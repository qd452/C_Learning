// Hamming Weight Problem
// Definition: Count number of 1's from 32-bit unsigned long with bitwise operation
//
// 2^32 = 4,294,967,296  4294967295
// unsigned long 32 bit (4-bytes)

#include <stdint.h>
#include <stddef.h>
#include <stdio.h>

#ifndef NULL
#error "Error NULL definition should be done. Please add required include "
#endif

typedef unsigned long ulong32_t;



int CountOnesFromulong32_t_1(ulong32_t);
int CountOnesFromulong32_t_2(ulong32_t);
int CountOnesFromulong32_t_bk(ulong32_t); // Brian Kernighan’s Algorithm


int main()
{
    ulong32_t inputValue;
    uint8_t onesOfValue; // 8-bit is enough
    printf("Please Enter value (between 0 to 4,294,967,295) : ");
    scanf("%u", &inputValue);
    onesOfValue = CountOnesFromulong32_t_bk(inputValue); //modify based on requirement

    printf("size of inputValue(32): %d, and size of the ones(8): %d\n", sizeof(inputValue), sizeof(onesOfValue));

    printf("\nThe Number has \"%d\" 1's", onesOfValue);
}

/**
 * @brief starting from the LSB and kind of one-liner using (?:) bitwise operation
 *
 * @note Here it loops through all the 32-bit no matter how, timing complexity is linear, O(var)
 *
 * @param   value     32-bit unsigned long input value
 * @return  count     number of one's
 */
int CountOnesFromulong32_t_1(ulong32_t var)
{
    uint8_t i, cnt = 0;

    for (i = 0; i < 32; i++) {
        cnt += (var & 0x01) ? 1 : 0;
        var >>= 1;
    }

    return cnt;
}

/**
 * @brief starting from the LSB and using negation operator (!) just reverses the meaning of tis operand.
 *
 * @note Here due to the while() loop, it actually stops when hit MSB and doesn't have to loop through all,
         timing complexity is Theta(log(var)) (Theta of log(var))
 *
 * @param   value     32-bit unsigned long input value
 * @return  count     number of one's
 */
int CountOnesFromulong32_t_2(ulong32_t var)
{
    uint8_t cnt = 0;
    uint8_t temp;
    while (var) {
        cnt += !!(var & 0x01);
        var >>= 1;
    }

    return cnt;
}

/**
 * @brief Brian Kernighan’s Algorithm
 *
 * @note Timing Complexity: O(log(var))
 *
 * @param   value     32-bit unsigned long input value
 * @return  count     number of one's
 */
int CountOnesFromulong32_t_bk(ulong32_t var)
{
    uint8_t cnt = 0;
    while (var) {
        var &= (var - 1);
        cnt++;
    }

    return cnt;
}