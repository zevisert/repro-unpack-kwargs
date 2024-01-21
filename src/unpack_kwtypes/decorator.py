from __future__ import annotations
from abc import abstractmethod

from functools import wraps
from typing import (
    Callable,
    Generic,
    ParamSpec,
    TypeVar,
    cast,
)

P = ParamSpec("P")
R = TypeVar("R", covariant=True)
K = TypeVar("K", contravariant=False, covariant=False)


class DecoratedCallable(Generic[P, R, K]):
    kwtypes: K

    @abstractmethod
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        raise NotImplementedError()


def attach_kwtypes(
    kwtypes: K,
) -> Callable[[Callable[P, R]], DecoratedCallable[P, R, K]]:
    def decorator(func: Callable[P, R]) -> DecoratedCallable[P, R, K]:
        @wraps(func)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            return func(*args, **kwargs)

        decorated = cast(DecoratedCallable[P, R, K], wrapped)
        decorated.kwtypes = kwtypes
        return decorated

    return decorator
