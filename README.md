# Scripts for Cryptologic Protocol Theory class
Project consists of scripts for Cryptologic Protocol Theory class. It's meant to support student's workflow through out the class.

# Cheatsheet
[`elem.py <modulo>`](#elem) - elements of a group  
[`gcd.py <a_number> <b_number>`](#gcd) - Greatest common dividor (GCD)  
[`eucgcd.py <a_number> <b_number>`](#eucgcd) - Euclidean Algorithm (GCD)  
[`ferm.py <number_to_test>`](#ferm) or [`ferm.py <number_to_test> <n_times>`](#ferm) - Fermant's test  
[`gen.py <element> <modulo>`](#gen) - tests if element is a generator  
[`phi.py <number>`](#phi) or [`phi.py <prime_factor> <prime_factor> ... `](#phi) - Euler's function  
[`inv.py <element> <modulo>`](#inv) - inverse element  
[`order.py <modulo>`](#order) - order of a group  
[`order.py <element> <modulo>`](#order) - order of an element

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
* `gen.py <element> <modulo>` - test if `<element>` is a generator in `Z*<modulo>`

example: `gen.py 3 10`

## <a name="phi"></a>Euler's function
* `phi.py <number>` - calculates Euler's function for `<number>`
* `phi.py <prime_factor> <prime_factor> ... ` - calculates Euler's function by prime factors of a number

example: `phi.py 60` or `phi.py 2 2 3 5`  
Second usage is filled with prime factorization `60 = 2^2 * 3 * 5`

## <a name="inv"></a>Inverse element
* `inv.py <element> <modulo>` - finds inverse to `<element>` in `Z*<modulo>` if exists

example: `inv.py 5 12` gives and inverse of 5 in modulo 12 (only multiplicative group)

## <a name="order"></a>Order
* `order.py <modulo>`  - prints out order of a group
* `order.py <element> <modulo>` - prints out order of an element in a group

example: `order.py 69` or `order.py 3 69`

## Complexity
* `complex.py` will show some basic info about computing complexity of an algorithm

# Requirements
In order to run above commands as shown you need to have installed [python](https://www.python.org/downloads/) interpret and either be in current directory with scripts or have path to them set in system variable `$PATH` (on Windows)

# Tip
For faster workflow type only first few letters and press `TAB` key for auto-compltion. This way you never have to type ".py" at least.

