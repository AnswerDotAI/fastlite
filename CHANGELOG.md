# Release notes

<!-- do not remove -->

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

