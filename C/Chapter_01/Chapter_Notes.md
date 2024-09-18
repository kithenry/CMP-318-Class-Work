# Super Brief Notes

## Chapter 1.1
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

## Chapter 1.2

### Sample Programme;
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



