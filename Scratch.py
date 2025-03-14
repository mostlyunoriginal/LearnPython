import polars as pl
import polars.selectors as cs

mtcars=pl.scan_csv("mtcars_w_names.csv")

q=(
    mtcars
    .unpivot(cs.numeric(),index="car")
)

cars=q.collect()

print(cars)

q=(
    cars.lazy()
    .collect()
    .pivot(
        index="car"
        ,on="variable"
        ,values="value"
        ,aggregate_function="first"
    )
    .lazy()
)

mtcars=q.collect()

print(mtcars)