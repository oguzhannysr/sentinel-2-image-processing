import spectral
import pycm as cm

def classification(rasterFilePath, trainPath, testPath, outputPath):
  
  img = spectral.envi.open(rasterFilePath).load()
  train = spectral.open_image(trainPath).read_band(0)
  classes1 = spectral.create_training_classes(img,train)
  gmlc = spectral.GaussianClassifier(classes1)
  clmap = gmlc.classify_image(img)
  d1 = imshow(classes=clmap)

  test=spectral.open_image(testPath).read_band(0)
  classes3 = spectral.create_training_classes(img,dogrulama)
  gmlc2 = spectral.GaussianClassifier(classes3)
  clmap2 = gmlc2.classify_image(img)  
  d2 = imshow(classes=clmap2)

  spectral.envi.save_classification(outputPath +"s1.hdr", clmap)
  spectral.envi.save_classification(outputPath +"s2.hdr", clmap2)
  train=clmap2.flatten()
  test=clmap.flatten()  
  
  hata_matrisi=cm.ConfusionMatrix(train,test) 
  print(hata_matrisi) 
  
