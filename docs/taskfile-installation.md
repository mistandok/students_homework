# Установка Taskfile

**Task** — это современный, кроссплатформенный инструмент сборки, вдохновленный Make, но написанный на Go. Он позволяет определять команды в YAML файле и выполнять их через простой интерфейс.

## Зачем нужен Taskfile?

- 🚀 **Простота**: Один файл `Taskfile.yml` с понятным YAML синтаксисом
- 🔄 **Переиспользование**: Определите команду один раз, используйте везде
- 📚 **Документирование**: Команды самодокументируются
- 🎯 **Кроссплатформенность**: Работает одинаково на всех операционных системах

## Установка Task

### macOS

**Homebrew (рекомендуется):**
```bash
brew install go-task
```

**MacPorts:**
```bash
port install go-task
```

### Linux

**Snap:**
```bash
sudo snap install task --classic
```

**Для Ubuntu/Debian через apt:**
```bash
sudo sh -c "echo 'deb [trusted=yes] https://repo.goreleaser.com/apt/ /' >> /etc/apt/sources.list.d/goreleaser.list"
sudo apt update
sudo apt install task
```

**Arch Linux:**
```bash
pacman -S go-task
```

### Windows

**Scoop (рекомендуется):**
```bash
scoop install task
```

**Chocolatey:**
```bash
choco install go-task
```

**Winget:**
```bash
winget install Task.Task
```

### Универсальные способы установки

#### Установочный скрипт (Linux/macOS)

```bash
# Установка в ./bin относительно текущей директории
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d

# Установка в кастомную директорию
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin
```

#### Бинарный файл

1. Перейдите на [страницу релизов](https://github.com/go-task/task/releases)
2. Скачайте бинарный файл для вашей платформы
3. Распакуйте и поместите в директорию, указанную в `$PATH`

#### NPM (кроссплатформенный)

```bash
# Глобальная установка
npm install -g @go-task/cli

# Или как зависимость проекта
npm install --save-dev @go-task/cli
```

#### Go install

Если у вас установлен Go:

```bash
go install github.com/go-task/task/v3/cmd/task@latest
```

## Проверка установки

После установки проверьте, что Task доступен:

```bash
task --version
```

Вы должны увидеть что-то вроде:
```
Task version: v3.x.x
```

## Первое использование

В корне проекта уже есть файл `Taskfile.yml`. Чтобы посмотреть доступные команды:

```bash
# Показать все доступные задачи
task --list

# Показать задачи с описаниями
task --list-all
```

Выполните команду:

```bash
# Инициализация проекта
task init

# Запуск всех тестов
task test

# Проверка кода линтером
task lint
```

## Альтернативы на разных платформах

### Если не можете установить Task глобально

Вы всегда можете использовать команды uv напрямую, так как они описаны в документации:

```bash
# Вместо task init
uv sync

# Вместо task test
uv run pytest

# Вместо task lint
uv run ruff check .
```

### Docker

Если у вас установлен Docker, можете использовать Task через контейнер:

```bash
docker run --rm -v ${PWD}:/work -w /work taskfile/task:latest --list
```

## Troubleshooting

### Command not found

Если после установки команда `task` не найдена:

1. **Проверьте PATH**: убедитесь, что директория установки Task в `$PATH`
2. **Перезапустите терминал** или выполните `source ~/.bashrc` / `source ~/.zshrc`
3. **Используйте полный путь**: найдите где установлен `task` и используйте полный путь

### Конфликт с системной командой task

На некоторых Linux системах уже есть команда `task` (Taskwarrior). В этом случае:

1. Используйте псевдоним: `alias t=task` в вашем `.bashrc`/.zshrc`
2. Или используйте полный путь до Go Task
3. Или переименуйте бинарный файл в `go-task`

### Ошибки выполнения на Windows

Если команды не выполняются на Windows:

1. Используйте PowerShell или Git Bash вместо cmd
2. Убедитесь, что у вас правильно настроен PATH
3. Некоторые команды могут потребовать WSL для корректной работы

## Дополнительные ресурсы

- [Официальная документация](https://taskfile.dev/)
- [GitHub репозиторий](https://github.com/go-task/task)
- [Примеры Taskfile.yml](https://github.com/go-task/examples)

## Поддержка

Если у вас возникли проблемы с установкой Task, вы всегда можете использовать команды `uv` напрямую — все необходимые команды описаны в документации к проекту.