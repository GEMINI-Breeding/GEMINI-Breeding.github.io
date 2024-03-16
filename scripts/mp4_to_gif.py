from moviepy.editor import VideoFileClip
import os

if __name__ == '__main__':
    video_file_path = "/Users/lion397/codes/GEMINI/GEMINI-Breeding.github.io/scripts/Screen Recording 2024-03-15 at 1.43.10 PM.mov"
    # get file name only
    file_name = video_file_path.split("/")[-1]
    # Get directory path
    directory_path = video_file_path.replace(file_name, "")

    # get file name without extension
    file_name = file_name.split(".")[0]
    
    videoClip = VideoFileClip(video_file_path)

    gif_file_path = os.path.join(directory_path,file_name+".gif")

    # Write the gif file by skipping 10 frames
    videoClip.write_gif(gif_file_path, fps=10)