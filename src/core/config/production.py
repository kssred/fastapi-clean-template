from typing import Literal, Optional

from src.core.config.base import EmailSettings, LogSettings


class EmailSettingsProd(EmailSettings):
    BACKEND: Optional[str] = "src.service.mail.emails.backend.EmailSMTPBackend"
    USE_TLS: Optional[bool] = True


class LogSettingsProd(LogSettings):
    LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "ERROR"
