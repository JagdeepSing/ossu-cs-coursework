# Computer Fundamentals

## What does a computer do?

- Fundamentally:

  - performs calculations, a billion calculations per second!
    - 2 operations per light-foot!!
  - remembers results, 100s of gigabytes of storage

- What kind of calculations?

  - build-in to the language
  - ones that you define as the programmer

## Are there limits?

- Despite its speed and size, a computer does have limitations
  - some problems still to complex
    - accurate weather prediction at a local scale
    - cracking encryption schemes
  - some problems are fundamentally impossible to compute
    - [Turing Halting Problem:](https://en.wikipedia.org/wiki/Halting_problem)
      - predicting whether a piece of code will always halt with an answer for any input

---

## Types of Knowledge

- **declarative knowledge** is statements of fact.

  - there is candy taped to the underside of one chair
  - square root of a number x is y such that y \* y = x

- **imperative knowledge** is a recipe or "how-to". Computation.

  - candy finding recipe:

    1. face the students at the front of the room
    2. count up 3 rows
    3. start from the middle section's left side
    4. count to the right 1 chair
    5. reach under chair and find it

  - [recipe for deducing square root of number x](http://mathforum.org/library/drmath/view/52609.html)
    1. start with a guess g
    2. if g\*g is close enough to x, stop and say g is the answer
    3. otherwise make a new guess by averaging g and x/g
    4. using the new guess, repeat process until close enough

## What is a recipe?

1. sequence of simple **steps**
2. **flow of control** process that specifies when each step is executed
3. a means of determining **when to stop**

   Steps 1+2+3 = an **algorithm**!!

---

## Exercise 1:

1. What is the difference between an Algorithm and a Program?

   An algorithm is a conceptual idea, a program is a concreat instantiation of an algorithm.

2. A computational mode of thinking means that everything can be viewed as a math problem involving numbers and formulas.
3. Computer Science is **NOT** the study of how to build efficient machines that run programs.
4. The two things every computer can do are: perform calculations and remember the results.

---

## Computers are machines

- how to capture a recipe in a mechanical process
- **fixed program** computer
  - calculator
  - Alan Turing's Bombe
- **stored program** computer
  - machine stores and executes instructions
  - emulating fixed program computer for each stored program

## Basic Machine Architecture

1. Memory
2. Arithmetic Logic Unit

- does primitive ops
- takes info from memory, reads it in, does primitive operation, stores data into memory

3. Control Unit

- program counter, points to instructions in memory
- keeps track of what specific operations needs to be done at any particular time

4. Input
5. Output

![Basic Machine Architecture](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Von_Neumann_Architecture.svg/1280px-Von_Neumann_Architecture.svg.png)

## Stored Program Computer

- sequence of **instructions stored** inside computer
  - built from predefined set of primitive instructions
    1. Arithmetic and Logic
    2. Simple Tests
    3. Moving Data
- special program (interpreter) **executes each instruction in order**
  - uses tests to change flow of control through sequence
  - stop when done

## Basic Primitives

- Turing showed you can **compute anything** using 6 primitives (Turing Complete)

  1. Move Right
  2. Move Left
  3. Print
  4. Scan
  5. Erase
  6. Nothing/Halt

- modern programming languages have more convenient set of primitives
- can **abstract** methods to **create new primitives**
- anything computable in one language is computable in any other programming language (Turing Complete property)

---

## Creating Recipes

- a programming language provides a set of primitive **operations**
- **expressions** are complex but legal combinations of primitives in a programming language
- expressions and computations have **values** and meanings in a programming language

## Aspects of Languages

- **primitive constructs**

  - English: words
  - programming language: numbers, strings, simple operators

- **syntax**

  - (determines whether a string is legal)
  - English:
    - "cat dog boy" -> not syntactically valid
    - "cat hugs boy" -> syntactically valid
  - programming language:
    - `"hi"5` -> not syntactically valid
    - `3.2\*5` -> syntactically valid

- **static semantics** is which syntactically valid strings have meaning

  - (determines whether a string has meaning)
  - English:
    - "I are hungry" -> syntactically valid but static semantic error programming language:
    - `3.2*5` -> syntactically valid
    - `3+"hi"` -> static semantic error

- **semantics** is the meaning associated with syntactically correct string of symbols with no static semantic errors

  - (assigns a meaning to a legal sentence)
  - English: can have many meanings --
    - "Flying planes can be dangerous"
    - "This reading lamp hasn't uttered a word since I bought it?"
  - programming languages: have only one meaning but may not be what programmer intended

## Where things go wrong

- **syntactic errors**
  - common and easily caught
- **static semantic errors**
  - some languages check for these before running program
  - can cause unpredictable behavior
- no semantic errors but **different meaning than what programmer intended**
  - program crashes, stops running
  - program runs forever
  - program gives an answer but different than expected
