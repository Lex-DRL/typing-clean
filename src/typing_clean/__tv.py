# encoding: utf-8
"""
``TypeVar``s import works in runtime, but some IDEs (PyCharm) can't see them and error out.
So, not a big deal: they're very simple, we just redefine them here.

As a submodule - to define them without underscores,
to make IDEs show their signatures as such (``KV`` in signature, not ``_KV``);
"""

from typing import TypeVar
try:
	from typing import ParamSpec
except ImportError:
	from typing_extensions import ParamSpec

# Any type:
T = TypeVar('T')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
T4 = TypeVar('T4')

# Key type:
KT = TypeVar('KT')
KT2 = TypeVar('KT2')
KT3 = TypeVar('KT3')
KT4 = TypeVar('KT4')

# Value type:
VT = TypeVar('VT')
VT2 = TypeVar('VT2')
VT3 = TypeVar('VT3')
VT4 = TypeVar('VT4')

# Any type covariant containers:
T_co = TypeVar('T_co', covariant=True)
T2_co = TypeVar('T2_co', covariant=True)
T3_co = TypeVar('T3_co', covariant=True)
T4_co = TypeVar('T4_co', covariant=True)

# Ditto contravariant:
T_contra = TypeVar('T_contra', contravariant=True)
T2_contra = TypeVar('T2_contra', contravariant=True)
T3_contra = TypeVar('T3_contra', contravariant=True)
T4_contra = TypeVar('T4_contra', contravariant=True)

P = ParamSpec('P')
P2 = ParamSpec('P2')
P3 = ParamSpec('P3')
P4 = ParamSpec('P4')
