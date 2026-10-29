# Mentor - AI Coding Tutor

## Start on Windows

1. Install Python 3.10 or newer. On the installer screen, enable **Add python.exe to PATH**.
2. Double-click **run-windows.bat** in this folder. It creates the local virtual environment and installs Flask the first time.
3. Open http://127.0.0.1:8000, create an account, and start practicing. Leave the black terminal window open; press Ctrl+C there to stop Mentor.

If PowerShell says `python` is not found, install Python from python.org, reopen PowerShell, then double-click the batch file again. You do not need to activate `.venv` manually. Do not open `index.html` directly because the app needs its local server.

## Languages

The language picker includes 38 options from different eras: Python, JavaScript, TypeScript, Java, C, C++, C#, Go, Rust, PHP, Ruby, Kotlin, Swift, Dart, Perl, R, Bash, Fortran, Pascal, Julia, Scala, Lua, Haskell, Zig, Objective-C, F#, OCaml, Clojure, Elixir, Nim, D, Crystal, COBOL, PowerShell, Mojo, V, Odin, and SQL.

Mentor can explain pasted code in any listed language without that language's compiler. Auto detect is also available in free-code mode. Challenge checking runs locally only when the needed compiler or interpreter is installed; the language menu shows the current toolchain status. SQL can be explained, while this stdin/stdout challenge runner does not execute SQL queries. The app does not automatically install compilers. Examples: Python needs Python, Java needs a JDK, C# and F# need the .NET SDK, and TypeScript needs both `tsc` and Node.js.

## Practice

- **Practice with a sample problem:** choose a question on the left, write code in the editor, then click Check my code. Use Give me a hint if you get stuck.
- **Understand my own code:** choose this option on the left, paste the assignment in the problem box, then paste your code. Mentor detects the language automatically as you type. Click Explain my code for a trace, likely output, and hints. You can choose a language yourself if detection is unsure. This mode never runs your code. When AI is connected, the server sends the problem and code to OpenAI for guidance.
- Create an account to keep practice scores and attempts in the local SQLite database.

## Optional AI explanations

Challenge checks and built-in hints work without an API key. The Get solution button provides complete offline Python reference solutions for the question bank; these are labeled as offline. With an OpenAI API key, Mentor sends the problem context and code to the OpenAI Responses API for task-aware hints, code traces, output explanations, bug feedback, and Socratic dialogue. Without the key, Mentor uses local code scanning and offline Socratic prompts. The app displays whether a key is configured.

In PowerShell, set the key in the same window and start the server:

    $env:OPENAI_API_KEY = "your-api-key"
    $env:OPENAI_MODEL = "gpt-5-mini"
    .\.venv\Scripts\python.exe app.py

Keep the key private; do not put it in `index.html`.

## Project data and safety

The source files are `app.py`, `extra_challenges.py`, `offline_solutions.py`, `index.html`, `requirements.txt`, and `run-windows.bat`. User accounts and attempts stay in `tutor.sqlite3`; existing records are preserved. The app creates `.session-secret` on first start.

Challenge submissions compile or run on this computer in temporary folders with time limits. This is a localhost learning prototype, not a hardened code sandbox. Use code you trust and do not expose the server to the internet.
