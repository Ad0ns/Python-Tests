import time
import hashlib

def generate_secret(minute):
    # Replace this with the actual logic you found from the binary
    # For example, hashing the minute (this is a placeholder!)
    return hashlib.md5(str(minute).encode()).hexdigest()

def main():
    current_minute = int(time.time() // 60)
    
    print("Secrets for minutes around current time:")
    for offset in range(-5, 6):  # 5 minutes before to 5 minutes after
        guess_minute = current_minute + offset
        secret = generate_secret(guess_minute)
        print(f"Minute {guess_minute}: {secret}")

if __name__ == "__main__":
    main()
