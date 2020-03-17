import cv2


def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

def sketch(img, saveIn, show=False):

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_gray = cv2.resize(img_gray, (600, 400 ))
    img_inv = 255 - img_gray
    img_blur = cv2.GaussianBlur(img_inv, ksize = (91,91), sigmaX = 0, sigmaY = 0)
    img_blend = dodgeV2(img_gray, img_blur)

    cv2.imwrite(saveIn, img_blend)
    
    if show == True:
        cv2.imshow("frame",img_blend)
        cv2.destroyAllWindows()
        
        
  
