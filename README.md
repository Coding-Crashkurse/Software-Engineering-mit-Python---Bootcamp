# Software-Engineering-mit-Python---Bootcamp

1. [Einführung (Warum SE mit Python)](#einführung)
2. [IDEs: VSCode und PyCharm](#ides)
3. [Modules & Packages](#modules-packages)
4. [Clean Code](#clean-code)
5. [Type Hinting](#type-hinting)
6. [Tooling](#tooling)
7. [Dependency Management & Virtual Environments](#dependency-management)
8. [Poetry](#poetry)
9. [Git & Github](#git-github)
10. [Pre-Commit-hooks](#pre-commit-hooks)
11. [Unittests und TDD](#unittests-tdd)
12. [Versionierung (z.B. SemVer)](#versionierung)
13. [Github Actions (CI/CD)](#github-actions)
14. [Dokumentation](#dokumentation)
15. [Grundlagen Typer](#grundlagen-typer)
16. [Capstone Projekt: Passwort Manager mit Typer, inkl. Packaging und automatischer Veröffentlichung über CI/CD Pipeline auf Pypi](#capstone-projekt)


## Einführung (Warum SE mit Python) {#einführung}

Inhalt

## IDEs: VSCode und PyCharm {#ides}

Inhalt

## Modules & Packages {#modules-packages}

<strong>Module:</strong> Ein Modul ist eine einzelne Python-Datei, die Python-Code wie Funktionen, Klassen oder Variablen enthält. Module werden verwendet, um den Code in kleinere, überschaubare Teile zu zerlegen, die spezifische Funktionen oder Aufgaben erfüllen. Module können in anderen Python-Dateien importiert und verwendet werden.
<strong>Packages:</strong> Ein Paket ist eine Sammlung von verwandten Modulen, die in einem Verzeichnis organisiert sind. Jedes Paketverzeichnis enthält eine __init__.py-Datei, die signalisiert, dass das Verzeichnis als Paket behandelt werden sollte. Die __init__.py-Datei kann leer sein oder Initialisierungscodes für das Paket enthalten.

<pre>
my_project/
│
├── main.py
│
├── package_a/
│   ├── __init__.py
│   ├── module_a1.py
│   └── module_a2.py
│
└── package_b/
    ├── __init__.py
    ├── module_b1.py
    └── module_b2.py
</pre>

Beispiel für import

```python
import package_a.module_a1
from package_a.module_a1 import greet
```