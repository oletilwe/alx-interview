#!/usr/bin/python3
import sys
import signal


def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_line(line, total_size, status_codes):
    parts = line.split()
    if len(parts) != 9:
        return total_size

    try:
        ip = parts[0]
        dash = parts[1]
        date = parts[2]
        request = parts[3]
        status_code = parts[-2]
        file_size = parts[-1]

        if request != '"GET /projects/260 HTTP/1.1"':
            return total_size

        file_size = int(file_size)
        status_code = int(status_code)

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

        total_size += file_size
    except Exception:
        pass

    return total_size


def signal_handler(sig, frame):
    print_statistics(total_size, status_codes)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    total_size = process_line(line, total_size, status_codes)
    line_count += 1

    if line_count % 10 == 0:
        print_statistics(total_size, status_codes)
