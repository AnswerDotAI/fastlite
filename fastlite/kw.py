from dataclasses import is_dataclass, MISSING, asdict
from typing import Any,Union,Tuple,List,Iterable
from fastcore.utils import *
import sqlite_utils
from sqlite_utils import Database
from sqlite_utils.db import Table,DEFAULT,ForeignKeysType,Default,Queryable


@patch
def create(
    self:Table,
    columns: Dict[str, Any]=None,
    pk: Optional[Any] = None,
    foreign_keys: Union[Iterable[Union[str, sqlite_utils.db.ForeignKey, Tuple[str, str], Tuple[str, str, str], Tuple[str, str, str, str]]], List[Union[str, sqlite_utils.db.ForeignKey, Tuple[str, str], Tuple[str, str, str], Tuple[str, str, str, str]]], NoneType] = None,
    column_order: Optional[List[str]] = None,
    not_null: Optional[Iterable[str]] = None,
    defaults: Optional[Dict[str, Any]] = None,
    hash_id: Optional[str] = None,
    hash_id_columns: Optional[Iterable[str]] = None,
    extracts: Union[Dict[str, str], List[str], NoneType] = None,
    if_not_exists: bool = False,
    replace: bool = False,
    ignore: bool = False,
    transform: bool = False,
    strict: bool = False,
    **kwargs):
    if not columns: columns={}
    columns = {**columns, **kwargs}
    return self._orig_create(
        columns, pk=pk, foreign_keys=foreign_keys, column_order=column_order, not_null=not_null,
        defaults=defaults, hash_id=hash_id, hash_id_columns=hash_id_columns, extracts=extracts,
        if_not_exists=if_not_exists, replace=replace, ignore=ignore, transform=transform, strict=strict)

@patch
def transform(
    self:Table, *,
    types: Optional[dict] = None,
    rename: Optional[dict] = None,
    drop: Optional[Iterable] = None,
    pk: Optional[Any] = DEFAULT,
    not_null: Optional[Iterable[str]] = None,
    defaults: Optional[Dict[str, Any]] = None,
    drop_foreign_keys: Optional[Iterable[str]] = None,
    add_foreign_keys: Optional[ForeignKeysType] = None,
    foreign_keys: Optional[ForeignKeysType] = None,
    column_order: Optional[List[str]] = None,
    keep_table: Optional[str] = None,
    **kwargs) -> Table:
    if not types: types={}
    types = {**types, **kwargs}
    return self._orig_transform(
            types=types, rename=rename, drop=drop, pk=pk, not_null=not_null, defaults=defaults,
            drop_foreign_keys=drop_foreign_keys, add_foreign_keys=add_foreign_keys, foreign_keys=foreign_keys,
            column_order=column_order, keep_table=keep_table)

@patch
def transform_sql(
    self:Table, *,
    types: Optional[dict] = None,
    rename: Optional[dict] = None,
    drop: Optional[Iterable] = None,
    pk: Optional[Any] = DEFAULT,
    not_null: Optional[Iterable[str]] = None,
    defaults: Optional[Dict[str, Any]] = None,
    drop_foreign_keys: Optional[Iterable[str]] = None,
    add_foreign_keys: Optional[ForeignKeysType] = None,
    foreign_keys: Optional[ForeignKeysType] = None,
    column_order: Optional[List[str]] = None,
    keep_table: Optional[str] = None,
    **kwargs) -> List[str]:
    if not types: types={}
    types = {**types, **kwargs}
    return self._orig_transform_sql(
            types=types, rename=rename, drop=drop, pk=pk, not_null=not_null, defaults=defaults,
            drop_foreign_keys=drop_foreign_keys, add_foreign_keys=add_foreign_keys, foreign_keys=foreign_keys,
            column_order=column_order, keep_table=keep_table)

@patch
def update(
    self:Table,
    pk_values: Union[list, tuple, str, int, float],
    updates: Any = None,
    alter: bool = False,
    conversions: Optional[dict] = None,
    **kwargs) -> Table:
    if not updates: updates={}
    if is_dataclass(updates): updates = asdict(updates)
    updates = {**updates, **kwargs}
    self._orig_update(pk_values=pk_values, updates=updates, alter=alter, conversions=conversions)


@patch
def insert(
    self:Table,
    record: Dict[str, Any]=None,
    pk=DEFAULT,
    foreign_keys=DEFAULT,
    column_order: Optional[Union[List[str], Default]] = DEFAULT,
    not_null: Optional[Union[Iterable[str], Default]] = DEFAULT,
    defaults: Optional[Union[Dict[str, Any], Default]] = DEFAULT,
    hash_id: Optional[Union[str, Default]] = DEFAULT,
    hash_id_columns: Optional[Union[Iterable[str], Default]] = DEFAULT,
    alter: Optional[Union[bool, Default]] = DEFAULT,
    ignore: Optional[Union[bool, Default]] = DEFAULT,
    replace: Optional[Union[bool, Default]] = DEFAULT,
    extracts: Optional[Union[Dict[str, str], List[str], Default]] = DEFAULT,
    conversions: Optional[Union[Dict[str, str], Default]] = DEFAULT,
    columns: Optional[Union[Dict[str, Any], Default]] = DEFAULT,
    strict: Optional[Union[bool, Default]] = DEFAULT,
    **kwargs) -> Table:
    if not record: record={}
    if is_dataclass(record): record = asdict(record)
    record = {**record, **kwargs}
    self._orig_insert(
        record=record, pk=pk, foreign_keys=foreign_keys, column_order=column_order, not_null=not_null,
        defaults=defaults, hash_id=hash_id, hash_id_columns=hash_id_columns, alter=alter, ignore=ignore,
        replace=replace, extracts=extracts, conversions=conversions, columns=columns, strict=strict)
    return self.get(self.last_pk)


@patch
def upsert(
    self:Table,
    record: Dict[str, Any]=None,
    pk=DEFAULT,
    foreign_keys=DEFAULT,
    column_order: Optional[Union[List[str], Default]] = DEFAULT,
    not_null: Optional[Union[Iterable[str], Default]] = DEFAULT,
    defaults: Optional[Union[Dict[str, Any], Default]] = DEFAULT,
    hash_id: Optional[Union[str, Default]] = DEFAULT,
    hash_id_columns: Optional[Union[Iterable[str], Default]] = DEFAULT,
    alter: Optional[Union[bool, Default]] = DEFAULT,
    extracts: Optional[Union[Dict[str, str], List[str], Default]] = DEFAULT,
    conversions: Optional[Union[Dict[str, str], Default]] = DEFAULT,
    columns: Optional[Union[Dict[str, Any], Default]] = DEFAULT,
    strict: Optional[Union[bool, Default]] = DEFAULT,
    **kwargs) -> Table:
    if pk==DEFAULT:
        assert len(self.pks)==1
        pk = self.pks[0]
    if not record: record={}
    if is_dataclass(record): record = asdict(record)
    record = {**record, **kwargs}
    self._orig_upsert(
        record=record, pk=pk, foreign_keys=foreign_keys, column_order=column_order, not_null=not_null,
        defaults=defaults, hash_id=hash_id, hash_id_columns=hash_id_columns, alter=alter,
        extracts=extracts, conversions=conversions, columns=columns, strict=strict)
    return self.get(self.last_pk)


@patch
def lookup(
    self:Table,
    lookup_values: Dict[str, Any],
    extra_values: Optional[Dict[str, Any]] = None,
    pk: Optional[str] = "id",
    foreign_keys: Optional[ForeignKeysType] = None,
    column_order: Optional[List[str]] = None,
    not_null: Optional[Iterable[str]] = None,
    defaults: Optional[Dict[str, Any]] = None,
    extracts: Optional[Union[Dict[str, str], List[str]]] = None,
    conversions: Optional[Dict[str, str]] = None,
    columns: Optional[Dict[str, Any]] = None,
    strict: Optional[bool] = False,
    **kwargs):
    if not lookup_values: lookup_values={}
    lookup_values = {**lookup_values, **kwargs}
    return self._orig_lookup(
        lookup_values=lookup_values, extra_values=extra_values, pk=pk, foreign_keys=foreign_keys,
        column_order=column_order, not_null=not_null, defaults=defaults, extracts=extracts,
        conversions=conversions, columns=columns, strict=strict)

