<div align="center">

# typing-clean

[![PyPI][pypi-shield]][pypi-url]
[![GitHub Release][github-release-shield]][github-release-url]

[pypi-shield]: https://img.shields.io/pypi/v/typing-clean?logo=pypi
[pypi-url]: https://pypi.org/p/typing-clean
[github-release-shield]: https://img.shields.io/github/v/release/Lex-DRL/typing-clean?logo=github
[github-release-url]: https://github.com/Lex-DRL/typing-clean/releases/latest

*Syntax sugar: import contents of built-in `typing` module — with protected and shortened names.*<br/>(`_A` for `Any`, `_C` for `Callable`, etc.)
</div>

> ## TL;DR
> You like type-hinted python, but you hate how much **EVERY** module's namespace is cluttered with `typing` objects? Then:
> - Instead of importing from `typing`, import from this `typing_clean`;
> - Use the same objects, just their names prefixed with underscores (`Iterable` -> `_Iterable`);
> - They will stay inside your module, never auto-propagating up the import chain;
> - Ask the maintainers of the lib you use to adopt `typing-clean`, too.
> 
> This module is deliberately the most barebones wrapper: it implements NOTHING. It merely imports from `typing` with different names. Any IDE should be 100% compatible with it.

---

## What and why
By its very purpose, the entire contents of the built-in `typing` module is what you'd call "implementation details": whenever **any** of its objects get imported in a module, they should stay hidden **inside** the module - never to be suggested by an IDE's autocomplete. And, ideally, never even visible from outside.

But, as you are well aware, this is not what happens. Instead, if you want to code typed python, you're presented a dilemma of **how** your own module will get polluted by `typing` - with either or both of:
- `typing`'s own objects spilled all over your module, while being irrelevant for an outer scope where your module is imported.
  - To add insult to injury, all the "standard" (i.e., non-underscored) names are by default imported into outer scope with wildcard import (`from your_module import *`), so your module pollutes them upstream... unless you manually add EVERYTHING your module defines by itself to its `__all__`.
- importing only `typing` itself, but adding long prefixes of `typing.SpecificType` everywhere in your code.

Both clutter the code and IDE autocomplete - either in your own module or from outside.

Ideally, your module should import any typing-related objects with a private (dunder) or at least protected (`_`) name. But now you just move boilerplate code to the imports section, making it tedious to import each type-hinting class in each of your submodules with `as`:
```python
from typing import Mapping as _Mapping, TypeVar as _TypeVar, ...
```

You **could** define your own service submodule which simply imports from `typing` with the right names, but then you won't be able to wildcard-import those names from it, unless you list every single name inside `__all__`... which is exactly what **this** package does:
- The classes from `typing` are imported with underscore prefix;
- many of the most used ones also have aliases where they are further shortened to just one letter (full names still available);
- `typing` itself is also imported as `_t`, just in case;
- this module defines its `__all__`, so:
  - in **your** module, you can do `from typing_clean import *`,
  - but the imported objects come underscored, so for an **outer** module (where yours got imported from), they don't get wildcard-imported.

<div align="center">

### Short names

| Here | Built-in |
|---|---|
| `_A` | `Any` |
| `_C` | `Callable` |
| `_G` | `Generator` |
| `_O` | `Optional` |
| `_M` | `Mapping` |
| `_P` | `Protocol` |
| `_U` | `Union` |
</div>
