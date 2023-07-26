from core_codes.coined_term_quiz import is_correct, coined_term


def test_is_correct():
    for term in coined_term:
        assert is_correct(coined_term[term], coined_term[term])
        assert not is_correct(coined_term[term], 'abc')
