library(tidyr)

cars<-rownames_to_column(mtcars,"car") %>%
  pivot_longer(
    cols=where(is.numeric)
    ,names_to="variable"
    ,values_to="value"
  )

print(cars)

mtcars<-cars %>%
  pivot_wider(
    id_cols=car
    ,names_from="variable"
    ,values_from="value"
  )

print(mtcars)