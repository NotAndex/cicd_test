from pathlib import Path

def main():
    print(f"cwd: {Path.cwd()}")
    print(f"home: {Path.home()}")
    
if __name__ == "__main__":
    main()