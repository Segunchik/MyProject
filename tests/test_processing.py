from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default():
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result = filter_by_state(data)

    for item in result:
        assert item["state"] == "EXECUTED"


def test_filter_by_state_canceled():
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    result = filter_by_state(data, state="CANCELED")

    for item in result:
        assert item["state"] == "CANCELED"


def test_sort_by_date_desc():
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    sorted_data = sort_by_date(data)
    assert sorted_data[0]["date"] == "2019-07-03T18:35:29.512364"
    assert sorted_data[-1]["date"] == "2018-06-30T02:08:58.425572"


def test_sort_by_date_asc():
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    sorted_data = sort_by_date(data, reverse=False)
    assert sorted_data[0]["date"] == "2018-06-30T02:08:58.425572"
    assert sorted_data[-1]["date"] == "2019-07-03T18:35:29.512364"
