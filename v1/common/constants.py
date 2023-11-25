from enum import Enum


class UserRole(Enum):
    ADMIN = "Administrator"
    MODERATOR = "Moderator"
    TEACHER = "Teacher"
    STUDENT = "Student"
    GUEST = "Guest"

    def __str__(self):
        return self.value
