import pytest
from syrupy.assertion import SnapshotAssertion

from unpack_kwtypes.usage import movie_titles_containing_word_the


@pytest.mark.asyncio
async def test_nokwargs(snapshot: SnapshotAssertion) -> None:
    await movie_titles_containing_word_the(limit=5) == snapshot


@pytest.mark.asyncio
async def test_limit_order(snapshot: SnapshotAssertion) -> None:
    await movie_titles_containing_word_the(limit=5, order="DESC") == snapshot


@pytest.mark.asyncio
async def test_limit_offset(snapshot: SnapshotAssertion) -> None:
    await movie_titles_containing_word_the(limit=5, offset=5) == snapshot


@pytest.mark.asyncio
async def test_limit_offset_order(snapshot: SnapshotAssertion) -> None:
    await movie_titles_containing_word_the(limit=5, offset=5, order="DESC") == snapshot
