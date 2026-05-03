import logging

class AppException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int = 500,
        error_code: str = "APP_ERROR",
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code


class ValidationException(AppException):
    def __init__(self, message="Validation failed"):
        super().__init__(message, 400, "VALIDATION_ERROR")

class DuplicateException(AppException):
    def __init__(self, message="Duplicate resource"):
        super().__init__(message, 409, "DUPLICATE")


class NotFoundException(AppException):
    def __init__(self, message="Resource not found"):
        super().__init__(message, 404, "NOT_FOUND")


class UnauthorizedException(AppException):
    def __init__(self, message="Unauthorized"):
        super().__init__(message, 401, "UNAUTHORIZED")


class ForbiddenException(AppException):
    def __init__(self, message="Forbidden"):
        super().__init__(message, 403, "FORBIDDEN")


class ConflictException(AppException):
    def __init__(self, message="Conflict occurred"):
        super().__init__(message, 409, "CONFLICT")