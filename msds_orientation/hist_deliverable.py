import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def reader(path):
    df = pd.read_excel(path)
    return df


if __name__ == '__main__':
    print(reader('data/MSDS-Orientation-Computer-Survey.xlsx'))
    df = reader('data/MSDS-Orientation-Computer-Survey.xlsx')

    plt.hist(df['RAM (in GB)'], bins=15, range=(0,70), color='xkcd:raspberry')
    plt.xlabel('RAM (GB)')
    plt.ylabel('Counts')
    plt.title('Distribution of RAM across Cohorts (2021-2024)')
    plt.show()
    #plt.savefig('hist_deliverable')
    