from box import Box

def parse_month_as_string(response, **kwargs):
    month = kwargs['variables']['birthMonth_from_main_source']
    monthAsInt = None

    match month:
        case "July":
            monthAsInt = "07"
        case "October":
            monthAsInt = "10"
        case _:
            raise Exception("Month not supported")

    return Box({"month_from_func": monthAsInt})