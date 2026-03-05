from typing import Any

from fast_api.utils.status import Status


class ResponseProvider:
    STATUS = "status"
    REASON = "reason"

    def create_successful_response(self, **kwargs) -> dict[str, Any]:
        return {
            self.STATUS: Status.SUCCESS.value,
            **kwargs
        }

    def create_failure_response(self, message: str) -> dict[str, Any]:
        return {
            self.STATUS: Status.FAILED.value,
            self.REASON: message
        }
