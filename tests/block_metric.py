import time

import pytest


def test_execution_metric(block_metric, mocked_send):
    with block_metric:
        pass

    mocked_send.assert_any_call("foo.executions", 1)


def test_errors_metric(block_metric, mocked_send):
    with block_metric:
        pass

    # Test that this call is not made
    with pytest.raises(AssertionError):
        mocked_send.assert_any_call("foo.errors", 1)

    with pytest.raises(Exception):
        with block_metric:
            raise Exception()

    mocked_send.assert_any_call("foo.errors", 1)


def test_processing_time_metric(block_metric, mocked_send):
    outer_time = time.time()
    with block_metric:
        time.sleep(0.1)
    outer_time = time.time() - outer_time

    found = False
    for call in mocked_send.call_args_list:
        if call[0][0] == "foo.processing_time":
            found = True
            assert outer_time > call[0][1] > 0.1
    assert found
