import logging

logging.basicConfig(
    handlers=[
        logging.FileHandler(
            filename="./logs/log_records.txt", encoding="utf-8", mode="a+"
        )
    ],
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%F %A %T",
    level=logging.INFO,
)


def notify(text):
    print(text)
    logging.info(text)
