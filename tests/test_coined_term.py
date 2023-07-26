from core_codes.coined_term_quiz import coined_term, is_correct


def test_is_correct():
    for term in coined_term:
        assert is_correct(coined_term[term], coined_term[term])
        assert not is_correct("1234", coined_term[term])