from uuid import UUID
from src.core.types import ID
from src.core.types.user import UserProtocol
from src.models.user import UserModel
from src.utils.repository import SQLAlchemyRepository
from src.utils.repository.base import RepositoryABC


class IUserRepository(RepositoryABC[UserProtocol, ID]):
    pass


class UserRepository(IUserRepository[UUID], SQLAlchemyRepository[UserProtocol, UUID]):
    model = UserModel
