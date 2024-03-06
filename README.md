*------Project Pig-----*
========================


**----How to prepare----**
--------------------------
Install chocolatey:  **Windows Only**
    Open your terminal and paste this:        
        Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

Install make:       **Windows Only**
    >>> choco install make

Install a virtual environment:
    >>> make venv

    Activate the virtual environment in your terminal:
        # Windows
            >>> . .venv/Scripts/activate
        # Linux/MacOS
            >>> . .venv/bin/activate

        Install all requirements:
            >>> make install


**-How to run the program-**
----------------------------
To be able to run the program you need to export the pythonpath.
This is done with this code in Git Bash:
    >>>export PYTHONPATH=”.”
After that you can start the game with the command:
    >>> python pig/main.py
All of the program’s code is located in the directory pig/.


**-How to run the unittests-**
------------------------------
To run all unittests:
    >>> make unittest

To run a single testfile:
    >>> python -m unittest test.test_game

To run a single testcase from a testfile:
    >>> python -m unittest test.test_game.TestGameClass.test_init_default_object

To run all unittests with coverage:
    >>> make coverage

To get the html address for the coverage:
    >>> coverage html
        to read the coverage report locate htmlcov/index.html in your directory

To run all unittests with coverage and linters:
    >>> make test


**-How to use linters-**
------------------------
Flake8:
    >>> flake8

Pylint
    >>> make pylint


**-Documentation-**
-------------------
    All of our documentation for this program can be found in the directory doc/.

To reproduce documentation:
    >>> make doc
    >>> make pyreverse

To delete all generated files:
    >>> make clean

To delete all generated files and installations:
    >>> make clean-all
