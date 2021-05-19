# Scripts for Cryptologic Protocol Theory class
Project consists of scripts for Cryptologic Protocol Theory class. It's meant to support student's workflow through out the class.

# Cheatsheet
[`elem.py <modulo>`](#elem) - elements of a group  
[`gcd.py <a_number> <b_number>`](#gcd) - Greatest common dividor (GCD)  
[`eucgcd.py <a_number> <b_number>`](#eucgcd) - Euclidean Algorithm (GCD)  
[`ferm.py <number_to_test>`](#ferm) or [`ferm.py <number_to_test> <n_times>`](#ferm) - Fermant's test  
[`gen.py <element> <modulo>`](#gen) - tests if element is a generator  
[`findgen.py <modulo>`](#findgen) - finds all generators of group  
[`phi.py <number>`](#phi) or [`phi.py <prime_factor> <prime_factor> ... `](#phi) - Euler's function  
[`inv.py <element> <modulo>`](#inv) - inverse element  
[`order.py <modulo>`](#order) - order of a group  
[`order.py <element> <modulo>`](#order) - order of an element  
[`pow.py <base> <power>`](#pow) or [`pow.py <base> <power> <modulo>`](#pow) - power  
[`mod.py <number> <modulo>`](#mod) - modulo

# Scripts and their usage
## <a name="elem"></a>Elements of a group
* `elem.py <modulo>` - prints out elements of additive and multiplicative group `Z<modulo>`

example: `elem.py 12`

## <a name="gcd"></a>Greatest common divisor (GCD)
* `gcd.py <a_number> <b_number>` - finds GCD

example: `gcd.py 9 7`

## <a name="eucgcd"></a>Euclidean algorithm (GCD)
* `eucgcd.py <a_number> <b_number>` - finds GCD with Euclidean algorithm

example: `eucgcd.py <33> <12>`

## <a name="ferm"></a>Fermant's test
* `ferm.py <number_to_test>` - tests if a `number` is a prime number through Fermant's test
* `ferm.py <number_to_test> <n_times> - runs Fermant's test `<n_times>`

example: `ferm.py 69` will run test only once or `ferm.py 69 3` will run test 3 times

## <a name="gen"></a>Generator
The generator is and element such that if you do element^1 than element^2 and so on, it will generate all elements in the group.
The group Z*q has phi(phi(q)) generators, ONLY if q is a prime!!! The only possible orders of an element are divisors of the Order of the group.
Only these possible orders are necessary to test if testing an element to be a generator. If at the possible order is the element congruent to 1 than this element is not a generator.
However, if the element is congruent to 1 at the order of phi(q) than the element is a generator.
* `gen.py <element> <modulo>` - test if `<element>` is a generator in `Z*<modulo>`
* `gen.py <-t | --theory>` - prints out some basic theory

example: `gen.py 3 10`

## <a name="findgen"></a>Find all generators
* `findgen.py <modulo>` - test all elements if they are a generator in `Z*<modulo>`

example: `findgen.py 11`

## <a name="phi"></a>Euler's function
* `phi.py <number>` - calculates Euler's function for `<number>`
* `phi.py <prime_factor> <prime_factor> ... ` - calculates Euler's function by prime factors of a number

example: `phi.py 60` or `phi.py 2 2 3 5`  
Second usage is filled with prime factorization `60 = 2^2 * 3 * 5`

## <a name="inv"></a>Inverse element
Inverse is a number `a(^-1)` such that: `a * a^(-1) = 1 (mod n)`.  
Inverse exist ONLY if a and n are comprime, means GCD(a,n) = 1 !!!
* `inv.py <element> <modulo>` - finds inverse to `<element>` in `Z*<modulo>` if exists
* `inv.py <-t | --theory>` - shows theory

example: `inv.py 5 12` - gives and inverse of 5 in modulo 12 (only multiplicative group)  
`inv.py --theory` - prints theory

## <a name="order"></a>Order
Order of a group says how many elements group has. Order of an element says how many elements of a group can this element generate.
The only possible orders of an element are divisors of Order of a group. Only these possible orders are necessary to test if testing an element to be a generator.
* `order.py <modulo>`  - prints out order of a group
* `order.py <element> <modulo>` - prints out order of an element in a group
* `order.py <-t | --theory>` - prints out basic theory

example: `order.py 69` or `order.py 3 69` or `order.py -t`

## <a name="pow"></a>Power
* `pow.py <base> <power>`
* `pow.py <base> <power> <modulo>`

example: `pow.py 69 2` - computes `69^2`  
 `pow.py 69 2 16` - computes `69^2 mod 16`

## <a name="mod"></a>Modulo
* `mod.py <number> <mod>`

example: `mod.py 69 60`


## Functions
Injective (one-to-one) function is such that no two x map to same y  
Surjective (onto) function is such that every y has AT LEAST one x  
Bijective (combination of both) function is such that every y has EXACTLY one x

* `func.py` - shows some basic theory about functions

## Complexity
* `complex.py` - will show some basic info about computing complexity of an algorithm

# Requirements
In order to run above commands as shown you need to have installed [python](https://www.python.org/downloads/) interpret and either be in current directory with scripts or have path to them set in system variable `$PATH` (on Windows)

# Tip
For faster workflow type only first few letters and press `TAB` key for auto-compltion. This way you never have to type ".py" at least.  
You don't have to type `python` or `python3` unless you want to use that specific version.

Feel free to contribute by forking and then requesting a pull <3 <3 <3

