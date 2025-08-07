import argparse
from backend.parser import parse_resume

def main():
    parser = argparse.ArgumentParser(description="Resume Scanner CLI")
    parser.add_argument('--file', required=True, help='Path to the resume file')
    args = parser.parse_args()

    with open(args.file, 'rb') as f:
        print("Parsing...")
        result = parse_resume(f)
        print("Result:", result)

if __name__ == "__main__":
    main()