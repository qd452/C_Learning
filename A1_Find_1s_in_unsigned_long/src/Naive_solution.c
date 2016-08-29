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



int CountOnesFromulong32_t_navie(ulong32_t);
int CountOnesFromulong32_t_navie_2(ulong32_t);

int main()
{
    ulong32_t inputValue;
    uint8_t onesOfValue; // 8-bit is enough
    printf("Please Enter value (between 0 to 4,294,967,295) : ");
    scanf("%u", &inputValue);
    onesOfValue = CountOnesFromulong32_t_navie_2(inputValue); //modify based on requirement

    printf("size of inputValue(32): %d, and size of the ones(8): %d\n", sizeof(inputValue), sizeof(onesOfValue));

    printf("\nThe Number has \"%d\" 1's", onesOfValue);
}

/**
 * @brief My Naive approach trying to handle from the MSB, not quite feasible
 *
 * @note http://stackoverflow.com/questions/9941261/warning-this-decimal-constant-is-unsigned-only-in-iso-c90
 *
 * @param   value     32-bit unsigned long input value
 * @return  count     number of one's
 */
int CountOnesFromulong32_t_navie(ulong32_t value)
{
    uint8_t i, temp, count = 0;
    ulong32_t MASK = 2147483648; //[todo-qd]: 32-bit data with MSB==1 while the rest of the bits are 0
    for (i = 0; i < 32 ; i++)
    {
        MASK = MASK >> i;
        printf("%d\n", MASK);
        temp = (value & MASK) >> MASK;
        printf("%d\n", temp);
        if (temp == 1)
        {
            count++;
        }
    }
    return count;
}

/**
 * @brief the Idea is quite similar to my initial idea, but this solution starts from the LSB
 *
 * @note http://codereview.stackexchange.com/questions/38182/counting-number-of-1s-and-0s-from-integer-with-bitwise-operation
 *
 * @param   value     32-bit unsigned long input value
 * @return  count     number of one's
 */
int CountOnesFromulong32_t_navie_2(ulong32_t value)
{
    uint8_t i, count = 0;
    for (i = 0; i < 32 ; i++)
    {
        if (value % 2 != 0)
        {
            count++;
        }
        value = value >> 1;
    }
    return count;
}