import pandas as pd
import statistics
import matplotlib.pyplot as plt
import clean_data as cd


# 1 Read xlsx file and get necessary data. This point also contains solving of task #5 - cleaning and verifying data.

df = pd.read_excel('vuz_u.xlsx')
entered = {}
graduated = {}
for i in range(29):
    year = cd.y_clear(df.iloc[i+40, 0])
    entered_clean = cd.data_cleaning(df.iloc[i+40, 2])
    graduated_clean = cd.data_cleaning(df.iloc[i+40, 4])
    entered[year] = entered_clean
    graduated[year] = graduated_clean

print(entered)


# 2 Using "statistics" module calculate mean, median, mode, variance and standard deviation of data which are analyzed.

graduated_mean = statistics.mean(graduated.values())

graduated_median = statistics.median(graduated.values())

graduated_mode = statistics.mode(graduated.values())

graduated_pvariance = statistics.pvariance(graduated.values())

graduated_pstdev = statistics.pstdev(graduated.values())

print(graduated_mean, graduated_median, graduated_mode, graduated_pvariance, graduated_pstdev, sep="\n")


# 3. Using "matplotlib.pyplot" module perform diagram of the analyzed data.

plt.plot(entered.keys(), entered.values(), label="Entered")
plt.plot(entered.keys(), graduated.values(), label="Graduated")

plt.xlabel("Years")
plt.ylabel("Number of entered/graduated, thousands persons")
plt.title("Number of entered and graduated persons in Ukraine 1990-2019")

plt.legend()

plt.grid()

plt.tight_layout()

plt.show()


# 4. Collections Series and Dataframe

graduated_years_col = pd.Series(graduated.keys())
graduated_persons_col = pd.Series(graduated.values())

print(graduated_years_col, graduated_persons_col, sep="\n")
print(graduated_persons_col[2])

print(graduated_persons_col.count(), graduated_persons_col.mean(), graduated_persons_col.min(),
      graduated_persons_col.max(), graduated_persons_col.std(), sep="\n")
print(graduated_persons_col.describe())

graduated_col = pd.Series(graduated.values(), index=graduated.keys())

print(graduated_col)
print(graduated_col["1995"])

graduated_dict = pd.DataFrame(graduated.items(), columns=["Years", "Graduated, thousands persons"])

print(graduated_dict)
print(graduated_dict[(graduated_dict != "1995") & (graduated_dict != "2005")])
print(graduated_persons_col.describe())
print(graduated_persons_col.sort_values())
