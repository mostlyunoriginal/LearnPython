import polars as pl

mtcars=pl.read_csv("mtcars.csv")

parms=(
    mtcars
    .group_by("cyl","gear")
    .agg()
)

iterator=list(parms.iter_rows(named=True))

df=map(
    lambda x: (
        mtcars
        .filter(
            (pl.col("cyl")==x['cyl']) & (pl.col("gear")==x['gear'])
        )
    )
    ,iterator
)

df=pl.concat(list(df))

print(df)
