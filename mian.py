import time

def generate_frequency(freq):
    period = 1.0 / freq
    half_period = period / 2
    try:
        while True:
            print("HIGH")
            time.sleep(half_period)
            print("LOW")
            time.sleep(half_period)
    except KeyboardInterrupt:
        print("Frequency generation stopped.")

def main():
    try:
        freq = int(input("Enter frequency (1-80 Hz): "))
        if 1 <= freq <= 80:
            generate_frequency(freq)
        else:
            print("Frequency must be between 1 and 80 Hz.")
    except ValueError:
        print("Please enter a valid whole number.")
    except KeyboardInterrupt:
        print("Program interrupted.")

if __name__ == "__main__":
    main()
