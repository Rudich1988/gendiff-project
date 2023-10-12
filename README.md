## Проект Вычислитель отличий.
Этот проект находит отличия между двумя файлами в форматах json, yml и yaml и выводит отличия на экран
### Минимальные требования:
- Python 3.6 и выше
- pip (версия 19 и выше)
- poetry 1.2.0 и выше
### Инструкция по установке проекта
```bash
make install
make test
make lint
make selfcheck
make check
make build
```
### Возможности проекта
- Вывод справки о возможностях пректа:
```bash
gendiff -h
```
- Вывод различий в структурированном формате json:
```bash
gendiff --format json filepath1 filepath2
```
- Вывод различий в других текстовых форматах:
```bash
gendiff filepath1 filepath2
gendiff --format plain filepath1 filepath2
```
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Rudich1988/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Rudich1988/python-project-50/actions)
[![Action Status](https://github.com/Rudich1988/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Rudich1988/python-project-50/actions/workflows/pyci.yml)

[![Test Coverage](https://api.codeclimate.com/v1/badges/0ff4cfc3f03f5c3d5154/test_coverage)](https://codeclimate.com/github/Rudich1988/python-project-50/test_coverage)

[![Maintainability](https://api.codeclimate.com/v1/badges/0ff4cfc3f03f5c3d5154/maintainability)](https://codeclimate.com/github/Rudich1988/python-project-50/maintainability)

### Демонстрация функций:
- [демонстрация функции -help и поиск различий в файлах json формата](https://asciinema.org/a/YyGjmPRfirgZEdODBHglg8fTB)
- [демонстрация функции -help и поиск различий в файлах json и yml форматов](https://asciinema.org/a/0dx6ZvZtiAlU2PEOsJi5Ur7Ld)
- [демонстрация функции -help и поиск различий в файлах yml формата](https://asciinema.org/a/1pRmjB6zqxPCMLALjS2Ok7bo9)
- [поиск различий в файлах json формата со вложенностью](https://asciinema.org/a/7kaeUDnzrelMaRujlys2E4khp)
- [демонстрация различий файлов json в разном оформлении](https://asciinema.org/a/rKP56355JIbb9sF9LQgYlliEk)
- [демонстрация различий файлов json в json формате](https://asciinema.org/a/jz4lV73DrkP9NDNO49gZ2nY1n)