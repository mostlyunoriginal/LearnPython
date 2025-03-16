import polars as pl

mtcars=pl.scan_csv("mtcars_w_names.csv")

alist=[mtcars]

astring="BOOM"
anotherstring=f"here i've insterted a bom-{astring}"
print(anotherstring)

abiginteger=1_000_000_000
print(abiginteger)
teststring=f"hmmm...{abiginteger}"
print(teststring)

print(anotherstring.title())

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

cyl=(
    mtcars
    .get_column("cyl")
    .unique()
    .sort()
)

df=pl.DataFrame({
    "test": ['a','b','c']
}).with_columns(
    pl.when(pl.col("test")=="a").then(pl.lit("astring")).otherwise("test")
)

print(df)