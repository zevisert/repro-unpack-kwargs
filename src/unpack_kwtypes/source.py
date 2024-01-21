from itertools import islice
from typing import Literal, LiteralString, TypedDict, Unpack

from unpack_kwtypes.decorator import attach_kwtypes


class Movie(TypedDict):
    title: str
    year: int


MOVIES: list[Movie] = [
    {"title": "The Matrix", "year": 1999},
    {"title": "Avatar", "year": 2009},
    {"title": "Star Wars: Episode IV - A New Hope", "year": 1977},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "year": 2001},
    {"title": "The Dark Knight", "year": 2008},
    {"title": "The Hunger Games", "year": 2012},
    {"title": "Django Unchained", "year": 2012},
    {"title": "The Godfather", "year": 1972},
    {"title": "The Shawshank Redemption", "year": 1994},
    {"title": "The Wolf of Wall Street", "year": 2013},
    {"title": "The Martian", "year": 2015},
    # Thanks copilot!
]


class QueryKeywordArgs(TypedDict, total=False):
    """Keyword arguments for query_db, to be attached to the function as a kwtypes attribute."""

    limit: int | None
    offset: int | None
    order: Literal["ASC", "DESC"]


@attach_kwtypes(QueryKeywordArgs)
async def query_db(
    title_query: LiteralString,
    /,
    **kwargs: Unpack[QueryKeywordArgs],
) -> list[Movie]:
    matched = sorted(
        [
            movie
            for movie in MOVIES
            if title_query.casefold() in movie["title"].casefold()
        ],
        key=lambda movie: movie["title"],
    )

    if kwargs.get("order", "ASC") == "DESC":
        matched = list(reversed(matched))

    if (offset := kwargs.get("offset", None)) is not None:
        matched = list(islice(matched, offset, None))

    if (limit := kwargs.get("limit", None)) is not None:
        matched = list(islice(matched, limit))

    return matched
