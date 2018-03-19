from injector import inject
from typing import Any, List
from uuid import UUID

from sqlutils import Repository, DataContext, create_one, create_many
from lingany_api.persistance.dto.language_dto import LanguageDTO


class LanguageRepository(Repository[LanguageDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def get_by_id(self, uid: str) -> LanguageDTO:
        data = self._context.callproc('get_language_by_id', [uid])
        return create_one(LanguageDTO, data)

    def add(self, entity: LanguageDTO) -> None:
        self._context.callproc('add_language', [entity.uid, entity.title])

    def get_all(self):
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid: Any) -> None:
        raise NotImplementedError