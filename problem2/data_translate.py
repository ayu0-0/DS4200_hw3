import pandas as pd

df = pd.read_csv("problem2/socialMedia.csv")

out = (
    df.groupby(["Platform", "PostType"], as_index=False)["Likes"]
      .mean()
      .rename(columns={"Likes": "AvgLikes"})
)

out["AvgLikes"] = out["AvgLikes"].round(2)

out.to_csv("problem2/socialMediaAvg.csv", index=False)