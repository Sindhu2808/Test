from fetchdata import Stu


def test_sindhu_data():
    db = Stu();
    db.connect('stu.json')
    d = db.retrievedata('sindhu')
    assert d['sid'] == 32
    assert d['name'] == 'sindhu'


def test_dhanu_data():
    db = Stu();
    db.connect('stu.json')
    d = db.retrievedata('dhanu')
    assert d['sid'] == 32
