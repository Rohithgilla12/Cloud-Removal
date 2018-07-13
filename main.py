import tkinter
from tkinter import filedialog as fd
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from PIL import Image
import numpy
import tifffile
from sklearn.linear_model import LinearRegression


class Gills:
    def __init__(self):
        win = tkinter.Tk()
        win.title("Cloud Removal")
        self.filename = []
        self.layer1 = ""
        self.layer2 = ""
        self.layer3 = ""
        self.layer4 = ""
        self.layer5 = ""
        self.layer6 = ""
        self.layer7 = ""
        self.layer8 = ""
        self.layer9 = ""
        self.layer10 = ""
        self.layer11 = ""
        self.layer12 = ""
        self.layer13 = ""
        self.hyper = ""

        # win.geometry("640x480")
        def layer1():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer1 = file

        def layer2():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer2 = file

        def layer3():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer3 = file

        def layer4():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer4 = file

        def layer5():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer5 = file

        def layer6():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer6 = file

        def layer7():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer7 = file

        def layer8():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer8 = file

        def layer9():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer9 = file

        def layer10():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer10 = file

        def layer11():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer11 = file

        def layer12():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer12 = file

        def layer13():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.layer13 = file

        def hyperspec():
            file = fd.askopenfilename()
            self.filename.append(file)
            self.hyper = file

        def submit():
            win.destroy()

        layer1 = Button(win, text="Layer1", command=layer1)
        layer1.grid(column=0, row=1)
        layer2 = Button(win, text="Layer2", command=layer2)
        layer2.grid(column=1, row=1)
        layer3 = Button(win, text="Layer3", command=layer3)
        layer3.grid(column=0, row=2)
        layer4 = Button(win, text="Layer4", command=layer4)
        layer4.grid(column=1, row=2)
        layer5 = Button(win, text="Layer5", command=layer5)
        layer5.grid(column=0, row=3)
        layer6 = Button(win, text="Layer6", command=layer6)
        layer6.grid(column=1, row=3)
        layer7 = Button(win, text="Layer7", command=layer7)
        layer7.grid(column=0, row=4)
        layer8 = Button(win, text="Layer8", command=layer8)
        layer8.grid(column=1, row=4)
        layer9 = Button(win, text="Layer8A", command=layer9)
        layer9.grid(column=0, row=5)
        layer10 = Button(win, text="Layer9", command=layer10)
        layer10.grid(column=1, row=5)
        layer11 = Button(win, text="Layer10", command=layer11)
        layer11.grid(column=0, row=6)
        layer12 = Button(win, text="Layer11", command=layer12)
        layer12.grid(column=1, row=6)
        layer13 = Button(win, text="Layer12", command=layer13)
        layer13.grid(column=0, row=7)
        # Hyper Spectral
        hyper = Label(text="Hyper Spectral : ")
        hyper.grid(column=0, row=8)
        hyperfile = Button(win, text="Hyper Spectral", command=hyperspec)
        hyperfile.grid(column=1, row=8)
        Label(win, text="Latitude ").grid(row=9, column=0)
        Label(win, text="Longitude").grid(row=10, column=0)
        e1 = Entry(win)
        e2 = Entry(win)
        e1.grid(row=9, column=1)
        e2.grid(row=10, column=1)
        submit = Button(win, text="Submit", command=submit)
        submit.grid(column=0, row=11)
        win.mainloop()


k = Gills()
print("Processing.....\n")
b1 = Image.open(k.layer1)
b2 = Image.open(k.layer2)
b3 = Image.open(k.layer3)
b4 = Image.open(k.layer4)
b5 = Image.open(k.layer5)
b6 = Image.open(k.layer6)
b7 = Image.open(k.layer7)
b8 = Image.open(k.layer8)
b9 = Image.open(k.layer10)
b8a = Image.open(k.layer9)
b10 = Image.open(k.layer11)
b11 = Image.open(k.layer12)
b12 = Image.open(k.layer13)
b1arr = numpy.array(b1)
b2arr = numpy.array(b2)
b3arr = numpy.array(b3)
b4arr = numpy.array(b4)
b5arr = numpy.array(b5)
b6arr = numpy.array(b6)
b7arr = numpy.array(b7)
b8arr = numpy.array(b8)
b8aarr = numpy.array(b8a)
b9arr = numpy.array(b9)
b10arr = numpy.array(b10)
b11arr = numpy.array(b11)
b12arr = numpy.array(b12)
# Hyper Spectral
ar = tifffile.imread(k.hyper)
# Functions


def get_rad(ar, x, y):
    temp = []
    temp.append(ar[x][y])
    temp.append(ar[x + 1][y])
    temp.append(ar[x + 1][y + 1])
    temp.append(ar[x + 1][y - 1])
    temp.append(ar[x][y + 1])
    temp.append(ar[x][y - 1])
    temp.append(ar[x - 1][y])
    temp.append(ar[x - 1][y - 1])
    temp.append(ar[x - 1][y + 1])
    return sum(temp) / len(temp)


def giveModel(x):
    x_axis = [443, 490, 560, 665, 705, 740, 783, 842, 865, 945, 1375, 1610, 2190]
    x_axis.pop(9)
    x_axis.pop(8)
    x_axis.pop(0)
    train_x = numpy.array(x).reshape(-1, 1)
    LinReg = LinearRegression()
    LinRegModel = LinReg.fit(train_x, x_axis)
    return LinRegModel


def get_array(x, y):
    temp = []
    temp.append(get_rad(b2arr, x, y))
    temp.append(get_rad(b3arr, x, y))
    temp.append(get_rad(b4arr, x, y))
    temp.append(get_rad(b5arr, x, y))
    temp.append(get_rad(b6arr, x, y))
    temp.append(get_rad(b7arr, x, y))
    temp.append(get_rad(b8arr, x, y))
    temp.append(get_rad(b8aarr, x, y))
    temp.append(get_rad(b11arr, x, y))
    temp.append(get_rad(b12arr, x, y))
    return temp


def new_array(y):
    temp = []
    model = giveModel(y)
    temp.append(model.predict(442))
    temp.append(model.predict(489))
    temp.append(model.predict(530))
    temp.append(model.predict(551))
    temp.append(model.predict(570))
    temp.append(model.predict(631))
    temp.append(model.predict(672))
    temp.append(model.predict(683))
    temp.append(model.predict(697))
    temp.append(model.predict(703))
    temp.append(model.predict(709))
    temp.append(model.predict(716))
    temp.append(model.predict(722))
    temp.append(model.predict(728))
    temp.append(model.predict(735))
    temp.append(model.predict(742))
    temp.append(model.predict(748))
    temp.append(model.predict(755))
    temp.append(model.predict(762))
    temp.append(model.predict(770))
    temp.append(model.predict(792))
    temp.append(model.predict(800))
    temp.append(model.predict(872))
    temp.append(model.predict(886))
    temp.append(model.predict(895))
    temp.append(model.predict(905))
    temp.append(model.predict(915))
    temp.append(model.predict(925))
    temp.append(model.predict(940))
    temp.append(model.predict(955))
    temp.append(model.predict(965))
    temp.append(model.predict(976))
    temp.append(model.predict(997))
    temp.append(model.predict(1019))
    temp.append(model.predict(1050))
    return temp


def perfect_array(arr):
    temp = []
    for i in range(len(arr)):
        temp.append(arr[i][0])
    return temp


def main():
    # Multi Spectral Images


    # Each Long lat in multi spectral
    eachx = (18.9827755 - 17.9777917962) / (b1arr.shape[0])
    eachy = (83.9418097928 - 82.885487935) / (b1arr.shape[1])

    # Getting the square of area
    x1 = (18.2824 - 17.9778) / eachx
    y1 = (83.0410 - 82.885487) / eachy
    x2 = (18.4172 - 17.9778) / eachx
    y2 = (83.1799 - 82.885487) / eachy

    # Approximating using basic arith
    x1 = int(x1 + 0.5)
    y1 = int(y1 + 0.5)
    x2 = int(x2 + 0.5)
    y2 = int(y2 + 0.5)

    # Each long,lat in hyper spectral
    eachhyx = (18.4172 - 18.2824) / (ar.shape[0])
    eachhyy = (-1) * (83.0410 - 83.1799) / (ar.shape[1])

    stepx = eachx/eachhyx
    stepy = eachy/eachhyy

    finalimg1 = numpy.zeros([735, 723])
    finalimg2 = numpy.zeros([735, 723])
    finalimg3 = numpy.zeros([735, 723])
    finalimg4 = numpy.zeros([735, 723])
    finalimg5 = numpy.zeros([735, 723])
    finalimg6 = numpy.zeros([735, 723])
    finalimg7 = numpy.zeros([735, 723])
    finalimg8 = numpy.zeros([735, 723])
    finalimg9 = numpy.zeros([735, 723])
    finalimg10 = numpy.zeros([735, 723])
    finalimg11 = numpy.zeros([735, 723])
    finalimg12 = numpy.zeros([735, 723])
    finalimg13 = numpy.zeros([735, 723])
    finalimg14 = numpy.zeros([735, 723])
    finalimg15 = numpy.zeros([735, 723])
    finalimg16 = numpy.zeros([735, 723])
    finalimg17 = numpy.zeros([735, 723])
    finalimg18 = numpy.zeros([735, 723])
    finalimg19 = numpy.zeros([735, 723])
    finalimg20 = numpy.zeros([735, 723])
    finalimg21 = numpy.zeros([735, 723])
    finalimg22 = numpy.zeros([735, 723])
    finalimg23 = numpy.zeros([735, 723])
    finalimg24 = numpy.zeros([735, 723])
    finalimg25 = numpy.zeros([735, 723])
    finalimg26 = numpy.zeros([735, 723])
    finalimg27 = numpy.zeros([735, 723])
    finalimg28 = numpy.zeros([735, 723])
    finalimg29 = numpy.zeros([735, 723])
    finalimg30 = numpy.zeros([735, 723])
    finalimg31 = numpy.zeros([735, 723])
    finalimg32 = numpy.zeros([735, 723])
    finalimg33 = numpy.zeros([735, 723])
    finalimg34 = numpy.zeros([735, 723])
    finalimg35 = numpy.zeros([735, 723])
    final = []
    for i in range(x1, x1 + (x2 - x1) * int(stepx)):
        for j in range(y1, y1 + (y2 - y1) * int(stepy)):
            final.append(perfect_array(new_array(get_array(i, j))))

    ii = 0
    finalimg = numpy.zeros([735, 723, 35])
    for i in range(735):
        for j in range(723):
            finalimg[i][j] = final[ii]
            ii = ii + 1
    tifffile.imsave("Outputs/output.tif", finalimg)
    print("Done Hyper")
    # Converting to individual layers
    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg1[i][j] = final[ii][0]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg2[i][j] = final[ii][1]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg3[i][j] = final[ii][2]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg4[i][j] = final[ii][3]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg5[i][j] = final[ii][4]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg6[i][j] = final[ii][5]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg7[i][j] = final[ii][6]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg8[i][j] = final[ii][7]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg9[i][j] = final[ii][8]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg10[i][j] = final[ii][9]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg11[i][j] = final[ii][10]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg12[i][j] = final[ii][11]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg13[i][j] = final[ii][12]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg14[i][j] = final[ii][13]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg15[i][j] = final[ii][14]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg16[i][j] = final[ii][15]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg17[i][j] = final[ii][16]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg18[i][j] = final[ii][17]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg19[i][j] = final[ii][18]
            ii = ii + 1

            ii = 0
    for i in range(735):
        for j in range(723):
            finalimg20[i][j] = final[ii][19]
            ii = ii + 1

    ii = 0
    print("Over here")
    for i in range(735):
        for j in range(723):
            finalimg21[i][j] = final[ii][20]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg22[i][j] = final[ii][20 + 1]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg23[i][j] = final[ii][20 + 1 + 1]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg24[i][j] = final[ii][23]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg25[i][j] = final[ii][24]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg26[i][j] = final[ii][25]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg27[i][j] = final[ii][26]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg28[i][j] = final[ii][27]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg29[i][j] = final[ii][28]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg30[i][j] = final[ii][29]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg31[i][j] = final[ii][30]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg32[i][j] = final[ii][31]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg33[i][j] = final[ii][32]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg34[i][j] = final[ii][33]
            ii = ii + 1

    ii = 0
    for i in range(735):
        for j in range(723):
            finalimg35[i][j] = final[ii][34]
            ii = ii + 1

    tifffile.imsave("Outputs/layer1.tif", finalimg1)
    tifffile.imsave("Outputs/layer2.tif", finalimg2)
    tifffile.imsave("Outputs/layer3.tif", finalimg3)
    tifffile.imsave("Outputs/layer4.tif", finalimg4)
    tifffile.imsave("Outputs/layer5.tif", finalimg5)
    tifffile.imsave("Outputs/layer6.tif", finalimg6)
    tifffile.imsave("Outputs/layer7.tif", finalimg7)
    tifffile.imsave("Outputs/layer8.tif", finalimg8)
    tifffile.imsave("Outputs/layer9.tif", finalimg9)
    tifffile.imsave("Outputs/layer10.tif", finalimg10)
    tifffile.imsave("Outputs/layer11.tif", finalimg11)
    tifffile.imsave("Outputs/layer12.tif", finalimg12)
    tifffile.imsave("Outputs/layer13.tif", finalimg13)
    tifffile.imsave("Outputs/layer14.tif", finalimg14)
    tifffile.imsave("Outputs/layer15.tif", finalimg15)
    tifffile.imsave("Outputs/layer16.tif", finalimg16)
    tifffile.imsave("Outputs/layer17.tif", finalimg17)
    tifffile.imsave("Outputs/layer18.tif", finalimg18)
    tifffile.imsave("Outputs/layer19.tif", finalimg19)
    tifffile.imsave("Outputs/layer20.tif", finalimg20)
    tifffile.imsave("Outputs/layer21.tif", finalimg21)
    tifffile.imsave("Outputs/layer22.tif", finalimg22)
    tifffile.imsave("Outputs/layer23.tif", finalimg23)
    tifffile.imsave("Outputs/layer24.tif", finalimg24)
    tifffile.imsave("Outputs/layer25.tif", finalimg25)
    tifffile.imsave("Outputs/layer26.tif", finalimg26)
    tifffile.imsave("Outputs/layer27.tif", finalimg27)
    tifffile.imsave("Outputs/layer28.tif", finalimg28)
    tifffile.imsave("Outputs/layer29.tif", finalimg29)
    tifffile.imsave("Outputs/layer30.tif", finalimg30)
    tifffile.imsave("Outputs/layer31.tif", finalimg31)
    tifffile.imsave("Outputs/layer32.tif", finalimg32)
    tifffile.imsave("Outputs/layer33.tif", finalimg33)
    tifffile.imsave("Outputs/layer34.tif", finalimg34)
    tifffile.imsave("Outputs/layer35.tif", finalimg35)


main()
print("The hyperspectral image is successfully build")



