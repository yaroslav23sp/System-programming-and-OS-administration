#!/bin/bash

DIR="/etc"

echo "Підрахунок Файлів у директорії......"

file_count=$(find "$DIR" -type f 2>/dev/null | wc -l)

echo "Кількість звичайних файлів: $file_count"
