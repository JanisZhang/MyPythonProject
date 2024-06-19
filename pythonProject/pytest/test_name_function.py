from name_function import get_formatted_name

def test_formatted_name():
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
    # assert formatted_name == ''
