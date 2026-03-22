from unittest.mock import MagicMock, patch

import pytest

from pytest_exercise import SimpleHasher, SecureVault, SecurityGuardError, InsufficientBalanceError, VaultLockedError, \
    FailedUnlockAttemptError, NegativeInitialBalanceError, VaultAlreadyUnlockedError, NegativeDepositAmountError


@pytest.fixture
def secure_vault() -> SecureVault:
    return SecureVault(0, SimpleHasher(), "hash_abc")


@pytest.fixture
def unlocked_secure_vault() -> SecureVault:
    vault = SecureVault(0, SimpleHasher(), "hash_abc")
    vault.unlock("cba")
    return vault


@pytest.mark.parametrize("pin_number", [
    "123",
    "456",
    "789"
])
def test__simple_hasher__returns_inverted_pin_number(pin_number):
    # Arrange
    simple_hasher = SimpleHasher()
    # Act + Assert
    assert simple_hasher.hash_pin(pin_number) == f"hash_{pin_number[::-1]}"


@pytest.mark.parametrize("negative_balance", [
    -1,
    -5,
    -100
    - 1000
])
def test__initializing_secure_value_with_negative_value__raises_value_error(negative_balance):
    # Arrange
    secret_hasher_mock = MagicMock()

    # Act + Assert
    with pytest.raises(NegativeInitialBalanceError):
        SecureVault(negative_balance, secret_hasher_mock, "xyz")


def test__secure_vault__unlocks_successfully(secure_vault):
    # Act
    secure_vault.unlock("cba")
    # Assert
    assert not secure_vault.is_locked


def test__secure_vault__raises_exception_when_unlocked_while_already_unlocked(secure_vault):
    # Arrange
    secure_vault.unlock("cba")
    # Act + Assert
    with pytest.raises(VaultAlreadyUnlockedError):
        secure_vault.unlock("cba")


def test__secure_vault__raises_exception_when_running_out_of_unlock_attempts_and_vault_has_security(secure_vault):
    # Arrange
    secure_vault.has_security = MagicMock(return_value=True)
    for _ in range(2):
        secure_vault.unlock("123")
    # Act + Assert
    with pytest.raises(SecurityGuardError):
        secure_vault.unlock("123")


def test__secure_vault__raises_exception_when_running_out_of_unlock_attempts_and_vault_doesnt_have_security(
        secure_vault):
    # Arrange
    secure_vault.has_security = MagicMock(return_value=False)
    for _ in range(2):
        secure_vault.unlock("123")
    # Act + Assert
    with pytest.raises(FailedUnlockAttemptError):
        secure_vault.unlock("123")


def test__secure_vault__locks_successfully(unlocked_secure_vault):
    # Act
    unlocked_secure_vault.lock()
    # Assert
    assert unlocked_secure_vault.is_locked


def test__deposit_to_vault__raises_exception_when_vault_is_locked(secure_vault):
    # Act + Assert
    with pytest.raises(VaultLockedError):
        secure_vault.deposit(100)


def test__deposit_negative_amount__raises_exception(unlocked_secure_vault):
    # Act + Assert
    with pytest.raises(NegativeDepositAmountError):
        unlocked_secure_vault.deposit(-100)


@pytest.mark.parametrize("amount", [
    5,
    10,
    20,
    100,
    200
])
def test__deposit_amount__updates_balance(amount, unlocked_secure_vault):
    # Act
    unlocked_secure_vault.deposit(amount)
    # Assert
    assert unlocked_secure_vault.balance == amount


@pytest.mark.parametrize("amount", [
    5,
    10,
    20,
    100,
    200
])
def test__deposit_method__returns_updated_balance(amount, unlocked_secure_vault):
    # Act + Assert
    assert unlocked_secure_vault.deposit(amount) == amount


def test__withdraw_while_locked__raises_runtime_error(secure_vault):
    # Act + Assert
    with pytest.raises(VaultLockedError):
        secure_vault.withdraw(100)


@pytest.mark.parametrize("deposit_amount, withdraw_amount", [
    (10, 100),
    (20, 30),
    (1, 2),
    (100, 1000)
])
def test__withdraw_amount_above_balance__raises_exception(deposit_amount, withdraw_amount, unlocked_secure_vault):
    # Act
    unlocked_secure_vault.deposit(deposit_amount)
    # Assert
    with pytest.raises(InsufficientBalanceError):
        unlocked_secure_vault.withdraw(withdraw_amount)


@pytest.mark.parametrize("deposit_amount, withdraw_amount", [
    (500, 100),
    (200, 100),
    (2, 1),
    (1000, 500)
])
def test__withdraw_method__updates_balance(deposit_amount, withdraw_amount, unlocked_secure_vault):
    # Act
    unlocked_secure_vault.deposit(deposit_amount)
    unlocked_secure_vault.withdraw(withdraw_amount)
    # Assert
    assert unlocked_secure_vault.balance == (deposit_amount - withdraw_amount)


@pytest.mark.parametrize("deposit_amount, withdraw_amount", [
    (500, 100),
    (200, 100),
    (2, 1),
    (1000, 500)
])
def test__withdraw_method_returns_updated_balance(deposit_amount, withdraw_amount, unlocked_secure_vault):
    # Act
    unlocked_secure_vault.deposit(deposit_amount)
    # Assert
    assert unlocked_secure_vault.withdraw(withdraw_amount) == (deposit_amount - withdraw_amount)


@pytest.mark.parametrize("roll", [4, 5])
@patch('random.randint')
def test__has_security__return_true(mock_random_randint, secure_vault, roll):
    # Arrange
    mock_random_randint.return_value = roll
    # Act + Assert
    assert secure_vault.has_security()


@pytest.mark.parametrize("roll", [1, 2, 3])
@patch('random.randint')
def test__has_security__return_false(mock_random_randint, secure_vault, roll):
    # Arrange
    mock_random_randint.return_value = roll
    # Act + Assert
    assert not secure_vault.has_security()
