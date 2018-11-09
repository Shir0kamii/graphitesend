import platform
import pytest

from graphitesend import GraphiteClient, GraphiteStructuredFormatter
from graphitesend.block_metric import BlockMetric


@pytest.fixture(params=["foo", "bar", "baz"])
def metric_name(request):
    return request.param


@pytest.fixture
def system_name():
    return platform.uname()[1]


@pytest.fixture
def default_formatter():
    return GraphiteStructuredFormatter()


@pytest.fixture
def default_client(mocker):
    mocker.patch('socket.socket')
    return GraphiteClient()


@pytest.fixture
def mocked_send(mocker, default_client):
    return mocker.patch.object(default_client, "send")


def test_mocked_send(mocked_send, default_client):
    assert default_client.send == mocked_send


@pytest.fixture
def block_metric(default_client):
    return BlockMetric(default_client, "foo")
