import pytest


def test_sync_example() -> None:
    """Example synchronous test."""
    assert True


@pytest.mark.asyncio
async def test_async_example() -> None:
    """Example asynchronous test."""
    assert True
