def get_one(the_list, default_none=True):
    if len(the_list) > 1:
        raise Exception("list have more than one item")
    if the_list:
        return the_list[0]
    if default_none:
        return None
    else:
        raise Exception("there is no items")