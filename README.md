# Static typing with attached keyword-argument TypedDicts

This is repro showing a piece of code that I'd like `mypy` to handle better.

The line of thinking is:

- `Unpack` is great for static typing!
- I want to use `Unpack` to provide types for `**kwargs` in scenarios where a function I'm writing just forwards them to another function.
- I don't want to redefine the other function's keyword arguments in my code.
- It's okay to modify the other code for now to add a `TypedDict` describing its keyword arguments
- It would be nice if the other function and the keyword argument typed dictionary were associated somehow.
- A decorator can do the association of these two things, attaching a `kwtypes` attribute to the decorated function.
- `mypy` should be able to typecheck it.

> This code is async because the code this repro is based on is async, and we want to make sure a solution will work with async code too. ie, the `attach_kwtypes` decorator should apply to async functions as well, but the `kwtypes` attribute should be accessible from synchronous code.
