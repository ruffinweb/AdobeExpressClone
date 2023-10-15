import multiprocessing
import os
from dotenv import load_dotenv

load_dotenv()


bind = os.getenv("mm_app_ADDRESS")
workers = multiprocessing.cpu_count() * 2 + 1

