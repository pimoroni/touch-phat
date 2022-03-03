
import sys
import pytest
import mock


@pytest.fixture(scope='function', autouse=True)
def cleanup():
    """This fixture removes modules under test from sys.modules.
    This ensures that each module is fully re-imported, along with
    the fixtures for each test function.
    """

    yield None
    try:
        del sys.modules["touchphat"]
    except KeyError:
        pass


@pytest.fixture(scope='function', autouse=False)
def cap1xxx():
    """Mock cap1xxx module."""
    cap1xxx = mock.MagicMock()
    sys.modules['cap1xxx'] = cap1xxx
    yield cap1xxx
    del sys.modules['cap1xxx']
