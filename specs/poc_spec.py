from mamba import description, context, it
from expects import expect, be_below, contain
from hypothesis import given
from hypothesis.strategies import text, integers, lists

from sut.methods import remove_zeros_from, get_positives


with description('Property Based Testing Proof of Concept specs') as self:
    with context('FEATURE: Removing zeros from a text'):
        with it('generates random text for input and checks that there are no zeroes at the output'):
            zero_char = '0'

            @given(text())
            def _test_sut(text):
                result = remove_zeros_from(text)

                expect(result).not_to(contain(zero_char))

            _test_sut()

    with context('FEATURE: Getting only the positive integers from a list'):
        with it('generates a random list of integers for input and checks there are no zeroes at the output'):
            zero = 0

            @given(lists(integers()))
            def _test_sut(items):
                result = get_positives(items)

                expect(result).not_to(contain(zero))
                expect(result).not_to(contain(be_below(zero)))

            _test_sut()
