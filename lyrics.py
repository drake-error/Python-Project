import time
import sys
def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()  # Move to the next line after finishing the lyric
def print_lyrics():
    lyrics = [

        "Haathon ko sambhaale mere haathon mein",
        "Kaise haathon ko sambhaale mere haathon mein?",
        "Jab tak neend na aaye in lakeeron mein" ,
        "Baatein hon...",

        "haan. . ." ,
    ]

    # per-line delay in seconds after each lyric line is typed
    delays = [2.0, 1.8, 2.1, 2.4, 1.7]
    print("\n🎧 Now Playing: ARZ KIYA HAI - (partial)\n")
    time.sleep(1.0)  # Initial delay before starting
    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])
print_lyrics()