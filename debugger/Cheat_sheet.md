# Python Debugger (pdb) Cheat Sheet

## Starting the Debugger

| Method | Usage |
|--------|-------|
| `breakpoint()` | Insert in code (Python 3.7+, recommended) |
| `import pdb; pdb.set_trace()` | Insert in code (classic approach) |
| `python -m pdb script.py` | Run script in debug mode from terminal |

## Navigation Commands

| Command | Short | Description |
|---------|-------|-------------|
| `next` | `n` | Execute next line (step over functions) |
| `step` | `s` | Step into function call |
| `continue` | `c` | Continue until next breakpoint |
| `return` | `r` | Continue until current function returns |
| `until` | `unt` | Continue until line number or end of frame |
| `jump <line>` | `j` | Jump to a specific line number |

## Inspecting Code

| Command | Short | Description |
|---------|-------|-------------|
| `list` | `l` | Show 11 lines around current position |
| `list <start>, <end>` | `l 1, 20` | Show specific line range |
| `longlist` | `ll` | Show entire current function |
| `where` | `w` | Show call stack (traceback) |
| `up` | `u` | Move up one level in call stack |
| `down` | `d` | Move down one level in call stack |

## Inspecting Variables

| Command | Description |
|---------|-------------|
| `p <expr>` | Print value of expression |
| `pp <expr>` | Pretty-print value of expression |
| `p locals()` | Print all local variables |
| `pp locals()` | Pretty-print all local variables |
| `p globals()` | Print all global variables |
| `display <expr>` | Display expression value each step |
| `undisplay <expr>` | Stop displaying expression |
| `interact` | Start interactive Python interpreter |

## Breakpoints

| Command | Short | Description |
|---------|-------|-------------|
| `break` | `b` | List all breakpoints |
| `break <line>` | `b 15` | Set breakpoint at line number |
| `break <func>` | `b my_func` | Set breakpoint at function |
| `break <file>:<line>` | `b utils.py:10` | Set breakpoint in specific file |
| `break <line>, <cond>` | `b 15, x > 5` | Conditional breakpoint |
| `tbreak <line>` | | Temporary breakpoint (auto-clears) |
| `clear` | `cl` | Clear all breakpoints |
| `clear <num>` | `cl 1` | Clear breakpoint by number |
| `disable <num>` | | Disable breakpoint |
| `enable <num>` | | Enable breakpoint |

## Execution Control

| Command | Short | Description |
|---------|-------|-------------|
| `quit` | `q` | Exit debugger (terminates program) |
| `restart` | `run` | Restart the program |
| `!<statement>` | | Execute Python statement |

## Useful Expressions in pdb
```python
# Show all local variables (clean)
pp locals()

# Filter out dunder variables
{k: v for k, v in locals().items() if not k.startswith('_')}

# Check type of variable
type(variable_name)

# Check attributes of object
dir(object_name)

# Evaluate any Python expression
p len(my_list)
p my_dict.keys()
```

## Environment Variables

| Variable | Effect |
|----------|--------|
| `PYTHONBREAKPOINT=0` | Disable all breakpoints |
| `PYTHONBREAKPOINT=ipdb.set_trace` | Use ipdb instead |
| `PYTHONBREAKPOINT=pudb.set_trace` | Use pudb instead |

## Example Debugging Session
```python
def buggy_function(items):
    total = 0
    for item in items:
        breakpoint()  # Debugger pauses here
        total + item  # Bug: missing assignment
    return total

buggy_function([1, 2, 3])
```
```
# Debugger session:
> buggy_function()
-> total + item
(Pdb) p total        # Check current total
0
(Pdb) p item         # Check current item
1
(Pdb) n              # Go to next iteration
(Pdb) p total        # Total still 0 - found the bug!
0
(Pdb) q              # Quit debugger
```

## Quick Reference
```
n       → next line
s       → step into
c       → continue
l       → list code
p var   → print variable
pp locals() → see all variables
w       → where am I (stack)
b 20    → breakpoint at line 20
q       → quit
```