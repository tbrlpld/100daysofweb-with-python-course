import pytest


@pytest.fixture
def table_connection():
    from short.db import DynamoTable
    table_connection_for_testing = DynamoTable("testing")

    yield table_connection_for_testing

    table_connection_for_testing.table.delete()


def test_saving_a_long_url_returns_dict(table_connection):
    response = table_connection.save_long_url("http://example.com")

    assert isinstance(response, dict)
