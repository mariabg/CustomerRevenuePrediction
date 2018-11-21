import sys
import glob
import pandas as pd

# bash commands for splitting a huge dataset into several smaller ones
# split -l 100000 train_v2.csv
# echo 'channelGrouping,customDimensions,date,device,fullVisitorId,geoNetwork,hits,socialEngagementType,totals,trafficSource,visitId,visitNumber,visitStartTime' > headerfile
# for csv in *.csv; do cat headerfile $csv > tmpfile2; mv tmpfile2 $csv; done
# rm headerfile

def main ():
    allFiles = glob.glob("*.csv")

    misc = pd.DataFrame({'visitId' : [], '': [], 'fullVisitorId': [], 'channelGrouping': [], 'socialEngagementType': [], 'date': [], 'visitStartTime': [], 'visitNumber': []})
    misc.to_csv('misc.csv')

    for fl in allFiles:
        print(fl)
        df = pd.read_csv(fl, usecols=["channelGrouping", "customDimensions", "date", "device", "fullVisitorId", "geoNetwork", "hits", "socialEngagementType", "totals", "trafficSource", "visitId", "visitNumber", "visitStartTime"])
        misc['visitId'] = df['visitId'].copy()
        misc['fullVisitorId'] = df['fullVisitorId'].copy()
        misc['channelGrouping'] = df['channelGrouping'].copy()
        misc['socialEngagementType'] = df['socialEngagementType'].copy()
        misc['date'] = df['date'].copy()
        misc['visitStartTime'] = df['visitStartTime'].copy()
        misc['visitNumber'] = df['visitNumber'].copy()
        print(misc.shape)
        with open('misc.csv', 'a') as f:
            misc.to_csv(f, header=False)

main()
