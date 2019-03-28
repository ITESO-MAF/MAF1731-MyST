
# -- Remover todos los objetos del "Environment"
rm(list = ls())

# -- los 0s aceptados antes de expresas una cifra en notacion cientifica
options("scipen"=100, "digits"=4)

# -- Cargas librerias a utilizar
suppressMessages(library(Quandl)) # Descargar Precios
suppressMessages(library(ROI))    # Optimizacion para portafolio
suppressMessages(library(plotly)) # Graficas interactivas

# -- Cargar el token de QUANDL
Quandl.api_key("4WLCk2ZUAMAPPyowvAYr")
Capital_Inicial <- 10000

# -- Funcion para descagar precios
Bajar_Precios <- function(Columns, Tickers, Fecha_In, Fecha_Fn) {
  Datos <- Quandl.datatable("WIKI/PRICES", qopts.columns=Columns, ticker=Tickers,
                            date.gte=Fecha_In, date.lte=Fecha_Fn)
    return(Datos)
}

# -- Crear nombres de archivos
archivos  <- c()
Tickers   <- list()
Datos_ETF <- list()
for(i in 1:13) {
  archivos[i]    <- paste("IAK_holdings_", i, ".csv", sep="")
  Datos_ETF[[i]] <- na.omit(data.frame(read.csv(paste0("Datos/", archivos[i]),
                                                row.names=NULL, skip=10, stringsAsFactors=FALSE)))
}

# -- Fecha inicial y fecha final
fs <- c("2017-03-01", "2018-03-01")
cs <- c("date", "open", "high", "low", "close", "adj_close")
Precios_ETF <- list()

# -- Obtener una lista de los Tickers Unicos en todo el periodo
for(i in 1:length(archivos)){
  Tickers[[i]] <- unique(Datos_ETF[[i]]$Ticker)
}
TodosTickers <- unique(unlist(Tickers))

# -- Bajar todos los precios
for(i in 1:length(TodosTickers)) {
  print(i)
  Precios_ETF[[i]] <- Bajar_Precios(Columns=cs, Ticker=TodosTickers[i], Fecha_In=fs[1], Fecha_Fn=fs[2])
}

# -- Cambiar el orden de los datos que previamente descargamos
for(i in 1:length(TodosTickers)){
  Precios_ETF[[i]] <- Precios_ETF[[i]][order(Precios_ETF[[i]][,1]), ]
}

# -- Encontrar tickers de la misma longitud
longitudes <- c()

for(i in 1:length(Precios_ETF)){
  longitudes[i] <- length(Precios_ETF[[i]]$date)
}

maximo <- max(longitudes)
completos   <- which(longitudes == maximo)
Precios_ETF <- Precios_ETF[completos]
names(Precios_ETF) <- TodosTickers[completos]

# -- Grafica con doble eje Y en plot.ly

serie1 <- Precios_ETF[["CB"]]$adj_close
serie2 <- Precios_ETF[["AIG"]]$adj_close

# -- Asegurarse que son las mismas fechas para todos los tickers

for(i in 1:(length(Precios_ETF)-1)) {
  if(!any(Precios_ETF[[i]]$date == Precios_ETF[[i+1]]$date)){
    print("Hubo 1 diferente, no usar las mismas fechas")
  } else {
    fechas <- Precios_ETF[[1]]$date
  }
}

# -- 

ejey <- list(
  tickfont = list(color = "red"),
  overlaying = "y",
  side = "right",
  title = "second y axis",
  type='log'
)

y1 <- Precios_ETF[[1]]$adj_close[which(Precios_ETF[[1]]$date == fechas[4])]

p <- plot_ly() %>%
  add_lines(x = ~fechas, y = ~serie1, name = "ETF") %>%
  layout(
    shapes = list(type='line', x0 = fechas[14], x1 = fechas[14], y0 = 0, y1 = y1,
                  line=list(dash='dot')),
    title = "Rebalanceo del ETF", yaxis2 = ejey,
    xaxis = list(title="x"),
    yaxis2 = list(type='log', autorange=T)
  )

  p
  

