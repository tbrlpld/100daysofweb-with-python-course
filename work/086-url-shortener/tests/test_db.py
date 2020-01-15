import pytest


@pytest.fixture
def table_connection():
    from short.db import DynamoTable
    table_connection_for_testing = DynamoTable("testing")

    yield table_connection_for_testing

    table_connection_for_testing.table.delete()


@pytest.fixture
def example_entry(table_connection):
    return table_connection.save_long_url("http://example.com")


class TestSaveMethod(object):
    def test_returns_dict(self, table_connection):
        response = table_connection.save_long_url("http://example.com")

        assert isinstance(response, dict)

    def test_returned_dict_keys(self, table_connection):
        response = table_connection.save_long_url("http://example.com")

        assert "short" in response.keys()
        assert "long_url" in response.keys()

    def test_value_of_short(self, table_connection):
        response = table_connection.save_long_url("http://example.com")

        short_value = response["short"]
        assert isinstance(short_value, str)
        assert len(short_value) == 4

    def test_saving_same_long_twice_yields_same_short(self, table_connection):
        response_1 = table_connection.save_long_url("http://example.com")
        short_1 = response_1["short"]

        response_2 = table_connection.save_long_url("http://example.com")
        short_2 = response_2["short"]

        assert short_1 == short_2

    def test_saving_different_long_leads_to_different_shorts(
        self,
        table_connection,
    ):
        response_1 = table_connection.save_long_url("http://example.com")
        short_1 = response_1["short"]

        response_2 = table_connection.save_long_url("http://otherexample.com")
        short_2 = response_2["short"]

        assert short_1 != short_2


class TestGetShortOfLongMethod(object):
    def test_finds_short_for_given_long_url(
        self,
        table_connection,
        example_entry,
    ):
        short = table_connection.get_short_of_long("http://example.com")

        assert short == example_entry["short"]


class TestGetLongFromShortMethod(object):
    def test_finds_saved_long_from_given_short(
        self,
        table_connection,
        example_entry,
    ):
        long_url = table_connection.get_long_from_short(example_entry["short"])

        assert long_url == example_entry["long_url"]
