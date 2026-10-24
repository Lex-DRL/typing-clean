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
> - Instead of importing from `typing` or `typing_extensions`, import from this `typing_clean`;
> - Use the same objects, just their names prefixed with underscores (`Iterable` -> `_Iterable`);
> - They will stay inside your module, never auto-propagating up the import chain;
> - Ask the maintainers of the lib you use to adopt `typing-clean`, too.

---

## Version
- First two numbers: oldest Python version supported;
- Last number: minor update within it.

The installed python and `typing-extensions` determine which version of `typing-clean` to install.

## How
This module is deliberately the most barebones wrapper: it implements NOTHING. It merely imports from `typing` and `typing_extensions` with prefixed names. Any IDE should be 100% compatible with it.

## What and why
By its very purpose, the entire contents of the built-in `typing` module is what you'd call "implementation details": whenever **any** of its objects get imported in a module, they should stay hidden **inside** the module - never to be suggested by an IDE's autocomplete when the module itself gets imported.

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
- missing/updated classes are imported from `typing_extensions` - you get the most full set of typing classes in one place;
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
| `_I` | `Iterable` |
| `_M` | `Mapping` |
| `_NT` | `NamedTuple` |
| `_O` | `Optional` |
| `_U` | `Union` |
| `_IV` | `ItemsView` |
| `_KV` | `KeysView` |
| `_VV` | `ValuesView` |
</div>

### `TypeVar`s

The only thing the module defines by itself is a set of TypeVars:
- both in `typing` and `typing_extensions` the defined ones aren't exported, so even though at runtime their import works just fine, some IDEs complain that they can't find them;
- the built-in set was too short for me, so I defined extra 3 numbered versions for each.

<div align="center">

| What | Built-in equivalent | +Second | +Third | +Fourth |
|---|---|---|---|---|
| Just any arbitrary type | `_T` | `_T2` | `_T3` | `_T4` |
| Key type for dicts | `_KT` | `_KT2` | `_KT3` | `_KT4` |
| Value type for dicts | `_VT` | `_VT2` | `_VT3` | `_VT4` |
| Type covariant:<br/>`TypeVar(..., covariant=True)` | `_T_co` | `_T2_co` | `_T3_co` | `_T4_co` |
| Ditto contravariant:<br/>`TypeVar(..., contravariant=True)` | `_T_contra` | `_T2_contra` | `_T3_contra` | `_T4_contra` |
| [Parameter specifier](https://docs.python.org/3/library/typing.html#typing.ParamSpec) | `_P` | `_P2` | `_P3` | `_P4` |
</div>