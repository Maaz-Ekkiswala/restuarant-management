from collections import OrderedDict


class SessionStatus:
    ACTIVE = "active"
    EXPIRED = "expired"

    FieldStr = OrderedDict({
        ACTIVE: 'Active',
        EXPIRED: 'Expired',
    })

    @classmethod
    def choices(cls):
        return cls.FieldStr.items()


class OrderStatus:
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

    FieldStr = OrderedDict({
        OPEN: 'Open',
        CLOSED: 'Closed',
        CANCELLED: 'Cancelled'
    })

    @classmethod
    def choices(cls):
        return cls.FieldStr.items()