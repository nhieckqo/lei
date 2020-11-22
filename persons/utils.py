
#-------------------------------------------------------------------
def get_fullname(object):
    return  (str(object.firstname).strip() if object.firstname else "") + \
        ((" "+str(object.midname).strip()) if object.midname else "") + \
        ((" "+str(object.lastname).strip()) if object.lastname else "")

def get_fulladdress(object):
    return (str(object.address_num).strip() if object.address_num else "") + \
        ((" "+str(object.address_lot).strip()) if object.address_lot else "") + \
        ((" "+str(object.address_block).strip()) if object.address_block else "") + \
        ((" "+str(object.address_street).strip()) if object.address_street else "") + \
        ((" "+str(object.address_phase).strip()) if object.address_phase else "") + \
        ((" "+str(object.address_sitio).strip()) if object.address_sitio else "") + \
        ((" "+str(object.address_brgy).strip()) if object.address_brgy else "") + \
        ((" "+str(object.address_city).strip()) if object.address_city else "") + \
        ((" "+str(object.address_province).strip()) if object.address_province else "") + \
        ((" "+str(object.address_country).strip()) if object.address_country else "") + \
        ((" "+str(object.address_zipcode).strip()) if object.address_zipcode else "")
