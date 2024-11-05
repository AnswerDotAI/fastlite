__all__ = ['opt_bool', 'database']

from dataclasses import MISSING
from typing import Any,Union,Tuple,List,Iterable
from fastcore.utils import *
from sqlite_minutils.db import Database,Table,DEFAULT,ForeignKeysType,Default,Queryable,NotFoundError,fix_square_braces,SQLITE_MAX_VARS
from enum import Enum

opt_bool = Union[bool, Default, None]

def database(path, wal=True)->Any:
    path = Path(path)
    path.parent.mkdir(exist_ok=True)
    db = Database(path)
    if wal: db.enable_wal()
    return db

@patch
def xtra(self:Table, **kwargs):
    "Set `xtra_id`"
    self.xtra_id = kwargs

@patch
def get_last(self:Table, as_cls:bool=True):
    assert self.last_rowid is not None
    row = first(self.rows_where('_rowid_=?', (self.last_rowid,)))
    assert row, f"Couldn't find {self.last_rowid}"
    vals = [row[pk] for pk in self.pks]
    self.last_pk = vals[0] if len(vals)==1 else vals
    if as_cls and hasattr(self,'cls'): row = self.cls(**row)
    return row

@patch
def ids_and_rows_where(
    self:Table,
    where: Optional[str] = None, # SQL where fragment to use, for example ``id > ?``
    where_args: Optional[Union[Iterable, dict]] = None, # Parameters to use with that fragment
    order_by: Optional[str] = None, # Column or fragment of SQL to order by
    limit: Optional[int] = None, # Number of rows to limit to
    offset: Optional[int] = None, # SQL offset
    select: str = '*', # Comma-separated list of columns to select - defaults to ``*``
) -> Generator[Tuple[Any, Dict], None, None]:
    "Like `.rows_where()` but returns `(rowid, row)` pairs."
    #cs = [c.name for c in self.columns]
    #select = ",".join("[{}]".format(c) for c in cs)
    select = "_rowid_ as __rid, " + select
    for row in self.rows_where(select=select, where=where, where_args=where_args, order_by=order_by, limit=limit, offset=offset):
        yield row.pop('__rid'), row

@patch
def get(self:Table, pk_values: list|tuple|str|int, as_cls:bool=True, xtra:dict|None=None)->Any:
    if not isinstance(pk_values, (list, tuple)): pk_values = [pk_values]
    last_pk = pk_values[0] if len(self.pks) == 1 else pk_values
    if not xtra: xtra = getattr(self, 'xtra_id', {})
    vals = list(pk_values) + list(xtra.values())
    pks = self.pks + list(xtra.keys())
    if len(pks)!=len(vals): raise NotFoundError(f"Need {len(pks)} pk")
    wheres = ["[{}] = ?".format(pk_name) for pk_name in pks]
    item = first(self.ids_and_rows_where(" and ".join(wheres), vals))
    if not item: raise NotFoundError
    rid,row = item
    self.last_pk,self.last_rowid = last_pk,rid
    if as_cls and hasattr(self,'cls'): row = self.cls(**row)
    return row

@patch
def __getitem__(self:Table, pk_values): return self.get(pk_values)

@patch
def create(
    self:Table,
    columns: Dict[str, Any]=None, pk: Any=None, foreign_keys=None,
    column_order: List[str]|None=None, not_null: Iterable[str]|None=None, defaults: Dict[str, Any]|None=None,
    hash_id: str|None=None, hash_id_columns: Iterable[str]|None=None,
    extracts: Union[Dict[str, str], List[str], NoneType]=None,
    if_not_exists: bool = False, replace: bool = False, ignore: bool = False,
    transform: bool = False, strict: bool = False,
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
    types: dict|None=None, rename: dict|None=None, drop: Iterable|None=None, pk: Any|None=DEFAULT,
    not_null: Iterable[str]|None=None, defaults: Dict[str, Any]|None=None,
    drop_foreign_keys: Iterable[str]|None=None, add_foreign_keys: ForeignKeysType|None=None,
    foreign_keys: ForeignKeysType|None=None,
    column_order: List[str]|None=None, keep_table: str|None=None,
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
    types: dict|None=None, rename: dict|None=None, drop: Iterable|None=None, pk: Any|None=DEFAULT,
    not_null: Iterable[str]|None=None, defaults: Dict[str, Any]|None=None,
    drop_foreign_keys: Iterable[str]|None=None, add_foreign_keys: ForeignKeysType|None=None,
    foreign_keys: ForeignKeysType|None=None,
    column_order: List[str]|None=None, keep_table: str|None=None,
    **kwargs) -> List[str]:
    if not types: types={}
    types = {**types, **kwargs}
    return self._orig_transform_sql(
            types=types, rename=rename, drop=drop, pk=pk, not_null=not_null, defaults=defaults,
            drop_foreign_keys=drop_foreign_keys, add_foreign_keys=add_foreign_keys, foreign_keys=foreign_keys,
            column_order=column_order, keep_table=keep_table)

@patch
def transform_sql(
    self:Table, *,
    types: dict|None=None, rename: dict|None=None, drop: Iterable|None=None, pk: Any|None=DEFAULT,
    not_null: Iterable[str]|None=None, defaults: Dict[str, Any]|None=None,
    drop_foreign_keys: Iterable[str]|None=None, add_foreign_keys: ForeignKeysType|None=None,
    foreign_keys: ForeignKeysType|None=None,
    column_order: List[str]|None=None, keep_table: str|None=None,
    **kwargs) -> List[str]:
    if not types: types={}
    types = {**types, **kwargs}
    return self._orig_transform_sql(
            types=types, rename=rename, drop=drop, pk=pk, not_null=not_null, defaults=defaults,
            drop_foreign_keys=drop_foreign_keys, add_foreign_keys=add_foreign_keys, foreign_keys=foreign_keys,
            column_order=column_order, keep_table=keep_table)

def _process_row(row): return {k:(v.value if isinstance(v, Enum) else v) for k,v in asdict(row).items() if v is not UNSET}

@patch
def update(self:Table, updates: dict|None=None, pk_values: list|tuple|str|int|float|None=None,
           alter: bool=False, conversions: dict|None=None, xtra:dict|None=None, **kwargs):
    if not updates: updates={}
    updates = _process_row(updates)
    if not xtra: xtra = getattr(self, 'xtra_id', {})
    updates = {**updates, **kwargs, **xtra}
    if pk_values is None: pk_values = [updates[o] for o in self.pks]
    self._orig_update(pk_values, updates=updates, alter=alter, conversions=conversions)
    return self.get_last()

@patch
def insert_all(
    self:Table,
    records: Dict[str, Any]=None, pk=DEFAULT, foreign_keys=DEFAULT,
    column_order: Union[List[str], Default, None]=DEFAULT,
    not_null: Union[Iterable[str], Default, None]=DEFAULT,
    defaults: Union[Dict[str, Any], Default, None]=DEFAULT,
    batch_size=DEFAULT,
    hash_id: Union[str, Default, None]=DEFAULT,
    hash_id_columns: Union[Iterable[str], Default, None]=DEFAULT,
    alter: opt_bool=DEFAULT, ignore: opt_bool=DEFAULT, replace: opt_bool=DEFAULT, truncate=False,
    extracts: Union[Dict[str, str], List[str], Default, None]=DEFAULT,
    conversions: Union[Dict[str, str], Default, None]=DEFAULT,
    columns: Union[Dict[str, Any], Default, None]=DEFAULT,
    strict: opt_bool=DEFAULT,
    upsert:bool=False, analyze:bool=False, xtra:dict|None=None,
    **kwargs) -> Table:
    if not xtra: xtra = getattr(self,'xtra_id',{})
    records = [_process_row(o) for o in records]
    records = [{**o, **xtra} for o in records]
    return self._orig_insert_all(
        records=records, pk=pk, foreign_keys=foreign_keys, column_order=column_order, not_null=not_null,
        defaults=defaults, batch_size=batch_size, hash_id=hash_id, hash_id_columns=hash_id_columns, alter=alter,
        ignore=ignore, replace=replace, truncate=truncate, extracts=extracts, conversions=conversions,
        columns=columns, strict=strict, upsert=upsert, analyze=analyze)

@patch
def insert(
    self:Table,
    record: Dict[str, Any]=None, pk=DEFAULT, foreign_keys=DEFAULT,
    column_order: Union[List[str], Default, None]=DEFAULT,
    not_null: Union[Iterable[str], Default, None]=DEFAULT,
    defaults: Union[Dict[str, Any], Default, None]=DEFAULT,
    hash_id: Union[str, Default, None]=DEFAULT,
    hash_id_columns: Union[Iterable[str], Default, None]=DEFAULT,
    alter: opt_bool=DEFAULT,
    ignore: opt_bool=DEFAULT,
    replace: opt_bool=DEFAULT,
    extracts: Union[Dict[str, str], List[str], Default, None]=DEFAULT,
    conversions: Union[Dict[str, str], Default, None]=DEFAULT,
    columns: Union[Dict[str, Any], Default, None]=DEFAULT,
    upsert=False,
    analyze=False,
    strict: opt_bool=DEFAULT,
    **kwargs
):
    """

    Use ``analyze=True`` to run ``ANALYZE`` after the insert has completed.
    """
    if not record: record={}
    record = _process_row(record)
    record = {**record, **kwargs}    
    
    pk = self.value_or_default("pk", pk)
    foreign_keys = self.value_or_default("foreign_keys", foreign_keys)
    column_order = self.value_or_default("column_order", column_order)
    not_null = self.value_or_default("not_null", not_null)
    defaults = self.value_or_default("defaults", defaults)
    hash_id = self.value_or_default("hash_id", hash_id)
    hash_id_columns = self.value_or_default("hash_id_columns", hash_id_columns)
    alter = self.value_or_default("alter", alter)
    ignore = self.value_or_default("ignore", ignore)
    replace = self.value_or_default("replace", replace)
    extracts = self.value_or_default("extracts", extracts)
    conversions = self.value_or_default("conversions", conversions) or {}
    columns = self.value_or_default("columns", columns)
    strict = self.value_or_default("strict", strict)

    if hash_id_columns and hash_id is None:
        hash_id = "id"

    if upsert and (not pk and not hash_id):
        raise PrimaryKeyRequired("upsert() requires a pk")
    assert not (hash_id and pk), "Use either pk= or hash_id="
    if hash_id_columns and (hash_id is None):
        hash_id = "id"
    if hash_id:
        pk = hash_id

    assert not (
        ignore and replace
    ), "Use either ignore=True or replace=True, not both"
    # Fix up any records with square braces in the column names
    records = list(fix_square_braces([record]))[0]
    num_columns = len(record.keys())
    assert (
        num_columns <= SQLITE_MAX_VARS
    ), "Rows can have a maximum of {} columns".format(SQLITE_MAX_VARS)
    self.last_rowid = None
    self.last_pk = None
    if not self.exists():
        column_types = suggest_column_types(record)
        column_types.update(columns or {})
        self.create(
            column_types,
            pk,
            foreign_keys,
            column_order=column_order,
            not_null=not_null,
            defaults=defaults,
            hash_id=hash_id,
            hash_id_columns=hash_id_columns,
            extracts=extracts,
            strict=strict,
        )
    all_columns_set = set(record.keys())
    all_columns = list(sorted(all_columns_set))
    if hash_id:
        all_columns.insert(0, hash_id)
        
    queries_and_params = self.build_insert_queries_and_params(
        extracts,
        [record],
        all_columns,
        hash_id,
        hash_id_columns,
        upsert,
        pk,
        not_null,
        conversions,
        1, # num_records_processed
        replace,
        ignore,
    )

    # Build the query
    query, params = first(queries_and_params)
    # Execute and transform into a dict called 'row'
    cursor = self.db.execute(query, tuple(params))
    columns = [c[0] for c in cursor.description]
    row = dict(zip(columns, cursor.fetchone())) 

    # Preserve old self.last_pk functionality
    if (hash_id or pk) and not upsert:
        if hash_id:
            self.last_pk = row[hash_id]
        elif isinstance(pk, str):
            self.last_pk = row[pk]
        else:
            self.last_pk = tuple(row[p] for p in pk)
    self.last_rowid = self.last_pk

    if analyze:
        self.analyze()
        
    if hasattr(self,'cls'): row = self.cls(**row)
    return row

@patch
def upsert(
    self:Table,
    record:Any=None, pk=DEFAULT, foreign_keys=DEFAULT,
    column_order: Union[List[str], Default, None]=DEFAULT,
    not_null: Union[Iterable[str], Default, None]=DEFAULT,
    defaults: Union[Dict[str, Any], Default, None]=DEFAULT,
    hash_id: Union[str, Default]|None=DEFAULT,
    hash_id_columns: Union[Iterable[str], Default, None]=DEFAULT,
    alter: Union[bool, Default]|None=DEFAULT,
    extracts: Union[Dict[str, str], List[str], Default, None]=DEFAULT,
    conversions: Union[Dict[str, str], Default, None]=DEFAULT,
    columns: Union[Dict[str, Any], Default, None]=DEFAULT,
    strict: Union[bool, Default]|None=DEFAULT,
    **kwargs) -> Table:
    if pk==DEFAULT:
        assert len(self.pks)==1
        pk = self.pks[0]
    if not record: record={}
    record = _process_row(record)
    record = {**record, **kwargs}
    last_pk = record[pk]
    self._orig_upsert(
        record=record, pk=pk, foreign_keys=foreign_keys, column_order=column_order, not_null=not_null,
        defaults=defaults, hash_id=hash_id, hash_id_columns=hash_id_columns, alter=alter,
        extracts=extracts, conversions=conversions, columns=columns, strict=strict)
    return self.get(last_pk)

@patch
def lookup(
    self:Table,
    lookup_values: Dict[str, Any],
    extra_values: Dict[str, Any]|None=None,
    pk: str|None = "id",
    foreign_keys: ForeignKeysType|None=None,
    column_order: List[str]|None=None,
    not_null: Iterable[str]|None=None,
    defaults: Dict[str, Any]|None=None,
    extracts: Union[Dict[str, str], List[str], None]=None,
    conversions: Dict[str, str]|None=None,
    columns: Dict[str, Any]|None=None,
    strict: bool|None = False,
    **kwargs):
    if not lookup_values: lookup_values={}
    lookup_values = {**lookup_values, **kwargs}
    return self._orig_lookup(
        lookup_values=lookup_values, extra_values=extra_values, pk=pk, foreign_keys=foreign_keys,
        column_order=column_order, not_null=not_null, defaults=defaults, extracts=extracts,
        conversions=conversions, columns=columns, strict=strict)
