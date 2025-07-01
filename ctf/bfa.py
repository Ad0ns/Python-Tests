import subprocess
import itertools
import string

# Define charset to use (alphanum here)
charset = string.ascii_letters + string.digits  # 62 characters (a-z, A-Z, 0-9)


# Flag prefix and suffix
#prefix = "BMCTF{"
#suffix = "}"

# Path to the binary that checks the flag
binary = "./Diff_EQ"  # Replace with actual binary path

# Loop over all 2-character combinations
for combo in itertools.product(charset, repeat=2):
    inner = ''.join(combo)
    #flag = f"{prefix}{inner}{suffix}"
    flag =f"{inner}"
    # Run the binary with the flag as input
    try:
        result = subprocess.run([binary], input=flag.encode(), capture_output=True, timeout=1)
        output = result.stdout.decode()

        if "Correct flag!" in output:
            print(f"[+] Found the flag: {flag}")
            break
        else:
            print(f"[-] Tried: {flag}")
    except Exception as e:
        print(f"[!] Error with flag {flag}: {e}")
