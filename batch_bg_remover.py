import pathlib
from PIL import Image
import rembg
dir_ = input("enter folder path: ");
paths_jpg = [];#list of save paths
paths_png = [];#list of save paths
og_jpg = [];#list of jpeg file
og_png = [];#list of png file
j = list(pathlib.Path(dir_).glob("*.jpeg"));#list of og jepg
p = list(pathlib.Path(dir_).glob("*.png"));#list of og png
for i in j:#creation of source file paths of jpeg
    a = str(i).lstrip("WindowsPath(").rstrip(")");
    #paths_jpg.append(a);
    og_jpg.append(a);

for i in p:#creation of source,save file paths of png
    a = str(i).lstrip("WindowsPath(").rstrip(")");
    og_png.append(a);
    a = str(i).rstrip(".png");
    a = a + "transparent.png";
    paths_png.append(a);

for i in og_jpg:#creation of save file paths of jpeg
    a = str(i).rstrip(".jpeg");
    a = a + "transparent.png";
    #paths_png.append(a);
    paths_jpg.append(a);

for i in range(len(og_jpg)):#jpeg bg removal
    a = Image.open(og_jpg[i]);
    a = rembg.remove(a);
    a.save(paths_jpg[i]);
    print(f"saved{paths_jpg[i]}");
for i in range(len(og_png)):#png bg removal
    a = Image.open(og_png[i]);
    a = rembg.remove(a);
    a.save(paths_png[i]);
    print(f"saved{paths_png[i]}");