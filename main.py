# Simple string formatter function

def format_name(f_name, l_name):
    """
    Formats and returns full name in title case.

    :param f_name: First name
    :type f_name: string
    :param l_name: Last name
    :type l_name: string

    :return: Formatted full name - first name in title case, last name in upper case.

    Example:
        >>> format_name("john", "snow")
        'John SNOW'
    """
    if f_name == "" or l_name == "":
        return "Invalid inputs."

    formated_f_name = f_name.title()
    formated_l_name = l_name.upper()
    return print(f"Formatted name: {formated_f_name} {formated_l_name}")


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

format_name(first_name, last_name)
