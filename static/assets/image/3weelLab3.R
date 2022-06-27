library(tidyverse)
install.packages("rvest") #used to scrape data from web
library(rvest)
starwars <- read_html("https://rvest.tidyverse.org/articles/starwars.html")
starwars

# Then find elements that match a css selector or XPath expression

# using html_elements(). In this example, each <section> corresponds

# to a different film

films <- starwars %>% html_elements("section")

films

title <- films %>% 
  html_element("h2") %>% 
  html_text2()
title

episode <- films %>% 
  html_element("h2") %>% 
  html_attr("data-id") %>% 
  readr::parse_integer()
episode

# If the page contains tabular data you can convert it directly to a data frame with html_table():



html <- read_html("https://en.wikipedia.org/w/index.php?title=The_Lego_Movie&oldid=998422565")

html

html %>% 
  
  html_element(".tracklist") %>% 
  
  html_table()

install.packages("tidyr")
library(tidyr)
install.packages("stringr")
library(stringr)
install.packages("lubridate")
library(lubridate, warn.conflicts = FALSE)
url = "http://espn.go.com/nfl/superbowl/history/winners" 
page = read_html(url)
page

sb_table = html_nodes(page, 'table')
sb = html_table(sb_table)[[1]]
sb

sb = sb[c(-1,-2),]
names(sb) = c("number", "date", "site", "result")
sb = as_tibble(sb)
sb


mutate(sb,number=1:nrow(sb))
mutate(sb,date=mdy(date))
separate(sb,site,c("stadium","city",NA),sep='[()]')

separate(sb,result,c("winner","loser"),sep=', ')

pattern = ' \\d+$' 
separate(sb,result,c("winner","loser"),sep=', ') %>%
  mutate(winnerscore=as.numeric(str_extract(winner,pattern))) %>% 
  mutate(winner=gsub(pattern,"",winner))

# Pipe
pattern = ' \\d+$'
sb %>%
  mutate(number=1:nrow(sb)) %>%
  mutate(date=mdy(date)) %>% 
  separate(site,c("stadium","city",NA),sep='[()]') %>% 
  separate(result,c("winner","loser"),sep=', ') %>% 
  mutate(winnerscore=as.numeric(str_extract(winner,pattern))) %>% 
  mutate(winner=gsub(pattern,"",winner))

#loser
sb %>%
  mutate(number=1:nrow(sb)) %>%
  mutate(date=mdy(date)) %>% 
  separate(site,c("stadium","city",NA),sep='[()]') %>% 
  separate(result,c("loser","winner"),sep=', ') %>% 
  mutate(loserscore=as.numeric(str_extract(loser,pattern))) %>% 
  mutate(loser=gsub(pattern,"",loser))

library(lubridate)
wday(today(),label=TRUE)


dmy(01032020)
dmy(28022020)  
dmy(01032020) - dmy(28022020)

tyson = dmy("12/08/1988")






