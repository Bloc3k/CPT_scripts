# Scripts for Cryptologic Protocol Theory class
Project consists of scripts for Cryptologic Protocol Theory class. It's meant to support student's workflow through out the class.

# Scripts and their usage
## Elements of a group
* `elem.py <number_group>`

example: `elem.py 12` prints out elements of additive and multiplicative group Z12

## Greatest common divisor
* `gcd.py <a_number> <b_number>`

example: `gcd.py 9 7`

## Fermant's test
* `ferm.py <number_to_test>`
* `ferm.py <number_to_test> <times>

example: `ferm.py 69` will run test only once or `ferm.py 69 3` will run test 3 times

## Generator
* `gen.py <element> <modulo>` - test if `<element>` is a generator in `Z*<modulo>`

example: `gen.py 3 10`

## Eulers function
* `phi.py <number>`
* `phi.py <factor_prime> <factor_prime> ... `

example: `phi.py 60` or `phi.py 2 2 3 5`  
Second usage is filled with prime factorization `60 = 2^2 * 3 * 5`

## Inverse element
* `inv.py <element> <modulo>`

example: `inv.py 5 12` gives and inverse of 5 in modulo 12 (only multiplicative group)

## Order
* `order.py <modulo>`  - prints out order of a group
* `order.py <element> <modulo>` - prints out order of an element in a group

example: `order.py 69` or `order.py 3 69`

## Complexity
* `complex.py` will show some basic info about computing complexity of an algorithm

# Requirements
In order to run above commands as shown you need to have installed [python](https://www.python.org/downloads/) interpret and either be in current directory with scripts or have path to them set in system variable `$PATH` (on Windows)

# Tip
For faster workflow type only first few letters and press `TAB` key for auto-compltion. This way you never have to type ".py" at least.

