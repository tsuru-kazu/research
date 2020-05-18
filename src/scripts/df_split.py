from sklearn.model_selection import train_test_split
import pandas as pd

INPUT_DIR = '../data/input'
OUTPUT_DIR = '../data/output'

INPUT_FILE = 'JPvideos.csv'

df = pd.read_csv(INPUT_DIR + '/' + INPUT_FILE)

