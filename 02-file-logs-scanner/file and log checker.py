# Dictionaries to store our counts
ip_counts = {}          # counts EVERY request per IP (all log levels)
flag_counts = {}        # counts how many INFO / WARNING / ERROR lines total
suspicious_ips = {}     # counts ONLY WARNING/ERROR lines per IP

with open("server.log", "r") as file:
    for i in file:
        parts = i.split()   # break the line into pieces by spaces
        ips = parts[3]      # the IP address is always the 4th item (index 3)
        flags = parts[2]    # the log level (INFO/WARNING/ERROR) is the 3rd item (index 2)

        # --- Count every request per IP, no matter the log level ---
        if ips in ip_counts:
            ip_counts[ips] += 1
        else:
            ip_counts[ips] = 1

        # --- Count how many lines are INFO vs WARNING vs ERROR overall ---
        if flags in flag_counts:
            flag_counts[flags] += 1
        else:
            flag_counts[flags] = 1

        # --- Only for WARNING/ERROR lines: count how many bad entries per IP ---
        if flags == "WARNING" or flags == "ERROR":
            if ips in suspicious_ips:
                suspicious_ips[ips] += 1
            else:
                suspicious_ips[ips] = 1

# Sort ip_counts to find the top 5 most active IPs (highest count first)
sorted_ips = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)[:5]

# Sort flag_counts to see the breakdown of log levels
sorted_flags = sorted(flag_counts.items(), key=lambda item: item[1], reverse=True)

# Filter suspicious_ips down to only IPs with 3 or more bad (WARNING/ERROR) entries
flagged = {}
for ip, count in suspicious_ips.items():
    if count >= 3:
        flagged[ip] = count

# ---- Print everything ----
print("Top 5 most active IPs:")
print(sorted_ips)

print("\nLog level breakdown:")
print(sorted_flags)

print("\nFlagged (suspicious) IPs - 3+ WARNING/ERROR entries:")
print(flagged)