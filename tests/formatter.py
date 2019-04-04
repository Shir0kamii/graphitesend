from graphitesend import TemplateFormatter, GraphiteStructuredFormatter


def test_template_name(metric_name):
    name_formatter = TemplateFormatter("{name}")
    assert metric_name == name_formatter(metric_name)


def test_template_group(metric_name):
    name_formatter = TemplateFormatter("{group}.{name}", group=lambda _: "boo")
    assert "boo." + metric_name == name_formatter(metric_name)


def test_default_prefix(default_formatter, system_name):
    assert default_formatter.prefix == "systems.{}.".format(system_name)


def test_arg_prefix(system_name):
    formatter = GraphiteStructuredFormatter(prefix="foo")
    assert formatter.prefix == "foo.{}.".format(system_name)


def test_arg_group(system_name):
    formatter = GraphiteStructuredFormatter(group="foo")
    assert formatter.prefix == "systems.{}.foo.".format(system_name)


def test_arg_system_name():
    formatter = GraphiteStructuredFormatter(system_name="foo")
    assert formatter.prefix == "systems.foo."
