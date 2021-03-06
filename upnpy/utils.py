# -*- coding: utf-8 -*-
"""
utils.py
~~~~~~~~

Defines utility functions used by UPnPy.
"""
from xml.etree.ElementTree import Element, SubElement


def camelcase_to_underscore(text):
    """
    Convert a camelCasedString to one separated_by_underscores. Treats
    neighbouring capitals as acronyms and doesn't separated them, e.g. URL does
    not become u_r_l. That would be stupid.

    :param text: The string to convert.
    """
    outstr = []
    previous = ''

    for char in text:
        if char.islower():
            outstr.append(char)
        elif (len(outstr) > 0) and (previous.islower()):
            outstr.append('_')
            outstr.append(char.lower())
        else:
            outstr.append(char.lower())

        previous = char

    return ''.join(outstr)


def get_SOAP_RPC_base():
    """
    Prepares the base XML for a SOAP RPC call. Returns a tuple containg the
    root element and then the element that contains the body.
    """
    envelope = Element('s:Envelope',
                       {'xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/',
                        's:encodingStyle': 'http://schemas.xmlsoap.org/soap/encoding/'})
    body = SubElement(envelope, 's:Body')

    return envelope, body
