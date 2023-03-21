from .conversions import to_base_62


def generate_slug(current_id, db_class):

    while True:

        slug = to_base_62(current_id)

        slug_exists = db_class.find_first(slug=slug)

        if not slug_exists:
            return slug

def generate_short_url(host_url, slug):

    return f'{host_url}{slug}'

