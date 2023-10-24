# Using a small dataframe as a map for values

This works best if you can maintain the invariant of unique keys (e.g. you have only one of each `market_ticker` for a given column), but could also work I believe if you have a few repeat values! Would just need a secondary column to use as a conflict resolution keys.

Was originally trying some fancy `.update()` and `.merge_asof()`, `.set_index()` with `.sort_index()` after combing through SO post after SO post, the answer ended up being:

```python
likely_bets = df1.merge(df2, on="market_ticker")
```
