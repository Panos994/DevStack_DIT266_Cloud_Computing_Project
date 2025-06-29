import re

# Τα metrics μου ως raw strings (copy-paste όπως τα έχω στο report παραπάνω εδώ)
disk_data = """
| 2025-06-29T12:50:00+00:00 |       300.0 |  20.0 |
| 2025-06-29T12:55:00+00:00 |       300.0 |  20.0 |
| 2025-06-29T13:00:00+00:00 |       300.0 |  20.0 |
| 2025-06-29T13:05:00+00:00 |       300.0 |  20.0 |
| 2025-06-29T13:10:00+00:00 |       300.0 |  20.0 |
"""

ram_data = """
| 2025-06-29T12:55:00+00:00 |       300.0 | 250.91796875 |
| 2025-06-29T13:00:00+00:00 |       300.0 | 273.09765625 |
| 2025-06-29T13:05:00+00:00 |       300.0 |  275.4609375 |
| 2025-06-29T13:10:00+00:00 |       300.0 |  304.8984375 |
"""

cpu_data = """
| 2025-06-29T12:55:00+00:00 |       300.0 | 286820000000.0 |
| 2025-06-29T13:00:00+00:00 |       300.0 | 577640000000.0 |
| 2025-06-29T13:05:00+00:00 |       300.0 | 872810000000.0 |
| 2025-06-29T13:10:00+00:00 |       300.0 | 960030000000.0 |
"""

# Τιμές μονάδας
vcpu_count = 1
vcpu_price = 0.05     # €/vCPU/ώρα
ram_price = 0.01      # €/GB/ώρα
storage_price = 0.005 # €/GB/ώρα
fip = 1               # Αλλαξε αν δεν έχεις FIP
fip_price = 0.02      # €/ώρα

# Εξαγωγή values
def extract_values(data):
    return [float(x) for x in re.findall(r"\|\s*[\d\-T\:\+\.]+\s*\|\s*[\d\.]+\s*\|\s*([\d\.]+)", data)]

# Δίσκος (GB) - σταθερό
disk_gb = extract_values(disk_data)[0]

# RAM (MB) -> GB
ram_vals = extract_values(ram_data)
ram_avg_gb = sum(ram_vals)/len(ram_vals)/1024  # από MB σε GB

# CPU (cumulative value, πχ nanoseconds) - Δείγμα
cpu_vals = extract_values(cpu_data)
cpu_delta = cpu_vals[-1] - cpu_vals[0]         # μεταβολή στη διάρκεια
intervals = len(cpu_vals)-1
hours = intervals * 300.0 / 3600               # Κάθε 300s = 5min, το σύνολο σε ώρες

# Υπολογισμός κόστους
cost_vcpu = vcpu_count * vcpu_price * hours
cost_ram = ram_avg_gb * ram_price * hours
cost_storage = disk_gb * storage_price * hours
cost_fip = fip * fip_price * hours

total = cost_vcpu + cost_ram + cost_storage + cost_fip

print(f"--- Προσομοίωση Χρέωσης (για διάστημα {hours:.2f} ώρες) ---")
print(f"vCPU ({vcpu_count} x {vcpu_price} €/ώρα): {cost_vcpu:.4f} €")
print(f"RAM ({ram_avg_gb:.2f} GB x {ram_price} €/GB/ώρα): {cost_ram:.4f} €")
print(f"Storage ({disk_gb} GB x {storage_price} €/GB/ώρα): {cost_storage:.4f} €")
print(f"Floating IP ({fip} x {fip_price} €/ώρα): {cost_fip:.4f} €")
print(f"Συνολικό κόστος: {total:.4f} €")
