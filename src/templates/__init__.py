from enum import StrEnum


class EmailTemplatePath(StrEnum):
    PASSWORD_RESET_TXT = "email/password_reset.txt"
    EMAIL_CONFIRM_TXT = "email/email_confirm.txt"
