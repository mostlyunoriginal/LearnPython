library(tidyverse)
library(dtplyr,warn.conflicts=F)
library(hms)

start<-Sys.time()

big<-data.table::fread("big.csv")

varnames<-setdiff(colnames(big),"id")

rows_dt<-lazy_dt(big) %>%
  group_by(id) %>%
  summarize(across(all_of(varnames),mean),.groups="keep") %>%
  filter(if_any(all_of(varnames),~.x>.4)) %>%
  collect() %>%
  nrow()

end<-Sys.time()

elapsed<-(end-start)

print(str_glue("{rows_dt} rows returned\nelapsed time for query: {as_hms(elapsed)}"))
