# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender is designed for classroom exploration and simple demonstration. It suggests songs that may fit a user’s stated preferences for genre, mood, energy, and acoustic style. It assumes the user has a few clear preferences and uses those to rank a small catalog of songs.

---

## 3. How the Model Works  

This recommender is a simple content-based system. It looks at the features of each song, such as genre, mood, energy, and tempo, and compares them with the preferences stored in a user profile. If a user tends to like songs that are calm, upbeat, and pop-oriented, the model gives higher scores to songs with similar qualities.

This is similar to the content-based side of how Spotify or YouTube recommend music, but it is simpler than the full systems those companies use. In real streaming platforms, collaborative filtering is also important: it studies patterns across many users, such as the fact that people who liked one set of songs often also liked another. Content-based filtering, on the other hand, relies more on the actual properties of the songs themselves. Both methods have strengths and weaknesses. Collaborative filtering can surface surprising recommendations, but it may struggle with new songs or users. Content-based filtering works well for new items, but it can be narrower and more predictable. The strongest systems often combine both approaches.

---

## 4. Data  

The model uses a small catalog of 18 songs from a CSV file. Each song includes basic features such as genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset is intentionally small and does not include full listening history, lyrics, or artist popularity, so it cannot capture the full range of real music taste.

---

## 5. Strengths  

The system works well for clear, simple preferences. It gives sensible results for users who want songs that match a specific genre, mood, or energy level. It also produces understandable explanations, which makes the recommendation process easier to inspect and discuss.

---

## 6. Limitations and Bias 

This recommender can create a filter bubble because it relies heavily on a small set of explicit features such as genre, mood, energy, and acousticness. In my experiments, profiles that matched a clear genre label often received very similar top results, even when the mood or energy fit was not ideal, which means the system can over-prioritize obvious labels and under-value more subtle matches. It also does not consider broader context such as listening history, artist familiarity, or cultural taste, so it may favor users who fit the dataset's most common patterns. Because the catalog is relatively small, the recommendations can feel repetitive and may not reflect the full range of a listener's preferences.

---

## 7. Evaluation  

I tested the recommender with four different user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a Conflicting Edge Case with a pop genre preference but a sad mood. I looked for whether the top recommendations matched the user’s stated genre, mood, and energy preferences, and whether the explanations made sense in plain language.

The High-Energy Pop profile produced upbeat songs such as Sunrise City and Gym Hero, which made sense because the system strongly rewards pop matches and high-energy songs. The Chill Lofi profile shifted toward calmer, more acoustic tracks like Library Rain and Midnight Coding, which also felt reasonable because the system gave a boost to acoustic preference and lower energy. The Deep Intense Rock profile mainly surfaced Storm Runner and other high-energy tracks, which makes sense because the model strongly favors songs that fit the target energy and genre. The Conflicting Edge Case was the most surprising profile, because a user who wanted pop but also had a sad mood still received mostly energetic pop-like songs. That happened because the model gives a strong early boost to genre and energy, so a mismatch in mood can be hidden by the more obvious pop signal.

A key comparison is that the High-Energy Pop and Chill Lofi profiles produced very different results even though both profiles had a clear style. That makes sense because the system is really testing whether the songs match the user’s energy and acousticness as well as the genre label. Another important comparison is that Gym Hero kept showing up in multiple lists, especially for happy or pop-oriented profiles. In plain language, that happens because the song is a strong match for the “pop” label and also has an appealing energy level, so it can keep rising to the top even when the user is not asking for the exact same mood.

---

## 8. Future Work  

I would improve this model by adding more features such as tempo, valence, or artist similarity. I would also test more balanced weights so genre does not dominate the ranking so strongly. A larger dataset and a more diverse set of user profiles would help the system make better and less repetitive recommendations.

---

## 9. Personal Reflection  

My biggest learning moment was realizing that a recommender can feel smart even when it is using very simple rules. A small set of hand-written weights can produce results that look reasonable, but they can still miss the deeper meaning behind a user’s taste. That was especially clear when one song kept appearing for pop-like profiles even when the mood did not match.

Using AI tools helped me move faster by suggesting code structure, scoring ideas, and ways to explain the logic. I still had to double-check the output carefully, especially when the AI suggested changes to the scoring math, because small mistakes in weights can change the ranking a lot. What surprised me most was how quickly a simple algorithm could start to feel like a real recommendation system once it had a score, an explanation, and a ranked list.

If I extended this project, I would try a larger dataset, more nuanced scoring, and a way to include user history or artist familiarity. I would also want to test whether the same recommendations still feel good when the profile becomes more complex and less obvious.
