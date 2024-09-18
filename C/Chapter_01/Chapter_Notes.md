# Super Brief Notes

## Chapter 1 ( Tutorial Intro)

### Chapter 1.1
- A C programme consists of functions and variables
--
- Every C programme must have the`main` function.
- Functions communicate data between each other using `arguments`.
- A function specifies parameters and the function caller gives `arguments` corresponding to the specified parameters
- the arguments are specified in what comes after the function name ()
- the parentheses are left empty if no arguments are needed.
- the curly braces after the parentheses contain the `function statements`
--
- the library `included` at the top `stdio` aids input and output operations in C
- "": used to enclose a `character string` or a `string constant`.
- `\n` is the `escape sequence` for a new line.

--

### Chapter 1.2

Sample Programme;

```
#include <stdio.h>
/* print Fahrenheit-Celsius table
for fahr = 0, 20, ..., 300 */
main()
{
    int fahr, celsius;
    int lower, upper, step;
    lower = 0;
    upper = 300;
    step = 20;
    /* lower limit of temperature scale */
    /* upper limit */
    /* step size */
    fahr = lower;
    while (fahr <= upper) {
        celsius = 5 * (fahr-32) / 9;
        printf("%d\t%d\n", fahr, celsius);
        fahr = fahr + step;
    }
}

```

- lines between `/**/` are ignored by the compiler. They are meant to get the human reader to understand what is going on in the code.
- all variables in C must be declared before they are used.
- declaration is defining properties for the variables
- `int fahr celcius` is a declaration of integer variables fahr and celcius
- range for int depends on system, so does that of a float.
- 16 bit ints : -32768 -> +32768
- float: has at least 6 significant digits and magnitude btn 10 pow(-38) and 10 pow(38)
- other data types include: char, short, long, double 

- `lower = 0` in the program above is an example of an assignment statement.
- a while loop can have a body enclosed in  braces or if with one statement, a body thats indented under the while statement.
- In C, integer division truncates. Dividing integers by integers will return an integer only, regardless of the presence of an floating point as a part of the answer.
- prinft out puts while scanf reads input from the user
- in an operation with both integers and floats, the ints are first converted to floats before the operation is executed.

### Chapter 1.3

- The For Statement
```
#include <stdio.h>16
/* print Fahrenheit-Celsius table */
main()
{
    int fahr;
    for (fahr = 0; fahr <= 300; fahr = fahr + 20)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}
```
- the for loop is a generalization of the while loop.
- `fahr = 0` is the initialization: It is run only once.
- `fahr <= 300` is the condition based on whose truth the loop statements run
- if the check evaluates to true, the loop statements are run, the third part is executed (`fahr = fahr + 20` , then the check is evaluated once more and the cycle continues till the checkis false

### Chapter 1.4

- Symbolic names : values that will be used often can be defined as `symbolic constants` at the top of a programme.
- Example: `#define LOWER 0 /*lower limit of table */` defines a symbolic constant lower with the value 0.
- There is no semi colon at the end of the declaration and the names are written in caps.

### Chapter 1.5

- Character input and output.
- C deals with all kinds of text input as streams of characters.
- A text stream: Sequence of line seperated characters, including empty (0 character lines)
- `getchar` and `putchar` are C functions for reading or writing a single `char` for every call, respectively 
- `char c = getchar(); // gets a character from stdin and stores it in c`
- `putchar(c); // outputs the character stored in c`

#### Chapter 1.5.1

- File Copying
Sample Programme
```
//read a character
//while (charater is not end-of-file indicator)
//  output the character just read
//  read a character
//Converting this into C gives:
#include <stdio.h>
/* copy input to output; 1st version */
main()
{
    int c;
    c = getchar();
    while (c != EOF) {
    putchar(c);
    c = getchar();
    }
}
```
- We know there is no more input when getchar() returns an`EOF`. (End Of File)
- `char` can't be used since it is not big enough to hold the size of `EOF`.
- Any expression has a value can can be used as a part of a larger expression.
- ` a = (c = getchar()); // gets a character from stdin, stores it in c, hands the value of c as a copy to a.`

```
#include <stdio.h>
/* copy input to output; 2nd version 
*/
main()
{
    int c;
    while ((c = getchar()) != EOF)
        putchar(c);
}
```
#### Chapter 1.5.2


