# Python Regular Expressions (RegEx) Cheat Sheet

## Common Functions

| Function | Description | Example |
|----------|-------------|---------|
| `re.search(pattern, string)` | Returns first match object, or `None` | `re.search(r'\d+', 'abc123')` → Match for '123' |
| `re.match(pattern, string)` | Match only at BEGINNING of string | `re.match(r'\d+', 'abc123')` → `None` |
| `re.findall(pattern, string)` | Returns list of all matches | `re.findall(r'\d+', 'a1b22')` → `['1', '22']` |
| `re.finditer(pattern, string)` | Returns iterator of match objects | Useful for large texts |
| `re.sub(pattern, repl, string)` | Replace matches with `repl` | `re.sub(r'\d', 'X', 'a1b2')` → `'aXbX'` |
| `re.split(pattern, string)` | Split string by pattern | `re.split(r'\s+', 'a  b')` → `['a', 'b']` |
| `re.compile(pattern)` | Compile pattern for reuse | `p = re.compile(r'\d+')` |

## Character Classes

| Pattern | Matches |
|---------|---------|
| `.` | Any character EXCEPT newline |
| `\d` | Digit (0-9) |
| `\D` | Non-digit |
| `\w` | Word character (a-z, A-Z, 0-9, _) |
| `\W` | Non-word character |
| `\s` | Whitespace (space, tab, newline) |
| `\S` | Non-whitespace |
| `[abc]` | Any ONE of: a, b, or c |
| `[^abc]` | Any character EXCEPT a, b, or c |
| `[a-z]` | Any lowercase letter |
| `[A-Z]` | Any uppercase letter |
| `[0-9]` | Any digit (same as `\d`) |
| `[a-zA-Z0-9_]` | Same as `\w` |

## Anchors

| Pattern | Matches |
|---------|---------|
| `^` | Start of string (or line with `re.MULTILINE`) |
| `$` | End of string (or line with `re.MULTILINE`) |
| `\b` | Word boundary |
| `\B` | Non-word boundary |

**Examples:**
- `r'^hello'` matches `'hello world'` but not `'say hello'`
- `r'world$'` matches `'hello world'` but not `'world peace'`
- `r'\bcat\b'` matches `'cat'` in `'the cat sat'` but not `'category'`

## Quantifiers

| Pattern | Matches |
|---------|---------|
| `*` | 0 or more (greedy) |
| `+` | 1 or more (greedy) |
| `?` | 0 or 1 (optional) |
| `{n}` | Exactly n times |
| `{n,}` | n or more times |
| `{n,m}` | Between n and m times (inclusive) |
| `*?`, `+?`, `??` | Non-greedy (minimal) versions |

**Greedy vs Non-greedy:**
```python
text = '<div>hello</div>'
re.search(r'<.*>', text)   # Matches '<div>hello</div>' (greedy)
re.search(r'<.*?>', text)  # Matches '<div>' (non-greedy)
```

## Groups and Alternation

| Pattern | Description |
|---------|-------------|
| `(...)` | Capturing group |
| `(?:...)` | Non-capturing group |
| `(?P<name>...)` | Named capturing group |
| `\1`, `\2` | Backreference to group 1, 2, etc. |
| `a\|b` | Alternation - match a OR b |

**Examples:**
```python
r'(\d{3})-(\d{4})'      # Captures '123' and '4567' separately
r'(?:Mr|Mrs|Ms)\.'      # Matches title but doesn't capture
r'(?P<year>\d{4})'      # Named group 'year'
r'(\w+) \1'             # Matches repeated words like 'the the'
```

## Lookahead and Lookbehind

| Pattern | Description |
|---------|-------------|
| `(?=...)` | Positive lookahead - matches if `...` follows |
| `(?!...)` | Negative lookahead - matches if `...` doesn't follow |
| `(?<=...)` | Positive lookbehind - matches if `...` precedes |
| `(?<!...)` | Negative lookbehind - matches if `...` doesn't precede |

**Examples:**
- `r'\d+(?= dollars)'` matches `'100'` in `'100 dollars'`
- `r'(?<=\$)\d+'` matches `'50'` in `'$50'`

## Common Flags

| Flag | Description |
|------|-------------|
| `re.IGNORECASE` or `re.I` | Case-insensitive matching |
| `re.MULTILINE` or `re.M` | `^` and `$` match at line breaks |
| `re.DOTALL` or `re.S` | `.` matches newlines too |
| `re.VERBOSE` or `re.X` | Allow comments/whitespace in pattern |

**Combining flags:**
```python
re.search(r'hello', text, re.IGNORECASE | re.MULTILINE)
```

## Match Object Methods

```python
match = re.search(r'(\d+)-(\d+)', 'phone: 123-4567')

match.group()      # '123-4567'  (entire match)
match.group(0)     # '123-4567'  (same as above)
match.group(1)     # '123'       (first capture group)
match.group(2)     # '4567'      (second capture group)
match.groups()     # ('123', '4567')  (tuple of all groups)
match.start()      # 7           (start index)
match.end()        # 15          (end index)
match.span()       # (7, 15)     (tuple of start, end)

# With named groups:
match = re.search(r'(?P<area>\d+)-(?P<num>\d+)', '123-4567')
match.group('area')   # '123'
match.groupdict()     # {'area': '123', 'num': '4567'}
```

## Raw Strings - Important!

Always use raw strings `r'...'` for regex patterns to avoid escaping backslashes:

```python
# Good:
re.search(r'\d+', text)
re.search(r'\bword\b', text)

# Bad (but works):
re.search('\\d+', text)
re.search('\\bword\\b', text)
```

## Common Patterns

| Use Case | Pattern |
|----------|---------|
| Email (simple) | `r'[\w.-]+@[\w.-]+\.\w+'` |
| URL (simple) | `r'https?://[\w./%-]+'` |
| Phone (US) | `r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'` |
| Date (MM/DD/YYYY) | `r'\d{2}/\d{2}/\d{4}'` |
| Time (HH:MM) | `r'\d{2}:\d{2}'` |
| IP Address | `r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'` |
| Hashtag | `r'#\w+'` |
| Mention | `r'@\w+'` |
| HTML tag | `r'<[^>]+>'` |

## Quick Reference

```
.       Any char (not newline)     ^       Start of string
\d      Digit [0-9]                $       End of string
\D      Non-digit                  \b      Word boundary
\w      Word char [a-zA-Z0-9_]     *       0 or more
\W      Non-word char              +       1 or more
\s      Whitespace                 ?       0 or 1
\S      Non-whitespace             {n,m}   n to m times
[abc]   Any of a, b, c             (...)   Capture group
[^abc]  Not a, b, c                a|b     a or b
```