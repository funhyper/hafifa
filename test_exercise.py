from unittest.mock import MagicMock, patch

import pytest

from pytest_exercise import SimpleHasher, SecureVault

# CR: I changed the exrcise a bit (I know it will break your tests, sorry about that) and added custom exceptions instead of the generic ones that were before, so it's easier to test on these specifically

# CR: each test should have Arrange, Act, Assert parts (which you write in a comment, for example)

def test__int__returns_integer_from_string():
    # Arrange
    test_num = "1"

    # Act
    result = int(test_num)

    # Assert
    assert result == 1

# CR: Of course not every test has Arrange, or some tests' Act and Assert can be combined (so you can do Act + Assert)

# CR: Our convention for test method names: test__{what_are_we_testing}__{what_are_we_expecting_to_happen}

# CR: You can just call it secure_vault - this way all methods that get it will also call it secure_vault, and it's kinda similar to DIP
# CR: There are many tests you start by unlocking it - perhaps you want to add another fixture (unlocked_secure_vault)
@pytest.fixture
def example_secure_vault() -> SecureVault:
    return SecureVault(0, SimpleHasher(), "hash_abc")

# CR: Good test naming - I usually like __ instead of _ so it's easier to read the separated parts (test__simple_hasher__returns_inverted_pin_number)
def test_simple_hasher_returns_inverted_pin_number():
    simple_hasher = SimpleHasher()
    # CR: Use parametrization
    assert simple_hasher.hash_pin("123") == "hash_321"


def test_initializing_secure_value_with_negative_value_raises_value_error():
    # CR: Practice parameterization and pass different negative amounts
    mock = MagicMock()
    negative_balance = -1

    # CR: You can do "with pytest.raises" and use it as context manager instead of passing a method
    pytest.raises(ValueError, lambda: SecureVault(negative_balance, mock, "xyz"))


def test_secure_vault_unlocks_successfully(example_secure_vault):
    example_secure_vault.unlock("cba")
    assert not example_secure_vault.is_locked


# CR: Interesting test name
def test_secure_vault_raises_runtime_error_when_unlocked_when_already_unlocked(example_secure_vault):
    example_secure_vault.unlock("cba")
    # CR: context manager pytest.raises
    pytest.raises(RuntimeError, lambda: example_secure_vault.unlock("cba"))


# CR: Also interesting test name - try to focus on what *exactly* the test checks - "when there are 3 attempts" is kind of redundant - you can just say that you are checking running out of attempts or something like that
@patch('random.randint')
def test_secure_vault_raises_permission_error_when_there_are_3_attempts_and_vault_has_security(
        mock_random_randint, example_secure_vault):
    mock_random_randint.return_value = 1
    for _ in range(2):
        example_secure_vault.unlock("123")
    # CR: context manager pytest.raises
    pytest.raises(PermissionError, lambda: example_secure_vault.unlock("123"))


# CR: this test and the one before are both the same, if we ignore the randint part:
# CR: you can check the return value of has_security for example (if random int is...) in a different test
# CR: Check for the specific message in the errors to separate between the two situations (with/without security) - since this is kinda weird, I changed the exercise to raise SecurityGuardError in that case - this way you can separate between the 2 errors
# CR: in this method, use mock on the secure vault has_security (it was "private" by accident, now I changed it to public method) instead of actively patching rand to get the result you want
@patch('random.randint')
def test_secure_vault_raises_permission_error_when_there_are_3_attempts_and_vault_doesnt_have_security(
        mock_random_randint, example_secure_vault):
    mock_random_randint.return_value = 4
    for _ in range(2):
        example_secure_vault.unlock("123")
    # CR: context manager pytest.raises
    pytest.raises(PermissionError, lambda: example_secure_vault.unlock("123"))


# CR: Great test!
def test_secure_vault_locks_successfully(example_secure_vault):
    example_secure_vault.unlock("cba")
    example_secure_vault.lock()
    assert example_secure_vault.is_locked


def test_deposit_to_vault_raises_runtime_error_when_vault_is_locked(example_secure_vault):
    # CR: context manager pytest.raises
    pytest.raises(RuntimeError, lambda: example_secure_vault.deposit(100))


def test_deposit_negative_amount_raises_value_error(example_secure_vault):
    example_secure_vault.unlock("cba")
    # CR: context manager pytest.raises
    pytest.raises(ValueError, lambda: example_secure_vault.deposit(-1))

@pytest.mark.parametrize("amount", [
    5,
    10,
    20,
    100,
    200
])
def test_deposit_updates_balance(amount, example_secure_vault):
    example_secure_vault.unlock("cba")
    example_secure_vault.deposit(amount)
    # CR: Perhaps check the return value of the deposit method as well (and another test that makes sure that the deposit/withdraw method returns the new balance)
    assert example_secure_vault.balance == amount

def test_withdraw_when_locked_raises_runtime_error(example_secure_vault):
    # CR: context manager pytest.raises
    pytest.raises(RuntimeError, lambda: example_secure_vault.withdraw(100))

def test_withdraw_amount_above_balance_raises_value_error(example_secure_vault):
    example_secure_vault.unlock("cba")
    example_secure_vault.deposit(10)
    # CR: context manager pytest.raises
    pytest.raises(ValueError, lambda: example_secure_vault.withdraw(20))


@pytest.mark.parametrize("amount", [
    5,
    10,
    20,
    100,
    200
])
def test_withdraw_updates_balance(amount, example_secure_vault):
    example_secure_vault.unlock("cba")
    # CR: Move this 500 to a parameter inside the parametrization
    example_secure_vault.deposit(500)

    example_secure_vault.withdraw(amount)
    # CR: Perhaps check the return value of the withdraw method as well
    assert example_secure_vault.balance == (500 - amount)


# CR: Add test for has_security (now public method)