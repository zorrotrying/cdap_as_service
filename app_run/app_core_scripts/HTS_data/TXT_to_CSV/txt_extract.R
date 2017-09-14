cdap_service_fun<-function(foldname='./Dataset'){
  ##folders and txts
  filelist = list.files(foldname, pattern = "\\.txt$")
  
  ##define result and its first row
  result = matrix(nrow = 300, ncol = 28)
  result[1,] = c("Row",paste("Col",1:24,sep = ""),"File name","Date","Time")
  
  ##data of the result
  index = 2
  for(i in 1:length(filelist)){
    filename = paste(foldname,filelist[i],sep="/")
    data_test = read.table(filename, fill = TRUE,header = F, stringsAsFactors= F )
    num_row = dim(data_test)[1]
    start_row = 17
    while(start_row<num_row){
      data_sub = data_test[start_row:(start_row+4),]
      temp = c(t(as.matrix(data_sub)))
      result[index,1:25] = temp
      result[index,26] = filelist[i]
      result[index,27] = data_test[2,2]
      result[index,28] = paste(data_test[2,4],data_test[2,5],sep = "")
      index = index + 1
      start_row = start_row+5
    }
  }
  ##write
  result = result[1:(index-1),]
  write.table(result,paste(foldname,"result.csv",sep = "/"),col.names = F,row.names = F,sep = ",")
  return(paste(foldname,"result.csv",sep = "/"))
}