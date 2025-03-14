library(dplyr)

parms<-distinct(mtcars,cyl,gear)

list<-pmap(
  parms
  ,function (...){
    parms<-rlang::dots_list(...)
    mtcars %>%
      dplyr::filter(cyl==parms$cyl & gear==parms$gear) 
  }
)

df<-list_rbind(list)

print(df)