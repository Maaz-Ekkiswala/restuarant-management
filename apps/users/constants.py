from collections import OrderedDict


class Role:
    MANAGER = 'manager'
    CUSTOMER = 'customer'

    FieldStr = OrderedDict({
        MANAGER: 'Manager',
        CUSTOMER: 'Customer',
    })

    @classmethod
    def choices(cls):
        return cls.FieldStr.items()
