# Core Elements of Programs

## Strings, Branching, Iteration

---

### Review

#### Variables

- **name**
  - descriptive
  - meaningful
  - helps you re-read code
  - cannot be keywords (int, float, etc)
- **value**
  - information stored
  - can be updated

---

### Variable Binding with `=`

- compute the right hand side -> VALUE

- store it (aka bind it) in the left hand side -> VARIABLE

- left hand side will be replaced with new value

- `=` is called assignment

  `x = 2`		

  `x = x * x`

  `y = x + 1`

---

### Strings

- contained in single or double quotes
- letters, special characters, spaces, digits
- can add string together using `+`
- get length of string using `len("hello")` -> 5
- **indexing**
  - `"hello"[1]` -> "e" (second character in string)
  - `"hello"[-1]` -> "o" (last character in string)

- **slicing**
  - "string"[start​ : end : step]
  - `"hello"[1:3]` -> "el"
  - `"hello"[:3]` -> "hel"
  - `"hello"[1:]` -> "ello"
  - `"hello"[:]` -> "hello" (copy of original)

---

### Input/Output: print

- used to output stuff to console

  `x = 1`

  `print(x)`

  `x_str = str(x)`

  `print("my fav num is", x, ".", "x =", x)` -> all values separated by a space

  `print("my fav num is " + x_str + ". " + "x = " + x_str)`