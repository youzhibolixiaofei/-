def get_formatted_name(first_name, last_name, middle_name=' '):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name +  middle_name +  last_name
    else:
        full_name = first_name +  last_name
    return full_name.title()
musician = get_formatted_name('李','飞')
print(musician)