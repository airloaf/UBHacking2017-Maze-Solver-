def paint(image, queue, saveName):
    # Red to blue
    l = len(queue) - 1
    dif = 255.0 / l
    curR = 255.0
    curB = 0.0

    pix = image.load()
    for i in queue:
        pix[i[0], i[1]] = (int(curR), 0, int(curB))
        curR -= dif
        curB += dif

        print(str(curR) + " " + str(curB))

    image.save(saveName)

