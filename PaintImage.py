import colorsys


def hsv_to_rgb(h, s, v):
    if s == 0.0: v *= 255; return (v, v, v)
    i = int(h * 6.)  # XXX assume int() truncates!
    f = (h * 6.) - i;
    p, q, t = int(255 * (v * (1. - s))), int(255 * (v * (1. - s * f))), int(255 * (v * (1. - s * (1. - f))));
    v *= 255;
    i %= 6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)

def paint_grad(image, queue, saveName):
    l = len(queue) - 1
    incr = 360 / l

    curG = 0.0
    curR = 255.0

    pix = image.load()
    for i in queue:
        color = (int(curR), int(curG), int(0.0))
        pix[i[0], i[1]] = color
        curR -= incr
        curG += incr

    image.save(saveName)

def paint_rainbow(image, queue, saveName):
    l = len(queue) - 1
    incr = 360 / l
    h = 0.0

    pix = image.load()
    for i in queue:

        h += incr
        color = hsv_to_rgb(int(h) / 360, 1, 1)

        pix[i[0], i[1]] = color

    image.save(saveName)

