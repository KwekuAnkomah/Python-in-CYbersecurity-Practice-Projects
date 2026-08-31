# Log File Analyzer

A Python script that reads a server log file and analyzes it for suspicious activity — built as practice for reading and parsing real-world log data.

## What it does
- Reads `server.log` line by line
- Counts total requests per IP address
- Counts how many INFO / WARNING / ERROR entries exist overall
- Flags any IP with 3 or more WARNING/ERROR entries as a possible brute-force login attempt

## What I learned
- Reading files with `with open()` instead of manual `open()`/`close()`
- Why the terminal's working directory matters when opening files by filename
- Splitting a log line into parts to extract specific fields (IP, log level)
- Building multiple count dictionaries in a single pass through a file
- Nesting `if` statements to apply a condition before counting
- Sorting a dictionary by value using `sorted()` and `lambda`
