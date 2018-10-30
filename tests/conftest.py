import platform
import pytest

from graphitesend import GraphiteStructuredFormatter


@pytest.fixture
def system_name():
    return platform.uname()[1]


@pytest.fixture
def default_formatter():
    return GraphiteStructuredFormatter()
