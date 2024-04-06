# Object detection app using YOLOv8 and Android

## Step 1:
Train yolov8 model on custom dataset and export it in .tflite format.

Check train_export_yolov8_model.ipynb 

## Step 2:
Open android_app folder.

Put your .tflite model and .txt label file inside the assets folder  (android_app\android_app\app\src\main\assets)

Rename paths of your model and labels file in Constants.kt file   (android_app\android_app\app\src\main\java\com\surendramaran\yolov8tflite)

Build and Run



## Credits

This project includes the andrroid app code from the following repository:

- [Original Repository Name](https://github.com/surendramaran/YOLOv8-TfLite-Object-Detector)

Special thanks to [link-to-original-author-profile](https://github.com/surendramaran) for their contribution.
