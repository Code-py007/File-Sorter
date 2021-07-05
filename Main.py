import shutil
import os

imageDir = 'Images'
exeDir = 'Exe files'
pdfDir = 'PDF Files'
txtDir = 'Txt Files'
msiDir = 'MSI Files'
zipDir = 'ZIP Files'
pyDir = 'Python Files'
videosDir = 'Videos'
musicDir = 'Music Files'
htmlDir = 'HTML Files'
wordDir = 'Word Files'
pptDir = 'PPT Files'
isoDir = 'iso files'
FontFiles = 'TFF and OFF files'
jarFiles = 'jar files'
rarDir = 'Rar Files'

def main():
    print ("starting")

    os.makedirs ('Images')
    print ("Created Images folder\n")
    os.makedirs ('Exe files')
    print ("Created EXE folder\n")
    os.makedirs ('PDF Files')
    print ("Created PDF folder\n")
    os.makedirs ('Txt Files')
    print ("Created Txt folder\n")
    os.makedirs ('MSI Files')
    print ("Created Msi folder\n")
    os.makedirs ('ZIP Files')
    print ("Created ZIP folder\n")
    os.makedirs ('Python Files')
    print ("Created Python folder\n")
    os.makedirs ('Videos')
    print ("Created Videos folder\n")
    os.makedirs ('Music Files')
    print ("Created Music folder\n")
    os.makedirs ('HTML Files')
    print ("Created HTML folder\n")
    os.makedirs('jar files')
    print ("Created Jar folder\n")
    os.makedirs('TFF and OFF files')
    print("Created Fonts folder\n")
    os.makedirs ('iso files')
    print("Created ISO folder\n")
    os.makedirs ('Rar Files')
    print("Created Rar folder\n")

    dirName = os.path.dirname (os.path.realpath (__file__))
    for root,dirs,files in os.walk(dirName):
        for file in files:

            if file.endswith('.txt'):
                path = os.path.join(root,file)
                shutil.move(path,txtDir)
                print("Sorted: " + path)

            elif file.endswith('.ttf'):
                path = os.path.join(root,file)
                shutil.move(path,FontFiles)
                print("Sorted: "+path)

            if file.endswith('.pdf'):
                path = os.path.join(root,file)
                shutil.move(path,pdfDir)
                print("Sorted: " + path)

            elif file.endswith('.exe'):
                path = os.path.join(root,file)
                shutil.move(path,exeDir)
                print("Sorted: " + path)

            elif file.endswith('.msi'):
                path = os.path.join(root,file)
                shutil.move(path,msiDir)
                print("Sorted: "+path)

            elif file.endswith('.jpeg'):
                path = os.path.join(root,file)
                shutil.move(path,imageDir)
                print("Sorted: "+path)

            elif file.endswith('.png'):
                path = os.path.join(root,file)
                shutil.move(path,imageDir)
                print("Sorted: "+path)

            elif file.endswith('.jpg'):
                path = os.path.join(root,file)
                shutil.move(path,imageDir)
                print("Sorted: "+path)

            elif file.endswith('.MP4'):
                path = os.path.join(root,file)
                shutil.move(path,videosDir)
                print("Sorted: "+path)

            elif file.endswith('.mp3'):
                path = os.path.join(root,file)
                shutil.move(path,musicDir)
                print("Sorted: "+path)

            elif file.endswith('.wav'):
                path = os.path.join(root,file)
                shutil.move(path,musicDir)
                print("Sorted: "+path)

            elif file.endswith('.zip'):
                path = os.path.join(root,file)
                shutil.move(path,zipDir)
                print("Sorted: "+path)

            elif file.endswith('.rar'):
                path = os.path.join(root,file)
                shutil.move(path,rarDir)
                print("Sorted: "+path)

            elif file.endswith('7z'):
                path = os.path.join(root,file)
                shutil.move(path,zipDir)
                print("Sorted: "+path)

            elif file.endswith('.jfif'):
                path = os.path.join(root,file)
                shutil.move(path,imageDir)
                print("Sorted: "+path)

            elif file.endswith('.html'):
                path = os.path.join(root,file)
                shutil.move(path,htmlDir)
                print("Sorted: "+path)

            elif file.endswith('.pptx'):
                path = os.path.join(root,file)
                shutil.move(path,pptDir)
                print("Sorted: "+path)

            elif file.endswith('.docx'):
                path = os.path.join(root,file)
                shutil.move(path,wordDir)
                print("Sorted: "+path)

            elif file.endswith('.iso'):
                path = os.path.join(root,file)
                shutil.move(path,isoDir)
                print("Sorted: "+path)

            elif file.endswith('.jar'):
                path = os.path.join(root,file)
                shutil.move(path,jarFiles)
                print("Sorted: "+path)

            else:
                file.endswith('.*')
                print("UnAcceptable File Format Found\nMoving to next File :D")


if __name__ == '__main__':
     main()
