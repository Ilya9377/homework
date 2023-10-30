def check_dict(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    res = []
    for d in data:
        if d["state"] == state:
            res.append(d)
    return res


