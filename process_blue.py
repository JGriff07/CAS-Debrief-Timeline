import pandas as pd

def process_blue_timeline(df, start_time):
    #Drop blanks lines from the dataframe
    df.drop(df[df['Label'] == None].index, inplace=True)

    count = len(df.index) + 1

    #set first line of dataframe to be vul start with empty 'x' as placeholder
    new_df = pd.DataFrame(data={'Label':df['Label'], 'Asset':df['To'], 'Color':'White', 'Hatch':'', 'Height':0.8, 'Count':count, 'Start':start_time['Vul Start'], 'End':start_time['Vul Start']}, index=[0])

    z = 1

    #make individual rows from each rectangle which needs be drawn
    for index, row in df.iterrows():
        label = row['Label']
        sender = row['From']
        asset = row['To']
        nom_time = row['Nominated']
        pass_time  = row['Passed']
        tally_time = row['Tally']
        first_time = row['First Effect']
        last_time = row['Last Effect']
        x = pd.DataFrame(data=[
            {'Label': label, 'Asset':asset, 'Color':'Yellow', 'Hatch':'', 'Height':0.8, 'Count':count, 'Start':pass_time,'End':tally_time},
            {'Label': label, 'Asset':asset, 'Color':'White', 'Hatch':'/', 'Height':0.7, 'Count':count, 'Start':tally_time, 'End':first_time},
            {'Label': label, 'Asset':asset, 'Color':'Green', 'Hatch':'', 'Height':0.8, 'Count':count, 'Start':first_time, 'End':last_time}
            ], index=[index, index+1, index+2])
        new_df = pd.concat([new_df, x])
        count = count - 1
        z = z + 3

    #Append Knock It Off to end of dataframe
    y = pd.DataFrame(data={'Label':df['Label'], 'Asset':df['To'], 'Color':'White', 'Hatch':'', 'Count':count, 'Start':start_time['Knock It Off'], 'End':start_time['Knock It Off']}, index=[0])
    new_df = pd.concat([new_df, y])

    #calculate and then add relative_start and relative_length to each row
    new_df['Start'] = pd.to_datetime(new_df['Start'])
    new_df['End'] = pd.to_datetime(new_df['End'])
    new_df['rel_start'] = ((new_df['Start'] - new_df['Start'].min()).dt.seconds/60)
    new_df['rel_length'] = ((new_df['End'] - new_df['Start']).dt.seconds/60)

    #print(new_df.to_string())
    #new_df.reindex(index=new_df.index, columns=['Count'])
    return new_df

def process_jtac_timeline(df, start_time):
    #Drop blanks lines from the dataframe
    df.drop(df[df['Label'] == None].index, inplace=True)

    #set first line of dataframe to be vul start with empty 'x' as placeholder
    new_df = pd.DataFrame(data={'Label':df['Label'], 'Asset':df['From'], 'Color':'White', 'Hatch':'', 'Height':0.8, 'Start':start_time['Vul Start'], 'End':start_time['Vul Start']}, index=[0])

    #make individual rows from each rectangle which needs be drawn
    for index, row in df.iterrows():
        label = row['Label']
        sender = row['From']
        asset = row['To']
        nom_time = row['Nominated']
        pass_time  = row['Passed']
        tally_time = row['Tally']
        first_time = row['First Effect']
        last_time = row['Last Effect']
        x = pd.DataFrame(data=[
            {'Label': label, 'Asset': asset, 'Color': 'Black', 'Hatch': '', 'Height':0.8, 'Start': nom_time, 'End': nom_time},
            {'Label': label, 'Asset':sender, 'Color':'White', 'Hatch':'', 'Height':0.05, 'Start':nom_time,'End':pass_time},
            {'Label': label, 'Asset':sender, 'Color':'Yellow', 'Hatch':'', 'Height':0.8, 'Start':pass_time, 'End':tally_time},
            {'Label': label, 'Asset': sender, 'Color': 'Green', 'Hatch': '/', 'Height': 0.8, 'Start': first_time, 'End': last_time}
            ], index=[index, index+1, index+2, index+3])
        new_df = pd.concat([new_df, x])

    #Append Knock It Off to end of dataframe
    y = pd.DataFrame(data={'Label':df['Label'], 'Asset':df['From'], 'Color':'White', 'Hatch':'', 'Height':0.8, 'Start':start_time['Knock It Off'], 'End':start_time['Knock It Off']}, index=[0])
    new_df = pd.concat([new_df, y])

    #calculate and then add relative_start and relative_length to each row
    new_df['Start'] = pd.to_datetime(new_df['Start'])
    new_df['End'] = pd.to_datetime(new_df['End'])
    new_df['rel_start'] = ((new_df['Start'] - new_df['Start'].min()).dt.seconds/60)
    new_df['rel_length'] = ((new_df['End'] - new_df['Start']).dt.seconds/60)

    return new_df
