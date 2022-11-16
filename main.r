x = c(1,2,3)
x

y = seq(from= 2,length=3,by=3)
y

x+y 
x-y

x[1]
y[2:3]
y[2:2]
x[-2]

y[-c(1,2)]

z = matrix(seq(1,12),3,4)
z

z[1:2,2:3]
z[,1:3]
z[,4]
z[,4,drop=FALSE]

dim(z)

ls

#Generating random uniform data 
a = runif(50)

#Generating random normal data
b = rnorm(50)


plot(a,b)
plot(a,b,xlab='Random uniform',ylab='Random normal',pch='*',col='blue')

par(mfrow=c(2,1))
hist(a)
hist(b)
