# Scripts for Cryptologic Protocol Theory class
Project consists of scripts for Cryptologic Protocol Theory class. It's meant to support student's workflow through out the class.

# Scripts and their usage
## Elements of a group
* `elem.py <number_group>`

example: `elem.py 12` prints out elements of additive and multiplicative group Z12

## Greatest common divisor
* `gcd.py <a_number> <b_number>`

example: `gcd.py 9 7`

## Euler's totient function
* `phi.py <number>`
* `phi.py <factor_prime> <factor_prime> ... `

example: `phi.py 60` or `phi.py 2 2 3 5`  
Second usage is filled with prime factorization `60 = 2^2 * 3 * 5`

## Inverse element
* `inv.py <element> <modulo>`

example: `inv.py 5 12` gives and inverse of 5 in modulo 12 (only multiplicative group)

## Complexity
* `complex.py` will show some basic info about computing complexity of an algorithm

# Requirements
In order to run above commands as shown you need to have installed [python](https://www.python.org/downloads/) interpret and either be in current directory with scripts or have path to them set in system variable `$PATH` (on Windows)

# Tip
For faster workflow type only first few letters and press `TAB` key for auto-compltion. This way you never have to type ".py" at least.

