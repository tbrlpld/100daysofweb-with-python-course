import pytest


class MockLimit(object):
    """
    Class to provide mocked returns for a max number of times.

    During instantiation, define the `mockreturn`. This is the value
    that will be initially returned by `mocking_func`.
    On every of these returns, the `mock_count` of the instance is
    increased. If the `mock_count` reaches the `mock_count_max` limit,
    then `mocking_func` will not return `mockreturn` anymore.
    Rather, the return value of `mocking_func` is defined by the return
    value of the `fallback_func`.

    Say you wish to mock the return of function `foo.bar` to be `baz`
    for 3 times. After you received the mock value 3 times, you wish
    to actually get the original functionality of `foo` back, then you
    set the `fallback_func` to be `foo.bar`.

    To get the above example, you would set it up like so:
    ```
    import foo
    foo_bar_mocker = MockLimit("baz", 3, foo.bar)
    monkeypatch.setattr(foo, "bar", foo_bar_mocker.mocking_func)
    ```

    """

    def __init__(self, mockreturn, mock_count_max, fallback_func):
        self.mock_count_max = mock_count_max
        self.mock_count = 0
        self.mockreturn = mockreturn
        self.fallback_func = fallback_func

    def mocking_func(self, *args, **kwargs):
        """
        Return mockreturn or fallback_func return depending on count.

        """

        if self.mock_count < self.mock_count_max:
            self.mock_count += 1
            return self.mockreturn
        return self.fallback_func()


@pytest.fixture
def table_connection():
    from short.db import DynamoTable
    table_connection_for_testing = DynamoTable("testing", local=True)

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

    def test_trailing_newlines_are_stipped_from_long_url(
        self,
        table_connection,
    ):
        response = table_connection.save_long_url("http://example.com\n")

        assert response["long_url"] == "http://example.com"

    def test_handing_when_random_key_generates_short_key_already_in_db(
        self,
        table_connection,
        example_entry,
        monkeypatch,
    ):
        first_short = example_entry["short"]
        # Mock `random_string` to produce the same value again. It could
        # actually be set to produce the same "random value" more than once.
        # We just need to define some limit to prevent the test getting stuck
        # because in a never ending loop. Also, we can assume that the
        # `random_string` function will eventually generate a key that is not
        # already in the database.
        from short import db
        random_mocker = MockLimit(first_short, 1, db.random_string)
        monkeypatch.setattr(db, "random_string", random_mocker.mocking_func)

        second_response = table_connection.save_long_url("http://example2.com")
        second_short = second_response["short"]

        assert second_short != first_short
        assert (
            table_connection.get_long_from_short(first_short)
            == example_entry["long_url"]
        )
        assert (
            table_connection.get_long_from_short(second_short)
            == "http://example2.com"
        )


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


class TestRandomString(object):
    def test_mocking_random_string_2_of_3_times(
        self,
        monkeypatch,
    ):
        """
        Test to show how `random_string` function can be mocked.

        In the given configuration, the `random_string` function is mocked
        twice and then the original functionality is restored. This is
        handled through the MockLimit class without the need to a context
        manager.

        This can be useful to test generation of duplicate short keys.
        The first execution can be used to create the first entry in the
        database. Then a second entry in the database for a (different) long
        URL is supposed to be made. But by "accident" (in this case design),
        the second generated "random string" is the same as the first. The
        handling of such a case will likely involve additional execution of the
        `random_string` function until a short key is found that is not
        contained in the database yet.

        Because we can expect the `random_string` function to eventually
        generate a key that is not in the database, we need to fallback to its
        original functionality.

        The mocking of that kind is demonstrated below. The limit of 2
        executions that get the same response is arbitrary. Since the idea of
        this test is to simply show the possibility of the mocking for limited
        number of executions, it could be set to any limit, but 2 out of 3
        should be fine to get the idea.

        """
        from short import db
        random_mocker = MockLimit("m0ck", 2, db.random_string)
        monkeypatch.setattr(db, "random_string", random_mocker.mocking_func)

        short1 = db.random_string()
        short2 = db.random_string()
        short3 = db.random_string()

        assert short1 == "m0ck"
        assert short2 == "m0ck"
        assert short3 != "m0ck"
