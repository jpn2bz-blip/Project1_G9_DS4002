import lyricsgenius
import csv
import textwrap
import pandas as pd

# Genius setup
genius = lyricsgenius.Genius("I6EMYtVeNvcoWxxt2naMjFwN4nbOlke09h09w8iA1--R1C4suUDnI9-50YqQMHzA")

# Genius API setup
genius.remove_section_headers = True  # remove [Chorus], [Verse] tags if present


def fetch_album(songs, artist, album_name, filename):
    """
    Fetch lyrics for a list of songs and save to CSV with one row per song.
    """
    data = []
    for title in songs:
        print(f"Fetching: {title} ...")
        song = genius.search_song(title, artist)
        if song and song.lyrics:
            # Clean up and join into one string
            lines = [line.strip() for line in song.lyrics.split("\n") if line.strip()]
            full_lyrics = " ".join(lines)

            data.append({
                "artist": song.artist,
                "album": album_name,
                "song": song.title,
                "lyrics": full_lyrics
            })
        else:
            data.append({
                "artist": artist,
                "album": album_name,
                "song": title,
                "lyrics": "Not found"
            })

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"✅ Saved {len(df)} songs to {filename}")


# ---------------- Amy Winehouse ----------------
back_to_black_songs = [
    "Rehab",
    "You Know I’m No Good",
    "Me & Mr Jones",
    "Just Friends",
    "Back to Black",
    "Love Is a Losing Game",
    "Tears Dry on Their Own",
    "Wake Up Alone",
    "Some Unholy War",
    "He Can Only Hold Her",
    "Addicted"
]
fetch_album(back_to_black_songs, "Amy Winehouse", "back_to_black", "back_to_black_lyrics.csv")

reputation_songs = [
    "...Ready for It?",
    "End Game",
    "I Did Something Bad",
    "Don't Blame Me",
    "Delicate",
    "Look What You Made Me Do",
    "So It Goes…",
    "Gorgeous",
    "Getaway Car",
    "King of My Heart",
    "Dancing With Our"]
fetch_album(reputation_songs, "Taylor Swift", "Reputation", "Reputation_lyrics.csv")


sabrina_album = [
    "Manchild",
    "Tears",
    "My Man on Willpower",
    "Sugar Talking",
    "We Almost Broke Up Again Last Night",
    "Nobody's Son",
    "Never Getting Laid",
    "When Did You Get Hot?",
    "Go Go Juice",
    "Don't Worry I'll Make You Worry",
    "House Tour",
    "Goodbye"
]
fetch_album(sabrina_album, "Sabrina Carpenter", "Man's Best Friend", "Man's_Best_Friend_lyrics.csv")