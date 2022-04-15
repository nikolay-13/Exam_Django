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


def get_choice(item):
    choices = ((str(i), str(i)) for i in item)
    return choices


def get_qnt_choice(ran):
    choices = ((i, i) for i in range(1, ran + 1))
    return choices
