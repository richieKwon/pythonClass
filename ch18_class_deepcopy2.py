import copy


class Basket:
    def __init__(self, product=None):
        if product is None:
            self._product = []
        else:
            # create a new object with list
            self._product = list(product)

    def put_prod(self, prod_name):
        self._product.append(prod_name)

    def del_prod(self, prod_name):
        self._product.remove(prod_name)


basket1 = Basket(['1', '2', '3'])
# copy the first type 만 다른 주소를 가진다.
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print(id(basket1), id(basket2), id(basket3))
print(id(basket1._product), id(basket2._product), id(basket3._product))
