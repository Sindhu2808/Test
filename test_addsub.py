import pytest
import add_sub


# @pytest.mark.skip(reason="skip add")

@pytest.mark.parametrize('a,b,res', [(5, 4, 9), (10, 20, 40), ('pf', 'sd', 'pfsd')])
def test_add(a,b,res):
    assert add_sub.add(a,b)==res
    # assert add_sub.add(10, 20) == 30
    # assert add_sub.add(6, 5) == 11

    # @pytest.mark.skipif(4 > 3, reason="four is greater than three")
    # def test_sub():
    #   assert add_sub.sub(5, 3) == 2
    #   assert add_sub.sub(20, 10) == 10

    # @pytest.mark.str
    # def test_add_string():
    # c = add_sub.add('pf', 'sd')
    # assert c == "pfsd"
    # assert type(c) is str

