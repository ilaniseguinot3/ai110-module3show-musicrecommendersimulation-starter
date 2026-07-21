"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        {
            "name": "High-Energy Pop",
            "prefs": {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.9,
                "likes_acoustic": False,
            },
        },
        {
            "name": "Chill Lofi",
            "prefs": {
                "favorite_genre": "lofi",
                "favorite_mood": "chill",
                "target_energy": 0.35,
                "likes_acoustic": True,
            },
        },
        {
            "name": "Deep Intense Rock",
            "prefs": {
                "favorite_genre": "rock",
                "favorite_mood": "intense",
                "target_energy": 0.95,
                "likes_acoustic": False,
            },
        },
        {
            "name": "Conflicting Edge Case",
            "prefs": {
                "favorite_genre": "pop",
                "favorite_mood": "sad",
                "target_energy": 0.9,
                "likes_acoustic": False,
            },
        },
    ]

    for profile in profiles:
        print(f"\nProfile: {profile['name']}\n")
        recommendations = recommend_songs(profile["prefs"], songs, k=5)
        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{index}. {song['title']}")
            print(f"   Score: {score:.2f}")
            print(f"   Why: {explanation}")
            print()


if __name__ == "__main__":
    main()
