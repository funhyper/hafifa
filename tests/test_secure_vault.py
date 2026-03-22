from unittest.mock import MagicMock, patch

import pytest

from code.pytest_exercise import SecureVault, SimpleHasher, NegativeInitialBalanceError, VaultAlreadyUnlockedError, \
    SecurityGuardError, FailedUnlockAttemptError, VaultLockedError, NegativeDepositAmountError, InsufficientBalanceError


@pytest.fixture
def secure_vault() -> SecureVault:
    return SecureVault(0, SimpleHasher(), "hash_abc")


@pytest.fixture
def unlocked_secure_vault() -> SecureVault:
    vault = SecureVault(0, SimpleHasher(), "hash_abc")
    vault.unlock("cba")
    return vault

@pytest.mark.parametrize("negative_balance", [
    -1,
    -5,
    -100
    - 1000
])
def test__init_negative_balance__raises_value_error(negative_balance):
    # Arrange
    secret_hasher_mock = MagicMock()

    # Act + Assert
    with pytest.raises(NegativeInitialBalanceError):
        SecureVault(negative_balance, secret_hasher_mock, "xyz")

def test__unlocks__sanity(secure_vault):
    # Act
    secure_vault.unlock("cba")
    # Assert
    assert secure_vault.is_locked is False

def test__unlock_already_unlocked_vault__raises_vault_already_unlocked_exception(secure_vault):
    # Arrange
    secure_vault.unlock("cba")
    # Act + Assert
    with pytest.raises(VaultAlreadyUnlockedError):
        secure_vault.unlock("cba")


def test__running_out_of_unlock_attempts_and_having_security___raises_security_guard_error(secure_vault):
    # Arrange
    secure_vault.has_security = MagicMock(return_value=True)
    # Act
    for _ in range(2):
        secure_vault.unlock("123")
    # Assert
    with pytest.raises(SecurityGuardError):
        secure_vault.unlock("123")


def test__running_out_of_unlock_attempts_and_not_having_security___raises_failed_unlock_attempt_error(secure_vault):
    # Arrange
    secure_vault.has_security = MagicMock(return_value=False)
    # Act
    for _ in range(2):
        secure_vault.unlock("123")
    # Assert
    with pytest.raises(FailedUnlockAttemptError):
        secure_vault.unlock("123")


def test__locks__sanity(unlocked_secure_vault):
    # Act
    unlocked_secure_vault.lock()
    # Assert
    assert unlocked_secure_vault.is_locked is True


def test__deposit_to_locked_vault__raises_vault_locked_error(secure_vault):
    # Act + Assert
    with pytest.raises(VaultLockedError):
        secure_vault.deposit(100)


def test__deposit_negative_amount__raises_negative_deposit_amount_error(unlocked_secure_vault):
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


def test__withdraw_while_locked__raises_vault_locked_error(secure_vault):
    # Act + Assert
    with pytest.raises(VaultLockedError):
        secure_vault.withdraw(100)


@pytest.mark.parametrize("deposit_amount, withdraw_amount", [
    (10, 100),
    (20, 30),
    (1, 2),
    (100, 1000)
])
def test__withdraw_amount_above_balance__raises_insufficient_balance_error(deposit_amount,
withdraw_amount, unlocked_secure_vault):
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
def test__withdraw_method__returns_updated_balance(deposit_amount, withdraw_amount, unlocked_secure_vault):
    # Arrange
    unlocked_secure_vault.deposit(deposit_amount)
    # Act + Assert
    assert unlocked_secure_vault.withdraw(withdraw_amount) == (deposit_amount - withdraw_amount)


@pytest.mark.parametrize("roll", [1, 2, 3, 4, 5])
@patch('random.randint')
def test__has_security__return_true(mock_random_randint, secure_vault, roll):
    # Arrange
    mock_random_randint.return_value = roll
    # Act + Assert
    if roll > 3:
        assert secure_vault.has_security() is True
    else:
        assert secure_vault.has_security() is False

