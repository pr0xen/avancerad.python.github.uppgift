import argparse
import logging

def setup_logging(level: str = "INFO"):
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def process_message(message: str) -> str:
    """Convert the message to uppercase."""
    return message.upper()

def main():
    parser = argparse.ArgumentParser(description="Advanced GitHub Assignment Script")
    parser.add_argument(
        "-m", "--message",
        type=str,
        default="Hello, GitHub assignment!",
        help="Message to process"
    )
    parser.add_argument(
        "-l", "--log",
        type=str,
        default="INFO",
        help="Logging level (DEBUG, INFO, WARNING, ERROR)"
    )
    args = parser.parse_args()

    setup_logging(args.log)
    logging.info("Starting the assignment script.")

    result = process_message(args.message)
    logging.info(f"Processed message: {result}")
    print(result)

if __name__ == "__main__":
    main()