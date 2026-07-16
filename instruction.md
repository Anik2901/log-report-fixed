An Apache-style access log is provided at /app/access.log. Each line is one HTTP request. Parse the log and write a JSON summary report to /app/report.json. Treat /app/access.log as read-only; do not modify it.

/app/report.json must be a single JSON object with exactly these three keys:
- "total_requests" (integer): the total number of request lines in the log.
- "unique_ips" (integer): the number of distinct client IP addresses (the first whitespace-separated field of each line).
- "top_path" (string): the request path that appears most often (the path in the quoted request line, e.g. "/index.html"). If two or more paths tie for the most requests, use the lexicographically smallest.

Success criteria:
1. /app/report.json exists.
2. /app/report.json is a JSON object whose keys are exactly "total_requests", "unique_ips", and "top_path".
3. "total_requests" equals the total number of request lines in /app/access.log.
4. "unique_ips" equals the number of distinct client IP addresses in /app/access.log.
5. "top_path" is the path requested most often in /app/access.log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
