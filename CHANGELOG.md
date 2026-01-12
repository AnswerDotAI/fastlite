# Release notes

<!-- do not remove -->

## 0.2.4

### Bugs Squashed

- Fix KeyError in insert when ignore=True and duplicate key exists ([#78](https://github.com/AnswerDotAI/fastlite/pull/78)), thanks to [@dienhoa](https://github.com/dienhoa)


## 0.2.3

### Bugs Squashed

- Use UNSET for default values ([#75](https://github.com/AnswerDotAI/fastlite/issues/75))


## 0.2.2

### New Features

- Add `__all__` to fastlite.kw ([#74](https://github.com/AnswerDotAI/fastlite/issues/74))
- Allow `flags` to modify SQLite connection ([#73](https://github.com/AnswerDotAI/fastlite/pull/73)), thanks to [@gautam-e](https://github.com/gautam-e)


## 0.2.1

### New Features

- Auto handle UNSET values in update kwargs ([#71](https://github.com/AnswerDotAI/fastlite/issues/71))


## 0.2.0

### Breaking Changes

- `fetchone` renamed to `selectone`, and now raises exception for non-unique return

### New Features

- Check for multi row return in `selectone` ([#70](https://github.com/AnswerDotAI/fastlite/issues/70))


## 0.1.4


### Bugs Squashed

- upsert method doesn't support composite primary keys ([#69](https://github.com/AnswerDotAI/fastlite/issues/69))


## 0.1.3

### New Features

- Add `link_dcs` and have `create_mod` output `__all__` ([#64](https://github.com/AnswerDotAI/fastlite/issues/64))


## 0.1.2

### New Features

- Add optional default value for `get` ([#55](https://github.com/AnswerDotAI/fastlite/pull/55)), thanks to [@tom-pollak](https://github.com/tom-pollak)
- Add table iter; Add `set_classes` and `get_tables` ([#51](https://github.com/AnswerDotAI/fastlite/issues/51))
- Add `table.fetchone` ([#50](https://github.com/AnswerDotAI/fastlite/issues/50))


## 0.1.1

### Breaking Changes

- fastlite has been rewritten to now use apsw instead of sqlite3 ([#47](https://github.com/AnswerDotAI/fastlite/pull/47)), thanks to [@pydanny](https://github.com/pydanny)
  - The key driver of this is that we found major concurrency and performance regressions in the python 3.12 sqlite3 module. However, there are many other good reasons also to switch to apsw. The python stdlib sqlite3 module is designed to focus on compatibility with the Python DB API, where apsw is designed to focus on compatibility with sqlite itself. We have found in production applications that with apsw's design it is far easier to get good performance and reliability compared to the stdlib module.

### New Features

- Use new `sqlite_minutils.Table.result` attribute ([#45](https://github.com/AnswerDotAI/fastlite/pull/45)), thanks to [@pydanny](https://github.com/pydanny)
- Make `get_last` defensive ([#39](https://github.com/AnswerDotAI/fastlite/pull/39)), thanks to [@pydanny](https://github.com/pydanny)
- Rewrite insert() function to take advantage of RETURNING data ([#37](https://github.com/AnswerDotAI/fastlite/pull/37)), thanks to [@pydanny](https://github.com/pydanny)

### Bugs Squashed

- Table.insert() with Falsy value generates an error ([#42](https://github.com/AnswerDotAI/fastlite/issues/42))


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

