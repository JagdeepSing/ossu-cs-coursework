# Python

## Python Programs

- a **program** is a sequence of definitions and commands

  - definitions **evaluated**
  - commands **executed** by Python interpreter in a shell

- **commands** (statements) instruct interpreter to do something

- can be typed directly in a **shell** or stored in a file that is read into the shell and evaluated

## Objects

- programs manipulate **data objects**
- objects have a **type** that defines the kinds of things programs can do to them
- objects are either:
  - scalar (cannot be subdivided)
  - non-scalar (have internal structure than can be accessed)

### Scaler Objects

- `int` - represent **integers**
- `float` - represent **real numbers**
- `bool` - represent **Boolean** values
- `NoneType` - **special** and has one value, `None`
- can use `type(...)` to see the type of an object

### Type Conversions (Cast)

- can **convert object of one type to another**
- `float(3)` converts integer 3 to float 3.0
- `int(3.9)` truncates float 3.9 to integer 3

## Printing to console

- to show output from code to a user, use `print` command
- no 'OUT' because no value returned, just something printed
- `print(...)`

## Expressions

- combine objects and operators to form expressions
- an expression has a value, which has a type
- syntax for a simple expression `<object> <operator> <object>`

## Operators on ints and floats

- `i+j` -> the **sum** (if both ints, result is int. if either or both are floats, result is float)
- `i-j` -> the **difference** (if both ints, result is int. if either or both are floats, result is float)
- `i*j` -> the **product** (if both ints, result is int. if either or both are floats, result is float)

* `i/j` -> **division** (float)
* `i//j` -> **int division** (result is int, quotient w/o remainder)
* `i%j` -> the **remainder** when i is divided by j
* `i**j` -> i to the **power** of j

## Simple Operations

- parentheses used to tell Python to do these operations first
- **operator procedence** without parentheses
  - \*\*
  - \*
  - /
  - - and -
  - executed left to right, as appear in expression
