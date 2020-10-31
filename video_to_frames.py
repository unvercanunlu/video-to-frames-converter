# imports
from argparse import ArgumentParser
from os import path, makedirs

import cv2 as cv


# main function
def main():
    # settings
    argument_parser = ArgumentParser()

    # arguments
    argument_parser.add_argument('-i', '--input',
                                 type=str,
                                 default='video.avi',
                                 help='path to video file')
    argument_parser.add_argument('-o', '--output',
                                 type=str,
                                 default='frames',
                                 help='path to output frames directory')
    argument_parser.add_argument('-p', '--prefix',
                                 type=str,
                                 default='frame',
                                 help='frame prefix')
    argument_parser.add_argument('-f', '--format',
                                 type=str,
                                 default='jpg',
                                 help='frame as image format')

    # arguments
    arguments = argument_parser.parse_args()

    # parameters
    frames_directory = arguments.output
    prefix = arguments.prefix
    video = arguments.input
    format = arguments.format

    # check frame directory exists
    if not path.exists(frames_directory):
        print("{output} directory does not exist.".format(output=frames_directory))
        makedirs(frames_directory)
        print("{output} directory is created.".format(output=frames_directory))

    # capture video
    print("Converting of video {input} to frames is started.".format(input=video))
    video_capture = cv.VideoCapture(video)

    # read frame
    print("{input} is reading.".format(input=video))
    success, frame = video_capture.read()

    # loop
    frame_count = 0
    while success:
        # save frame as image
        frame_file_name = "{prefix}{frame_count}.{format}".format(prefix=prefix,
                                                                  frame_count=frame_count,
                                                                  format=format)
        frame_path = path.join(frames_directory, frame_file_name)
        cv.imwrite(frame_path, frame)
        print("{frame_path} is saved.".format(frame_path=frame_path))

        # read next frame
        success, frame = video_capture.read()
        frame_count += 1

    print("Converting of video {input} to frames is finished.".format(input=video))


# main
if __name__ == '__main__':
    main()
