library(tidyverse)

filter(mtcars,cyl==6) %>% nrow()
filter(mtcars,hp>150) %>% nrow()