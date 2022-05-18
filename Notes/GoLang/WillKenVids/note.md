- [types](#types)
  - [bool](#bool)
  - [simple number](#simple-number)
  - [slice](#slice)

# types
## bool
- and := true && false
## simple number
## slice
- 3 components:
  - A pointer to some element of a backing array that represents the first element of the slice (not necessarily the first element of the array)
  - A length, representing the number of elements in the slice
  - A capacity, which represents the upper value of the length
  - If not otherwise specified, the capacity value equals the number of elements between the start of the slice and the end of the backing array.
- slices are typed only according to the type of their elements, not their number. The make built-in function can be used to create a slice with a nonzero length 
- m = append(m, 3), The reason for this is that behind the scenes, if the destination has sufficient capacity to accommodate the new elements, then a new slice is constructed from the original underlying array. If not, a new underlying array is automatically allocated.
