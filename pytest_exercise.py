import abc
import random


# Create a tests folder, containing tests for this file
# Make sure to test the SecretValue usage and the SimpleHasher as separated things (as well as together)
# Use fixtures, parametrization, mocking, patching and pytest functions (for example, pytest.assert_raised)
# Instead of using mocking and patching inside the method, try to use them with decorators, and try to use both together in some of the tests
# Use fixtures instead of creating SimpleHasher and SecureVault each test
# Use mocking instead of creating SimpleHasher when it's redundant to the test
# Use parametrization to test different parameters to the same test (different amounts to withdraw, for example)

# Generally, the tests you create should make sure that nothing is changed in the logic of thsi class without breaking one of the tests:
# Errors are raised correctly (for example, someone removes one of the error raises - at least one of your tests should fail)
# Core logic is correct - deposit and withdraw work as expected
# Security intervenes when necessary (use patching to test that)
# Whatever else you consider important

class SecretHasher(abc.ABC):
    @abc.abstractmethod
    def hash_pin(self, pin: str) -> str:
        pass


class SimpleHasher(SecretHasher):
    def hash_pin(self, pin: str) -> str:
        return f"hash_{pin[::-1]}"


class SecurityGuardError(Exception):
    pass

class FailedUnlockAttemptError(Exception):
    pass

class VaultAlreadyUnlockedError(Exception):
    pass

class VaultLockedError(Exception):
    pass

class NegativeInitialBalanceError(Exception):
    pass

class NegativeDepositAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class SecureVault:
    def __init__(self, initial_balance: float, hasher: SecretHasher, correct_hash: str):
        if initial_balance < 0:
            raise NegativeInitialBalanceError()
        self._balance = initial_balance
        self._hasher = hasher
        self._correct_hash = correct_hash
        self._is_locked = True
        self._failed_attempts = 0

    def unlock(self, pin: str) -> None:
        if self._is_locked:
            if self._hasher.hash_pin(pin) == self._correct_hash:
                self._is_locked = False
                self._failed_attempts = 0
            else:
                self._failed_attempts += 1
                if self._failed_attempts >= 3:
                    if self.has_security():
                        raise SecurityGuardError()
                    raise FailedUnlockAttemptError()
        else:
            raise VaultAlreadyUnlockedError()

    def lock(self) -> None:
        self._is_locked = True

    def deposit(self, amount: float) -> float:
        if self._is_locked:
            raise VaultLockedError()
        if amount <= 0:
            raise NegativeDepositAmountError()
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if self._is_locked:
            raise VaultLockedError()
        if amount > self._balance:
            raise InsufficientBalanceError()

        self._balance -= amount
        return self._balance

    def has_security(self) -> bool:
        roll = random.randint(1, 5)
        if roll > 3:
            return True
        return False

    @property
    def is_locked(self) -> bool:
        return self._is_locked

    @property
    def balance(self) -> bool:
        return self._balance