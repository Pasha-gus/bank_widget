def filter_by_state(list_of_dicts: list, state="EXECUTED") -> list:
    filtered_list = [d for d in list_of_dicts if d.get("state") == state]
    return filtered_list


def sort_by_date(list_of_dicts: list, order="desc") -> list:
    sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=(order == "desc"))
    return sorted_list


sorted_list_desc = filter_by_state(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)

print(sorted_list_desc)
