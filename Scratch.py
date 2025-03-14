import polars as pl
import itertools as it

mtcars=pl.read_csv("mtcars.csv")

parms=(
    mtcars
    .group_by("cyl","gear")
    .agg()
)

iterator=[tuple(row) for row in parms.iter_rows(named=False)]

df=it.starmap(
    lambda cyl, gear: (
        mtcars
        .filter(
            (pl.col("cyl")==cyl) & (pl.col("gear")==gear)
        )
      
    )
    ,iterator
)

df=pl.concat(list(df))

print(df)
