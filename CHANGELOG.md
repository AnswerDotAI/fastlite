# Release notes

<!-- do not remove -->

## 0.0.14

### New Features

- sqlite3 => apsw ([#47](https://github.com/AnswerDotAI/fastlite/pull/47)), thanks to [@pydanny](https://github.com/pydanny)
  - https://github.com/AnswerDotAI/apswutils/pull/1

- Use new `sqlite_minutils.Table.result` attribute ([#45](https://github.com/AnswerDotAI/fastlite/pull/45)), thanks to [@pydanny](https://github.com/pydanny)
  - > [!WARNING]  
> This pull request is dependent on https://github.com/AnswerDotAI/sqlite-minutils/pull/42.

Functions modified minimally to use the new `sqlite_minutils.Table.result` attribute:

- [x] `Table.insert`
- [x] `Table.update`
- [x] `Table.upsert`

## Tests verified to pass

- [x] All fastlite tests and notebooks
- [x] Fasthtml notebooks and adv_app
- [x] Internal application tests

- Make get_last defensive ([#39](https://github.com/AnswerDotAI/fastlite/pull/39)), thanks to [@pydanny](https://github.com/pydanny)

- Rewrite insert() function to take advantage of RETURNING data ([#37](https://github.com/AnswerDotAI/fastlite/pull/37)), thanks to [@pydanny](https://github.com/pydanny)
  - 1. Rewrites the `fastlite.insert()` method to take advantage of sqlite-minutil's incoming ability to return data on writes via the `RETURNING *` suffix to `INSERT`, `UPDATE`, and `INSERT` actions
2. Converts kw.py to use nbdev.
3. Dependency on https://github.com/AnswerDotAI/sqlite-minutils/pull/28, will fail unless running that code

## Background

Sqlite-minutils was designed as a CLI tool in to be written to by a  single user often loading large sets of data periodically. Write actions are written for large imports, not individual actions, resulting in extra layers of abstraction for smaller actions which piggyback off the large imports.

In comparison fastlite is designed for web environments with:

1. Frequent writes of small bits of data
4. Multiple users

This PR therefore moves most of the logic for the patched version `insert` from sqlite-minutils to fastlite itself. While it does so, it also leverages utility functions from sqlite-minutils including `fix_square_braces` and `build_insert_queries_and_params`.

This PR takes care to preserve the `.last_pk` prefix.

## Dependency

1. https://github.com/AnswerDotAI/sqlite-minutils/pull/28

### Bugs Squashed

- Table.insert() with Falsy value generates an error ([#42](https://github.com/AnswerDotAI/fastlite/issues/42))
  - While [writing tests for inserts](https://github.com/AnswerDotAI/fastlite/pull/41), we discovered `Table.insert()` when supplied with a Falsy value generates an error because the sqlite-minutils `insert` method expects a record. Not the empty dict provided when a Falsy value is provided as the record. See https://github.com/AnswerDotAI/fastlite/blob/23993b133c843ae5ada63e5a72bfd22bd822301d/fastlite/kw.py#L175

@audreyfeldroy and I think it should return an empty `dict` 

```python
if not record: return {}
```

Possibly even a None object:

```python
if not record: None
```

Or maybe raise an error.

```python
if not record: raise InvalidRecordType
```


## 0.0.13

### New Features

- Add `xtra` param to all methods that use `xtra` instance var ([#34](https://github.com/AnswerDotAI/fastlite/issues/34))


## 0.0.12

### Breaking Changes

- Bump sqlite-minutils dependency to use sqlite transactions

### New Features

- add enum support ([#32](https://github.com/AnswerDotAI/fastlite/pull/32)), thanks to [@hamelsmu](https://github.com/hamelsmu)


## 0.0.11

### New Features

- add `import_file` ([#24](https://github.com/AnswerDotAI/fastlite/issues/24))


## 0.0.10

### New Features

- add markdown to doc output ([#22](https://github.com/AnswerDotAI/fastlite/issues/22))
- Use fastcore asdict instead of dataclasses asdict ([#17](https://github.com/AnswerDotAI/fastlite/pull/17)), thanks to [@pydanny](https://github.com/pydanny)

### Bugs Squashed

- Fix `__contains__` on tuple pk searches ([#20](https://github.com/AnswerDotAI/fastlite/pull/20)), thanks to [@pydanny](https://github.com/pydanny)
- Compound primary keys fail on `__contains__` when done with tuple ([#19](https://github.com/AnswerDotAI/fastlite/issues/19))


## 0.0.9

### New Features

- sqlite-minutil 3.37 compatibility


## 0.0.8

### New Features

- Use flexiclass ([#16](https://github.com/AnswerDotAI/fastlite/issues/16))
- Add `select` param ([#15](https://github.com/AnswerDotAI/fastlite/issues/15))


## 0.0.7

### New Features

- `Database.create` for creating a table from a class ([#12](https://github.com/AnswerDotAI/fastlite/issues/12))


## 0.0.6


### Bugs Squashed

- Fix `None` checks in fastlite.kw ([#11](https://github.com/AnswerDotAI/fastlite/issues/11))


## 0.0.5

### New Features

- Switch to sqlite-minutils ([#10](https://github.com/AnswerDotAI/fastlite/issues/10))


## 0.0.4

### New Features

- Filter table callable using `xtra` ([#9](https://github.com/AnswerDotAI/fastlite/issues/9))


## 0.0.3

### New Features

- Add `ids_and_rows_where` and use it to work around sqlite-utils rowid bug ([#6](https://github.com/AnswerDotAI/fastlite/issues/6))
- Add `get_last` and use it to set `last_pk` correctly and return updated row ([#5](https://github.com/AnswerDotAI/fastlite/issues/5))


## 0.0.2

### New Features

- `xtra` field support
- Auto-get pks for `update`, and return updated record ([#4](https://github.com/AnswerDotAI/fastlite/issues/4))
- Return updated value on insert/upsert ([#3](https://github.com/AnswerDotAI/fastlite/issues/3))


## 0.0.1

- Initial release

