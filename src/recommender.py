import csv
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []
        for song in self.songs:
            score, _ = self._score_song(user, song)
            scored_songs.append((score, song))

        scored_songs.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        score, reasons = self._score_song(user, song)
        if not reasons:
            return f"This song scored {score:.2f} because it is a reasonable match for your profile."
        return f"This song scored {score:.2f} because it {', '.join(reasons)}."

    def _score_song(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        score = 0.0
        reasons: List[str] = []

        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0
            reasons.append("matches your favorite genre")

        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0
            reasons.append("matches your favorite mood")

        energy_gap = abs(song.energy - user.target_energy)
        energy_similarity = max(0.0, 1.0 - energy_gap)
        score += energy_similarity
        reasons.append(f"has energy close to your target ({energy_similarity:.2f})")

        if user.likes_acoustic and song.acousticness >= 0.6:
            score += 0.5
            reasons.append("fits your acoustic preference")
        elif not user.likes_acoustic and song.acousticness <= 0.3:
            score += 0.2
            reasons.append("stays relatively non-acoustic")

        return score, reasons


def load_songs(csv_path: str) -> List[Dict]:
    """Load song records from a CSV file into a list of dictionaries."""
    print(f"Loading songs from {csv_path}...")
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        songs = []
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against a user profile and return the score with reasons."""
    favorite_genre = str(user_prefs.get("favorite_genre", "")).lower()
    favorite_mood = str(user_prefs.get("favorite_mood", "")).lower()
    target_energy = float(user_prefs.get("target_energy", 0.0))
    likes_acoustic = bool(user_prefs.get("likes_acoustic", False))

    score = 0.0
    reasons: List[str] = []

    if str(song.get("genre", "")).lower() == favorite_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if str(song.get("mood", "")).lower() == favorite_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_gap = abs(float(song.get("energy", 0.0)) - target_energy)
    energy_similarity = max(0.0, 1.0 - energy_gap)
    score += energy_similarity
    reasons.append(f"energy similarity ({energy_similarity:.2f})")

    acousticness = float(song.get("acousticness", 0.0))
    if likes_acoustic and acousticness >= 0.6:
        score += 0.5
        reasons.append("acoustic preference")
    elif not likes_acoustic and acousticness <= 0.3:
        score += 0.2
        reasons.append("lower acousticness")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top-k recommendations with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = f"This song fits because it {'; '.join(reasons)}."
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
