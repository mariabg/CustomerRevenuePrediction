import sys
import glob
import pandas as pd


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

    # Select an specific group, like a country
    # df = df.loc[df['country'] == 'Spain']

    # df.to_csv('cleanedData.csv', encoding='utf-8')


main()
