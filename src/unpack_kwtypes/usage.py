from typing import TYPE_CHECKING, Unpack
from unpack_kwtypes.source import query_db, Movie


async def movie_titles_containing_word_the(
    **kwargs: Unpack[query_db.kwtypes],
) -> list[Movie]:
    return await query_db("the", **kwargs)


if TYPE_CHECKING:
    # src/unpack_kwtypes/usage.py:14: note: Revealed type is "def (**kwargs: Any) -> typing.Coroutine[Any, Any, builtins.list[TypedDict('unpack_kwtypes.source.Movie', {'title': builtins.str, 'year': builtins.int})]]"
    # Expecting: "def (**kwargs: Unpack[TypedDict('unpack_kwtypes.source.QueryKeywordArgs', {'limit'?: Union[builtins.int, None], 'offset'?: Union[builtins.int, None], 'order'?: Union[Literal['ASC'], Literal['DESC']]})]) -> typing.Coroutine[Any, Any, builtins.list[TypedDict('unpack_kwtypes.source.Movie', {'title': builtins.str, 'year': builtins.int})]]"
    reveal_type(movie_titles_containing_word_the)
    # src/unpack_kwtypes/usage.py:17: note: Revealed type is "def (*, limit: Union[builtins.int, None], offset: Union[builtins.int, None], order: Union[Literal['ASC'], Literal['DESC']]) -> TypedDict('unpack_kwtypes.source.QueryKeywordArgs', {'limit'?: Union[builtins.int, None], 'offset'?: Union[builtins.int, None], 'order'?: Union[Literal['ASC'], Literal['DESC']]})"
    # Expecting: "TypedDict('unpack_kwtypes.source.QueryKeywordArgs', {'limit'?: Union[builtins.int, None], 'offset'?: Union[builtins.int, None], 'order'?: Union[Literal['ASC'], Literal['DESC']]})"
    reveal_type(query_db.kwtypes)
