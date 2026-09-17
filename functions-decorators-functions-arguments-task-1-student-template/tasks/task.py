from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc, *filters: ModifierFunc) -> DataType:
    result = selector(data)
    for f in filters:
        result = f(result)
    return result


def select(*columns: str) -> ModifierFunc:
    def selector(data):
        return [{key: row[key] for key in columns if key in row} for row in data]

    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    def filterer(data):
        return [row for row in data if row.get(column) in values]

    return filterer


def test_query():
    friends = [{"name": "Sam", "gender": "male", "sport": "Basketball"}]
    value = query(
        friends,
        select(*("name", "gender", "sport")),
        field_filter(*("sport", *("Basketball", "volleyball"))),
        field_filter(*("gender", *("male",))),
    )
    assert [{"gender": "male", "name": "Sam", "sport": "Basketball"}] == value


if __name__ == "__main__":
    test_query()
