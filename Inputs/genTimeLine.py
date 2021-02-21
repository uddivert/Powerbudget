import pandas as pd
import matplotlib.pyplot as plt

previousTimeline = pd.read_csv("newTimeline.csv")
newTimeline = pd.read_csv("CSVMOCIPOWER_2_16_2021.csv")
# newTimeline = pd.read_excel("MOCIPower5CellYPlus4.xlsx")

firstTime = newTimeline['Time (UTCG)'][0]

offset = 0
for t in newTimeline['Time (UTCG)']:
    if t == firstTime:
        if offset != 0:
            offset -= 1
            break
    offset += 1

newDF = newTimeline[:offset]

print(newDF.head())

# for i in range(offset+1, newTimeline.shape[0]):
#     if (i % offset == 1):
#         print(i)
    
#     newDF.at[i%offset, 'Power (W)'] += newTimeline.at[i, 'Power (W)'] 

newTimeline = newDF
print(newTimeline.head())

newTimeline['Current Submode'] = ""

index = 0
working = True

print("Adding submods")

while(working):
    for i in range(0, previousTimeline.shape[0]):
        if index < newTimeline.shape[0]:
            newTimeline.at[index, 'Current Submode'] = previousTimeline.at[i, 'Current Submode']
            index += 1
        else:
            working = False
            break

newTimeline = newTimeline.set_index('Time (UTCG)')
print(newTimeline.head())
newTimeline.to_csv("updatedTimeline.csv")

print(newTimeline.shape)
print("Plotting")
line = newTimeline.plot.line(y='Power (W)')
plt.show()