CATEGORY = (
    ('SHIRTS', 'shirts'),
    ('JEANS', 'Jeans'),
    ('TOPS', 'Tops'),
    ('JACKETS', 'Jackets'),
    ('COATS', 'Coats'),
    ('SHOES', 'Shoes'),
)

GENDER = (
    ('MEN', 'men'),
    ("WOMEN", 'women'),
    ('KIDS', 'kids'),
)
SIZES = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
)
QNT_CHOICE = ((i, str(i)) for i in range(20))


def get_size_choice(item):
    choices = ((i, i) for i in item)
    return choices


def get_color_choice(item):
    choices = ((i, i) for i in item)
    return choices
