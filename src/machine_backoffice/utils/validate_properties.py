def validate(object: dict, property: str):
    response = {}
    try:
        response = object.__dict__[property]
    except Exception as _:
        response = {}
    try:
        response = object[property]
    except Exception as _:
        response = {}

    return response