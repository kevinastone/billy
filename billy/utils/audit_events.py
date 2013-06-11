def string_attr(the_object, the_attribute):
    prop = getattr(the_object, the_attribute, None)
    if prop:
        try:
            return str(prop)
        except:
            return None
    else:
        return None



class EventCatalog(object):

    #CUSTOMER EVENTS
    CUSTOMER_CREATE = "CUSTOMER_CREATE"
    CUSTOMER_APPLY_COUPON = "CUSTOMER_APPLY_COUPON"
    CUSTOMER_REMOVE_COUPON = "CUSTOMER_REMOVE_COUPON"
    CUSTOMER_ADD_PLAN = "CUSTOMER_ADD_PLAN"
    CUSTOMER_CANCEL_PLAN = "CUSTOMER_CANCEL_PLAN"
    CUSTOMER_ADD_PAYOUT = "CUSTOMER_ADD_PAYOUT"
    CUSTOMER_CANCEL_PAYOUT = "CUSTOMER_CANCEL_PAYOUT"
    CUSTOMER_CHARGE_ATTEMPT = "CUSTOMER_CHARGE_ATTEMPT"
    CUSTOMER_CLEAR_DEBT = "CUSTOMER_CLEAR_DEBT"

    #Plan Invoice
    PRORATE_LAST_INVOICE = "PRORATE_LAST_INVOICE"






