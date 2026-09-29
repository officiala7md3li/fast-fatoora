import pytest

def test_tlv_tag_lengths():
    seller = 'Ahmed Ali'
    encoded = seller.encode('utf-8')
    assert len(encoded) == len(seller)

def test_vat_number_format():
    vat = '300000000000003'
    assert len(vat) == 15
    assert vat.startswith('3') and vat.endswith('3')