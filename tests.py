import nose.tools as n

from moving_window import window

def test_window():
    observed = list(map(tuple,window(range(8), n = 3)))
    expected = [
        (0,1,2),
        (1,2,3),
        (2,3,4),
        (3,4,5),
        (4,5,6),
        (5,6,7),
    ]
    n.assert_list_equal(observed, expected)
