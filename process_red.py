import pandas as pd

def process_red_timeline(df, start_time):
    # Drop blanks lines from the dataframe
    df.drop(df[df['Label'] == None].index, inplace=True)

    # set first line of dataframe to be vul start with empty 'x' as placeholder
    new_df = pd.DataFrame(
        data={'Label': df['Label'], 'Color': 'Red', 'Start': start_time['Vul Start'],
              'End': start_time['Vul Start']}, index=[0])

    for index, row in df.iterrows():
        label = row['Label']
        first_time = row['Start']
        last_time = row['End']
        x = pd.DataFrame(data=[
            {'Label': label, 'Color': 'Red', 'Start': first_time, 'End': last_time}
        ], index=[index])
        new_df = pd.concat([new_df, x])

    #Append Knock It Off to end of dataframe
    y = pd.DataFrame(data={'Label':df['Label'], 'Color':'White', 'Start':start_time['Knock It Off'], 'End':start_time['Knock It Off']}, index=[0])
    new_df = pd.concat([new_df, y])

    #calculate and then add relative_start and relative_length to each row
    new_df['Start'] = pd.to_datetime(new_df['Start'])
    new_df['End'] = pd.to_datetime(new_df['End'])
    new_df['rel_start'] = ((new_df['Start'] - new_df['Start'].min()).dt.seconds/60)
    new_df['rel_length'] = ((new_df['End'] - new_df['Start']).dt.seconds/60)

    return new_df