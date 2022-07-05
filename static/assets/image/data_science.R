print("i")
print("Hello, World!")
3*(2+5)
x = 10
3*x

a=10
b=3
a+b
a %% b
a %/% b
a/b

c=5
d=16
c>d
c<d
c==d
c!=d

logic_a=c(TRUE,FALSE,0,100)
logic_b=c(FALSE,TRUE,FALSE,TRUE)
!logic_a
logic_a&logic_b
logic_a&&logic_b
logic_a|logic_b
logic_a||logic_b

# Fizzbuzz
for (i in 1:20)
{
  if (i%%15==0)
    cat("FIZZBUZZ ")
  else if (i%%3==0)
    cat("fizz ")
  else if (i%%5==0)
    cat("buzz ")
  else
    cat(i," ")
}

# Fizzbuzz
for (i in 1:20)
{
  if (i%%15==0)
    print("FIZZBUZZ ")
  else if (i%%3==0)
    print("fizz ")
  else if (i%%5==0)
    print("buzz ")
  else
    cat(i," ")
}

sum(1:10)

num = as.integer(readline(prompt = "enter the number: "))
if(num<0){
  print("enter the positive number")
} else{
  sum = 0
  #Use while loop to iterate value till zero
  while(num>0){
    sum = sum+num
    num = num -1
  }
  print(paste("this sum is", sum))
}

num = as.integer(readline(prompt = "enter the number: "))
if(num<0){
  print("enter the positive number")
} else{
 
  #Use while loop to iterate value till zero
    sum = (num *(num+1)) /2;
  print(paste("this sum is", sum))
}

if(num<0){
  print("enter the positive number")
} else{
  
  #Use while loop to iterate value till zero
  sum = (num^2 *(num+1)^2) /2;
  print(paste("this sum is", sum))
}

if(num<0){
  print("enter the positive number")
} else{
  sum=0
  #Use while loop to iterate value till zero
  while(num>0){
    sum=sum+num^3
    num=num-1
  }
  print(paste("this sum is", sum))
}

install.packages("tidyverse")
library(tidyverse)
data=mpg
head(data)
view(data)
names(data)
str(data)
typeof(data$manufacturer)
x=data$displ
y=data$hwy

ggplot(data) +
  geom_point(mapping = aes(x, y))

ggplot(data) +
  geom_point(mapping = aes(x, y, colour=class, size=cyl))

people = c("Djokovic","Federer","Thiem","Zverev", "Barty","Kenin","Halep","Muguruza")
print(people)
str(people)

people = c(1, 2, 3, 4, 5, 6)
print(people)
str(people)

people = c("Djokovic","Federer","Thiem", 1, 2, 3, 4)
print(people)
str(people)

odds = seq(1,20,2)
print(odds)

even =seq(0,20,2)
print(even)

one_to_seventy = 1:70
print(one_to_seventy)

a = c(3,1,4,1,5)
b = c(1,6,1,8,0)
a+b

vowels = c("a","e","i","o","u")
print(vowels[1])
print(length(vowels))
print(vowels[length(vowels)])
print(vowels[2:4])
print(vowels[c(1,3,5)])
print(vowels[1])
print(vowels[2])
print(vowels[10])
print(vowels[-3])



shoe_sizes = c(5.5, 11, 7, 8, 4)
filter = c(TRUE, FALSE, FALSE, FALSE, TRUE)
print(shoe_sizes[filter])
shoe_is_small = (shoe_sizes<6) 
print(shoe_is_small)
print(shoe_sizes[shoe_is_small])
print(shoe_sizes[shoe_sizes>6])

person = list(
  first_name = "Ada",
  job = "Programmer",
  salary = 100000,
  carparking_permit = TRUE
)
print(person)
names(person)
person$first_name
person$job

person[["salary"]]
animals = list("Aardvark","Baboon","Camel")
print(animals)
animals[1]
animals[[1]]
is.list(animals)
is.list(animals[1])
is.list(animals[[1]])


library(tidyverse)
name = c("Nadal","Djokovic","Federer","Medvedev","Theim",
         "Tsitsipas","Zverev","Berrettini","Bautista Agut","Monfils", "Barty","Pliskova","Halep","Osaka","Svitolina",
         "Andreescu","Bencic","Kvitova","Williams","Bertens") 
rank = c(1:10,1:10)
age = c(33,32,38,23,26,21,22,23,31,33,
        23,27,28,22,25,19,22,29,38,28)
height = c(1.85,1.88,1.85,1.98,1.85,1.93,1.98,1.96,1.83,1.93,
           1.66,1.86,1.68,1.80,1.74,1.70,1.75,1.82,1.75,1.82)
weight = c(85,77,85,83,79,89,90,95,75,85, 62,72,60,69,60,60,63,68,72,74) 
gender = c(rep("M",10),rep("F",10))
tennis = tibble(name,rank,age,height,weight) 
print(tennis)
names(tennis)
summary(tennis)
summary(tennis $age)

tennis = tribble(
  ~name, ~rank, ~age, ~height, ~weight, ~gender, 
  "Nadal",
  "Djokovic",
  "Federer",
  "Medvedev",
  "Theim",
  1, 33, 1.85, 85, "M", 2, 32, 1.88, 77, "M", 3, 38, 1.85, 85, "M", 4, 23, 1.98, 83, "M", 5, 26, 1.85, 79, "M",
  "Tsitsipas",
  "Zverev",
  "Berrettini",
  "Bautista Agut", 9, 31, 1.83, 75, "M", "Monfils", 10, 33, 1.93, 85, "M", "Barty", 1, 23, 1.66, 62, "F",
  6, 21, 1.93, 89, "M",
  7, 22, 1.98, 90, "M",
  8, 23, 1.96, 95, "M",

  "Pliskova", 2, 27, 1.86, 72, "F", "Halep", 3, 28, 1.68, 60, "F",
  "Osaka",          4, 22, 1.80, 69, "F",
  "Svitolina",
  "Andreescu",
  "Bencic",
  "Kvitova",
  "Williams",
  "Bertens",
  5, 25, 1.74, 60, "F",
  6, 19, 1.70, 60, "F",
  7, 22, 1.75, 63, "F",
  8, 29, 1.82, 68, "F",
  9, 38, 1.75, 72, "F",
  10, 28, 1.82, 74, "F"
)
print(tennis)
nrow(tennis)
ncol(tennis)
colnames(tennis) 
summary(tennis)
View(tennis) # with capital V

tennis[1,"name"]
tennis[1,"age"]
tennis[1,]
tennis[,"height"]
tennis$height

ggplot(tennis, aes(y=height)) +
  geom_boxplot()

ggplot(tennis, aes(x=gender, y=height)) + geom_boxplot()

ggplot(tennis, aes(y=age)) +
  geom_boxplot()

ggplot(tennis, aes(x=gender, y=age)) + geom_boxplot()

ggplot(tennis, aes(y=age)) +
  geom_boxplot() + coord_flip()

ggplot(tennis, aes(x=gender, y=age)) + geom_boxplot() + coord_flip()


