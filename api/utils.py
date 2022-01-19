def simplify_edition_name(edition_name):
    """
    The first two words in the edition name are always "MICHELIN Guide".
    Remove those, make all characters lower case, and replace spaces with
    hyphens to simplify the URIs.
    :param edition_name:
    :return:
    """
    simplified_name = '-'.join(edition_name.split()[2:]).lower()
    return simplified_name.replace('ñ', 'n')


def complicate_edition_name(simplified_name):
    """

    :param simplified_name:
    :return:
    """
    if simplified_name == 'espana':
        simplified_name = 'españa'

    short_edition_name = (simplified_name
                          .replace('-', ' ')
                          .title()
                          .replace(' Of ', ' of '))

    return f"MICHELIN Guide {short_edition_name}"
