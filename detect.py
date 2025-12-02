log = open("access.log").read().splitlines()

suspicious = []

for line in log:
    ip, dash, endpoint = line.split(" ", 2)

    if "/admin" in line:
        suspicious.append(f"{ip} tried to access admin page")

    if "' OR 1=1" in line:
        suspicious.append(f"{ip} attempted SQL Injection")

    if log.count(line) > 2:
        suspicious.append(f"{ip} is making too many requests")

# Save Report
with open("report.txt", "w") as r:
    r.write("Suspicious Activity Report\n\n")
    for s in set(suspicious):
        r.write(s + "\n")

print("Report generated: report.txt")