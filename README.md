# Mentor — AI Coding Tutor

## Start on Windows

1. Install Python 3.10 or newer. On the installer screen, enable **Add python.exe to PATH**.
2. Double-click **run-windows.bat** in this folder. It creates the local virtual environment and installs Flask the first time.
3. Open http://127.0.0.1:8000, create an account, and start practicing. Leave the black terminal window open; press Ctrl+C there to stop Mentor.

If PowerShell says `python` is not found, install Python from python.org, reopen PowerShell, then double-click the batch file again. You do not need to activate `.venv` manually. Do not open `index.html` directly because the app needs its local server.

## Use free local AI

Mentor uses Ollama, which runs the AI model on your computer. There is no OpenAI API key, account, or per-request charge. The model download is about 1.9 GB; speed depends on your computer.

1. Install [Ollama for Windows](https://ollama.com/download/windows).
2. Open PowerShell and run `ollama pull qwen2.5-coder:3b`. Wait for the download to finish.
3. Start or restart Mentor with `run-windows.bat`.
4. In Mentor, scroll to **Free local AI (Ollama)** and click **Check local AI**.

The model runs locally through Ollama's API at `http://127.0.0.1:11434`; local API requests do not need an API key. Mentor also detects when Ollama is stopped or the model is missing and shows the matching setup step.

You can change the model in `.env` by setting `OLLAMA_MODEL`. The suggested 3B coding model is a compact option; a smaller model may be needed on a low-memory PC, and local answers can be less capable than larger hosted models.

## Languages

The language picker includes 38 options: Python, JavaScript, TypeScript, Java, C, C++, C#, Go, Rust, PHP, Ruby, Kotlin, Swift, Dart, Perl, R, Bash, Fortran, Pascal, Julia, Scala, Lua, Haskell, Zig, Objective-C, F#, OCaml, Clojure, Elixir, Nim, D, Crystal, COBOL, PowerShell, Mojo, V, Odin, and SQL.

Mentor can attempt explanations and answers for every listed language when the local model is running. Answer quality depends on the selected model and the code or question; it is not guaranteed. **Understand my own code** detects common language signatures locally and asks the local model to help when code is unclear and Ollama is running. You can also select a language yourself.

Sample checks run on this computer and require the matching compiler or interpreter. The language menu tells you whether that tool is ready and how to set it up. Examples: Python needs Python, Java needs a JDK, C needs GCC or Clang, C# and F# need the .NET SDK, and TypeScript needs both `tsc` and Node.js. SQL can be explained, but the sample checker does not execute SQL queries. Mentor does not automatically install compiler toolchains.

## How to use Mentor

- **Practice with a sample problem:** pick a question, choose your programming language, write code, and click **Check my code**. Add clarifications in the extra-details box; for example, saying “numbers only, not strings” for the palindrome problem switches the checker to the built-in number-palindrome inputs. A passing example means the program's printed answer matched the expected answer. Harmless labels such as `Answer: 9` are accepted; the final answer and order of multiple values still have to match.
- **Get hints:** choose how many hints you want, then click **Give me a hint**. Ollama gives task-aware hints; if it is unavailable, Mentor labels the built-in hint and explains how to start it.
- **Understand my own code or ask a question:** choose that mode, paste code if you have it, and type your question in the question box. Click **Ask Mentor / explain code**. You can ask without pasting code; choose a language yourself if you want a language-specific answer. Mentor gives an explanation and Socratic questions when code is present. This mode reads code but does not execute it.
- **Get an example answer:** The local model can produce a solution in the selected language when Ollama is running. Offline example answers are available for Python only and are clearly labeled.

## Project data and safety

The source files are `app.py`, `extra_challenges.py`, `offline_solutions.py`, `index.html`, `requirements.txt`, and `run-windows.bat`. User accounts and attempts stay in the local SQLite database `tutor.sqlite3`; `.session-secret` is created locally. Both are excluded from Git.

Challenge submissions run on this computer in temporary folders with time limits. The checker supports single-file console programs that read the sample input and print an answer; it does not run arbitrary websites, GUI programs, multi-file projects, or all library/build configurations. SQL can be explained but sample SQL execution is not included. The selected language's compiler or interpreter must be installed for sample checks. AI-generated explanations and code are best effort, may contain mistakes, and are not guaranteed to compile; review them and use **Check my code** against the sample inputs. This is a localhost learning prototype, not a hardened code sandbox. Use code you trust and do not expose the server to the internet.
