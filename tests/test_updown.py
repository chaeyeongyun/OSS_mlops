from core_codes.up_down_quiz import updown, rnd_val


def test_updown():
    assert updown(rnd_val)
    assert not updown(rnd_val-100)
