import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('games.csv')

# Identify unique game IDs
unique_game_ids = df['game_id'].unique()

# Calculate the number of rows per chunk
total_games = len(unique_game_ids)
chunks = 5
games_per_chunk = total_games // chunks

# Split the game IDs into smaller chunks
split_game_ids = [unique_game_ids[i*games_per_chunk:(i+1)*games_per_chunk] for i in range(chunks)]

# Split the DataFrame into smaller chunks based on game IDs
split_data = [df[df['game_id'].isin(game_ids)] for game_ids in split_game_ids]

# Save each chunk to a separate CSV file
for i, chunk in enumerate(split_data):
    chunk.to_csv(f'chunk_{i}.csv', index=False)
