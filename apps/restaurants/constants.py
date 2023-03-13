from collections import OrderedDict


class RestaurantStatus:
    OPEN = 'open'
    CLOSED = 'closed'

    FieldStr = OrderedDict({
        OPEN: 'Open',
        CLOSED: 'Closed',
    })

    @classmethod
    def choices(cls):
        return cls.FieldStr.items()