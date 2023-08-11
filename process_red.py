import pandas as pd

def process_red_timeline(blue_df, df, start_time):
    # Drop blanks lines from the dataframe
    blue_df.drop(blue_df[blue_df['POO'] == 'None'].index, inplace=True)
    df.drop(df[df['POO'] == 'None'].index, inplace=True)

    # set first line of dataframe to be vul start with empty 'x' as placeholder
    new_df = pd.DataFrame(
        data={'POO': df['POO'], 'Color': 'White', 'Start': start_time['Vul Start'], 'End': start_time['Vul Start']}, index=[0])

    for index, row in blue_df.iterrows():
        label = row['POO']
        first_time = row['Start']
        last_time = row['End']
        x = pd.DataFrame(data=[
            {'POO': label, 'Color': 'Blue', 'Start': first_time, 'End': last_time}], index=[index])
        new_df = pd.concat([new_df, x])

    for index, row in df.iterrows():
        label = row['POO']
        first_time = row['Start']
        last_time = row['End']
        x = pd.DataFrame(data=[
            {'POO': label, 'Color': 'Red', 'Start': first_time, 'End': last_time}], index=[index])
        new_df = pd.concat([new_df, x])


    #Append Knock It Off to end of dataframe
    y = pd.DataFrame(data={'POO':df['POO'], 'Color':'White', 'Start':start_time['Knock It Off'], 'End':start_time['Knock It Off']}, index=[0])
    new_df = pd.concat([new_df, y])

    #calculate and then add relative_start and relative_length to each row
    new_df['Start'] = pd.to_datetime(new_df['Start'])
    new_df['End'] = pd.to_datetime(new_df['End'])
    new_df['rel_start'] = ((new_df['Start'] - new_df['Start'].min()).dt.seconds/60)
    new_df['rel_length'] = ((new_df['End'] - new_df['Start']).dt.seconds/60)

    return new_df