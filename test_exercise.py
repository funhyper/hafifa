from unittest.mock import MagicMock, patch

import pytest

from pytest_exercise import SimpleHasher, SecureVault


@pytest.fixture
def example_secure_vault() -> SecureVault:
    return SecureVault(0, SimpleHasher(), "hash_abc")


def test_simple_hasher_returns_inverted_pin_number():
    simple_hasher = SimpleHasher()
    assert simple_hasher.hash_pin("123") == "hash_321"


def test_initializing_secure_value_with_negative_value_raises_value_error():
    mock = MagicMock()
    negative_balance = -1

    pytest.raises(ValueError, lambda: SecureVault(negative_balance, mock, "xyz"))


def test_secure_vault_unlocks_successfully(example_secure_vault):
    example_secure_vault.unlock("cba")
    assert not example_secure_vault.is_locked


def test_secure_vault_raises_runtime_error_when_unlocked_when_already_unlocked(example_secure_vault):
    example_secure_vault.unlock("cba")
    pytest.raises(RuntimeError, lambda: example_secure_vault.unlock("cba"))


@patch('random.randint')
def test_secure_vault_raises_permission_error_when_there_are_3_attempts_and_vault_has_security(
        mock_random_randint, example_secure_vault):
    mock_random_randint.return_value = 1
    for _ in range(2):
        example_secure_vault.unlock("123")
    pytest.raises(PermissionError, lambda: example_secure_vault.unlock("123"))


@patch('random.randint')
def test_secure_vault_raises_permission_error_when_there_are_3_attempts_and_vault_doesnt_have_security(
        mock_random_randint, example_secure_vault):
    mock_random_randint.return_value = 4
    for _ in range(2):
        example_secure_vault.unlock("123")
    pytest.raises(PermissionError, lambda: example_secure_vault.unlock("123"))


def test_secure_vault_locks_successfully(example_secure_vault):
    example_secure_vault.unlock("cba")
    example_secure_vault.lock()
    assert example_secure_vault.is_locked


def test_deposit_to_vault_raises_runtime_error_when_vault_is_locked(example_secure_vault):
    pytest.raises(RuntimeError, lambda: example_secure_vault.deposit(100))


def test_deposit_negative_amount_raises_value_error(example_secure_vault):
    example_secure_vault.unlock("cba")
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
    assert example_secure_vault.balance == amount

def test_withdraw_when_locked_raises_runtime_error(example_secure_vault):
    pytest.raises(RuntimeError, lambda: example_secure_vault.withdraw(100))

def test_withdraw_amount_above_balance_raises_value_error(example_secure_vault):
    example_secure_vault.unlock("cba")
    example_secure_vault.deposit(10)
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
    example_secure_vault.deposit(500)

    example_secure_vault.withdraw(amount)
    assert example_secure_vault.balance == (500 - amount)