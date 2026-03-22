import pytest

from code.pytest_exercise import SimpleHasher


@pytest.mark.parametrize("pin_number", [
    "123",
    "456",
    "789"
])
def test__hash_pin__returns_inverted_pin_number(pin_number):
    # Arrange
    simple_hasher = SimpleHasher()
    # Act + Assert
    assert simple_hasher.hash_pin(pin_number) == f"hash_{pin_number[::-1]}"