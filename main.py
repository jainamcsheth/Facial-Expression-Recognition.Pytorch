import face_detection_video
import visualize

def main():
    video_path = './videos/00006.mp4'
    images_path = './images/annotated_images/'

    face_detection_video.face_detection(video_path)
    visualize.emotion_detection(images_path)

if __name__ == "__main__":
    main()
