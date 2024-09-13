import lyricsgenius
from config import GENIUS_API_TOKEN

genius = lyricsgenius.Genius(GENIUS_API_TOKEN)

def clean_lyrics(lyrics):
    lines = lyrics.split('\n')
    cleaned_lines = []
    for line in lines:
        if "You might also like" in line:
            break
        if not line.startswith('Embed') and not 'Contributors' in line and not line.isdigit():
            cleaned_lines.append(line)
    return '\n'.join(cleaned_lines)

def complete_lyric(text):
    try:
        song = genius.search_song(text)
        if song:
            cleaned_lyrics = clean_lyrics(song.lyrics)
            return song.artist, song.title, cleaned_lyrics
        else:
            return None, None, "Sorry, I couldn't find the lyrics for this song."
    except Exception as e:
        return None, None, f"An error occurred: {e}"