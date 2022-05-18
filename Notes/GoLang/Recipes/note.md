- [env](#env)
  - [flags](#flags)
- [strings](#strings)
- [numbers](#numbers)
# env
- os.Args list commandline args
- The Go package for flag handling does not support flag combining like ls -ll, where there are multiple flags after a single dash. Each flag must be separate. The Go flag package also does not differentiate between long options and short ones. Finally, -flag and --flag are equivalent. 
## flags
- The first type is the simple name of the flag type such as Int. This function will return the pointer to the integer variable where the value of the parsed flag is.
- The XXXVar functions are the second type. These provide the same functionality, but you need to provide the pointer to the variable. The parsed flag value will be stored in the given variable.
- The Go library also supports a custom flag type. The custom type must implement the Value interface from the flag package.
# strings

# numbers
- The function Atoi of package strconv is, in fact, the ParseInt function with the base of 10.
