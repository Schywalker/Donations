
import pandas as pd

train_file_path = "/Users/nellie/Documents/github_NR/kaggle/Donation/train.csv"
test_file_path = "/Users/nellie/Documents/github_NR/kaggle/Donation/test.csv"


def read_file(file_path):
	df = pd.read_csv(file_path)
	return df


def main():
 
 df_train = read_file(train_file_path)
 print(df_train.head())


if __name__ == '__main__':
		main()	