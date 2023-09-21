import pytest


@pytest.mark.parametrize(
    ('n', 'expected'), [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        pytest.mark.xfail((1, 0)),
        pytest.mark.xfail(reason="some bug")((1, 0)),
        pytest.mark.skipif('sys.version_info >= (3,0)')((10, 11)),
    ]
)
def test_increment(n, expected):
    assert n + 1 == expected