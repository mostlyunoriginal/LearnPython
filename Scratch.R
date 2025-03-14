library(dplyr)

parms<-distinct(mtcars,cyl) %>%
  pull()

list<-map(
  parms
  ,function (x){
    mtcars %>%
      dplyr::filter(cyl==x) %>%
      arrange(desc(mpg))
  }
)

df<-list_rbind(list)

print(df)