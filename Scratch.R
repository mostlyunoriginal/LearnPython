library(tidyverse)

cyl<-mtcars %>%
  distinpuct(cyl) %>%
  arrange(cyl) %>%
  pull()