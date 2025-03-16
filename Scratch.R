library(tidyverse)

cyl<-mtcars %>%
  distinct(cyl) %>%
  arrange(cyl) %>%
  pull()