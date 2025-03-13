import polars as pl

mtcars=pl.scan_csv("mtcars.csv")

q=(
    mtcars
    .with_columns(
        pl.when(pl.col("mpg")<10).then(pl.lit("very bad"))
        .when(pl.col("mpg")<15).then(pl.lit("bad"))
        .when(pl.col("mpg")<20).then(pl.lit("okay"))
        .when(pl.col("mpg")<25).then(pl.lit("good"))
        .otherwise(pl.lit("great"))
        .alias("mpg.cat")
    )
    .sort("mpg",descending=True)
)

df=q.collect()

print(df)
