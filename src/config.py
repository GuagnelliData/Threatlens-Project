from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
CSV_FILE = DATA_DIR / "MachineLearningCVE" / "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.2
BATCH_SIZE = 256
EPOCHS = 10
