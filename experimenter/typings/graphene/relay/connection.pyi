"""
This type stub file was generated by pyright.
"""

from ..types.field import Field
from ..types.objecttype import ObjectType, ObjectTypeOptions

class PageInfo(ObjectType):
    class Meta:
        description = ...

    has_next_page = ...
    has_previous_page = ...
    start_cursor = ...
    end_cursor = ...

class ConnectionOptions(ObjectTypeOptions):
    node = ...

class Connection(ObjectType):
    class Meta:
        abstract = ...

    @classmethod
    def __init_subclass_with_meta__(cls, node=..., name=..., **options):  # -> None:
        class EdgeBase: ...
        class EdgeMeta: ...

class IterableConnectionField(Field):
    def __init__(self, type, *args, **kwargs) -> None: ...
    @property
    def type(self): ...
    @classmethod
    def resolve_connection(cls, connection_type, args, resolved): ...
    @classmethod
    def connection_resolver(cls, resolver, connection_type, root, info, **args): ...
    def get_resolver(self, parent_resolver): ...

ConnectionField = IterableConnectionField
