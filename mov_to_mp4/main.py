import os
from moviepy.editor import VideoFileClip
from tqdm.auto import tqdm

def convert_to_mp4(input_file, output_file):
    try:
        clip = VideoFileClip(input_file)
        clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

        # Delete the original .heic file after successful conversion
        # os.remove(input_file)
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

def main():
    # Replace 'your_custom_folder_path' with the actual path to your folder containing HEIC files
    folder_dir = 'C:/Users/THUY LINH/OneDrive/Documents/PyCharm/mov_to_mp4/mov'
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_directory = os.path.join(script_directory, folder_dir)

    for root, _, files in os.walk(input_directory):
        for file in tqdm(files):
            file_ext = os.path.splitext(file.lower())[1]
            if file_ext == '.mov':
                input_file = os.path.join(root, file)
                output_file = os.path.splitext(input_file)[0] + ".mp4"
                convert_to_mp4(input_file, output_file)

if __name__ == "__main__":
    main()