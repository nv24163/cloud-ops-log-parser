# cloud-ops-log-parser

A structured Python project that simulates a real-world Cloud Operations log parsing workflow.

This project focuses on building a safe, fault-tolerant log parser before performing filtering, reporting, or exporting operations.

---

# 📘 Scenario

Cloud operations teams receive log files containing thousands of lines.

Some lines are:
- Properly formatted
- Contain extra whitespace
- Missing fields
- Broken or malformed

Before any monitoring, alerting, or reporting can happen, logs must be safely parsed.

---

# 🧱 Log Format Specification

Each valid log line follows this structure:


timestamp | level | service | message


Example:


2026-02-05 08:11:20 | ERROR | db | DB timeout


There must be **exactly four fields separated by `|`**.

In Lesson 1:
- We validate only the format.
- We DO NOT validate allowed log levels yet.

---

# 🎯 Learning Objectives

By completing this project, you will:

- Safely parse structured log lines
- Handle malformed input gracefully
- Work with file I/O in Python
- Count and classify invalid data
- Export structured data to JSON
- Build modular, reusable parsing logic

---

# 📂 Project Structure


cloud-log-parser-foundations/
│
├── task1_parse_single.py
├── task2_parse_list.py
├── task3_parse_file.py
├── task4_report_invalids.py
├── task5_export_parsed_json.py
├── sample_logs.txt
└── parsed_logs.json (generated after Task 5)


---

# 🧩 Task Breakdown

---

## ✅ Task 1 — Parse a Single Line

File: `task1_parse_single.py`

Implement:

```python
def parse_log_line(line: str):

Requirements:

Strip whitespace

Return None if line is empty

Split using "|"

Strip each field

If number of fields ≠ 4 → return None

Return:

(timestamp, level, service, message)

This function is the foundation for all remaining tasks.

✅ Task 2 — Parse a List of Lines

File: task2_parse_list.py

Accept a Python list of raw log lines

Use parse_log_line()

Skip invalid lines

Return a list of valid parsed tuples

✅ Task 3 — Parse a Log File

File: task3_parse_file.py

Open sample_logs.txt

Read line-by-line

Parse each line

Print the first 5 valid parsed tuples

This simulates processing a real log file.

✅ Task 4 — Count Invalid Format Lines

File: task4_report_invalids.py

Count:

Total lines

Valid lines

Invalid format lines

Output must match EXACTLY:

Total lines: X
Valid lines: Y
Invalid format lines: Z
✅ Task 5 — Export Parsed Logs to JSON

File: task5_export_parsed_json.py

Read sample_logs.txt

Parse valid lines

Export to parsed_logs.json

Required JSON structure:

[
  {
    "timestamp": "...",
    "level": "...",
    "service": "...",
    "message": "..."
  }
]
⚠️ Critical Implementation Rules

These rules are required for full marks:

Always start with:

line = line.strip()

If line becomes empty:

return None

After splitting:

Strip each field

Ensure exactly 4 fields

Never crash on bad input

Invalid lines must return None

🧪 How to Run

From the project root:

python task1_parse_single.py
python task2_parse_list.py
python task3_parse_file.py
python task4_report_invalids.py
python task5_export_parsed_json.py

After running Task 5, a new file will be generated:

parsed_logs.json
🧠 Design Approach

This project follows a layered parsing strategy:

Build a safe, reusable parsing function

Reuse that function across all tasks

Separate parsing logic from file handling

Keep validation minimal and focused

Avoid unnecessary assumptions about data

This mirrors real-world production log pipelines.

📊 Grading Rubric (10 Points)
Criteria	Points
Correct parsing logic	4
Proper invalid handling	2
Correct file processing	2
Correct JSON export structure	2
Total	10
🛠 Requirements

Python 3.8+

No external libraries required

Uses only Python standard library

🚀 Future Improvements (Beyond Lesson 1)

Possible enhancements:

Validate allowed log levels (INFO, WARNING, ERROR)

Convert timestamp to datetime objects

Add CLI arguments

Add unit tests

Add logging instead of print

Handle very large files efficiently

👤 Author

Cloud Operations Log Parsing Lab
Isa AlShallan
