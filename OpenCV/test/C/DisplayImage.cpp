/*==============================================*/
/* Auther:   Willy Xie                          */
/* Filename: DisplayImage.cpp                   */
/* Version:  1.0                                */
/*==============================================*/
/* Description:                                 */
/* An example of using opencv to read and       */
/* display image.                               */
/*==============================================*/

// Reference : https://blog.gtwang.org/programming/ubuntu-linux-install-opencv-cpp-python-hello-world-tutorial/

#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;

int main(int argc, char* argv[]) {
  // Check for existence of the input image
  if ( argc != 2 ) {
    printf("usage: DisplayImage.out <Image_Path>n");
    return -1;
  }

  // Read the frame
  Mat image;
  image = imread( argv[1], 1 );

  // Check whether the image is loaded properly
  if ( !image.data ) {
    printf("No image data n");
    return -1;
  }

  // Display the image until any keyboard interrupt is received
  namedWindow("Display Image", WINDOW_AUTOSIZE);
  imshow("Display Image", image);
  waitKey(0);

  return 0;
}
