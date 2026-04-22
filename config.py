from os import environ as env

class Config:
    # ===== Data =====
    DATASET_DIR = "/kaggle/input/subchannel"
    TRAIN_SET_PATH = VALIDATION_SET_PATH = TEST_SET_PATH = DATASET_DIR
    TRAIN_SET_FILENAME = "train.csv"
    VALIDATION_SET_FILENAME = "val.csv"
    TEST_SET_FILENAME = "test.csv"

    # ===== Output =====
    MODEL_PATH = "/kaggle/working/models"
    EVALUATION_REPORT_PATH = "/kaggle/working/reports"
    CONFUSION_MATRIX_PATH = "/kaggle/working/reports"

    # ===== Training config =====
    SEED = int(env.get("SEED", "42"))
    EPOCH = int(env.get("EPOCH", "10"))
    MAX_LEN = int(env.get("MAX_LEN", "512"))
    BATCH_SIZE = int(env.get("BATCH_SIZE", "64"))
    LR = float(env.get("LR", "2e-5"))
    WEIGHT_DECAY = float(env.get("WEIGHT_DECAY", "0.01"))
    WARMUP_RATIO = float(env.get("WARMUP_RATIO", "0.1"))

    # ===== Hugging Face model ID =====
    HF_MODEL_ID = env.get("HF_MODEL_ID", "bert-base-multilingual-uncased")

# instantiate
config = Config()