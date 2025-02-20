#!/bin/bash

# Функция для вывода справки
usage() {
    echo "Использование: $0 [-p] <имя файла или шаблон>"
    echo "  -p  Включает режим поиска по шаблону (подстроке)"
    exit 1
}

# Проверка на пустые аргументы
if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    usage
fi

# Обработка аргументов
if [ "$1" == "-p" ]; then
    if [ -z "$2" ]; then
        usage
    fi
    PATTERN="$2"
    FILES_TO_DELETE=$(find . -type f -name "*$PATTERN*" -not -name "*[A-Z]*")
else
    PATTERN="$1"
    FILES_TO_DELETE=$(find . -type f -name "$PATTERN" -not -name "*[A-Z]*")
fi

# Проверка наличия файлов для удаления
if [ -z "$FILES_TO_DELETE" ]; then
    echo "Файлы не найдены."
    exit 0
fi

# Удаление файлов
for file in $FILES_TO_DELETE; do
    echo "Удаляю: $file"
    rm "./$file"
done

echo "Готово."
