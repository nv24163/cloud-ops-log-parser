# Task 1 — Parse a single line (Lesson 1)
# Implement parse_log_line(line) and run the test cases.

def parse_log_line(line: str):
    """Return (timestamp, level, service, message) OR None if invalid format."""
    # TODO: 1) strip whole line
    # TODO: 2) if empty -> return None
    # TODO: 3) split by '|'
    # TODO: 4) strip each part
    # TODO: 5) if not exactly 4 parts -> return None
    # TODO: 6) return tuple(parts)
    pass


def run_tests():
    cases = [
        ("2026-02-05 08:11:20 | ERROR | db | DB timeout",
         ("2026-02-05 08:11:20", "ERROR", "db", "DB timeout")),
        ("  2026-02-05 08:11:20|ERROR|db|DB timeout  \n",
         ("2026-02-05 08:11:20", "ERROR", "db", "DB timeout")),
        ("BAD LINE WITHOUT SEPARATORS", None),
        ("2026-02-05 | INFO | auth | ok | EXTRA", None),
    ]

    for i, (line, expected) in enumerate(cases, start=1):
        got = parse_log_line(line)
        print(f"Case {i}: expected={expected} got={got}")


if __name__ == "__main__":
    run_tests()
