import pytest

from apps.products.models import Product


@pytest.mark.parametrize(
    'title, category, slug, description, regular_price, discount_price, validity',
    [
        ('NewTitle', 1, "NewDescription", "slug", "4.66", "3.99", True),
        ('NewTitle', 1, "NewDescription", "slug", "4.66", "3.99", False),
    ]
)

def test_product_instance(db, product_factory, title, category, description, slug, regular_price, discount_price, validity):
    test = product_factory(
        title=title,
        category_id=category,
        slug=slug,
        description=description,
        regular_price=regular_price,
        discount_price=discount_price,
    )
    item = Product.objects.all().count()
    assert item == validity
