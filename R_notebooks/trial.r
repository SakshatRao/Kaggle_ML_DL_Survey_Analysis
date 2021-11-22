names <- c('a', 'b', 'c')
vals <- c(a = 1, b = 2, c = 3)
temp <- as.data.frame(do.call(cbind, list(names, vals)))
colnames(temp) <- NULL
rownames(temp) <- 1:dim(temp)[1]
print(typeof(temp))
print(temp)