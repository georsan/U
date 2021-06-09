#cambiar tamaño de ver
options(max.print = 99999)

#datos traidos de git hub
enlace <- 'https://raw.githubusercontent.com/georsan/U/main/Estadistica/abalone.txt'

#datos
datos <- read.table(file=enlace, header=TRUE,sep = ",")

#logitud
longitud <- datos[[2]]

# media poblacional
media <- mean(longitud)

#10000 muestras
muestra <- replicate(10000,sample(longitud,size = 20,replace = TRUE))

#muestras en las que la media esta en el intervalo
med_inter=0

for (i in 1:10000) {

#intervalo
intervalo <- t.test(x=muestra[,i],conf.level = 0.95)$conf.int

#saber si la media esta en el intervalo
if (intervalo[1]<=media && media <= intervalo[2]) {
  med_inter=med_inter+1
}
}
#fraccion
fraccion <- med_inter/10000
