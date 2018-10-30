def test_block_metric(default_client, mocked_send):
    with default_client.block_metric("foo"):
        pass
    mocked_send.assert_any_call("foo.executions", 1)
    assert ("foo.processing_time" in
            [c[0][0] for c in mocked_send.call_args_list])


def test_decorator(default_client, mocked_send):
    @default_client.decorator
    def foo():
        pass

    mocked_send.assert_not_called()
    foo()
    mocked_send.assert_any_call("foo.executions", 1)
    assert ("foo.processing_time" in
            [c[0][0] for c in mocked_send.call_args_list])
