import random
import json

formats = ['avi', 'mp4', 'mov', 'mkv', 'mp3', 'flac', 'webm', 'wmv']

commands = {
    'simple_conversion': '-i input.{0} output.{1}',
    'codec_conversion': '-i input.{0} -c:v libx264 output.{1}',
    'audio_conversion': '-i input.{0} -vn -ar 44100 -ac 2 -b:a 192k output.{1}',
    'codec_audio_conversion': '-i input.{0} -c:v libvpx -c:a libvorbis output.{1}',
    'resolution_conversion': '-i input.{0} -vf scale=640:480 output.{1}',
    'quality_conversion': '-i input.{0} -q:v 0 output.{1}',
    'frame_rate_conversion': '-i input.{0} -r 30 output.{1}',
    'volume_adjust_conversion': '-i input.{0} -filter:a "volume=0.5" output.{1}',
    'mute_audio_conversion': '-i input.{0} -an output.{1}',
    'extract_audio_conversion': '-i input.{0} -vn output.{1}',
    'convert_to_gif_conversion': '-i input.{0} output.{1}.gif',
    'subtitle_conversion': '-i input.{0} -vf subtitles=input.srt output.{1}',
    'rotate_video_conversion': '-i input.{0} -vf "transpose=1" output.{1}',
    'mirror_video_conversion': '-i input.{0} -vf "hflip" output.{1}',
    'speedup_video_conversion': '-i input.{0} -filter:v "setpts=0.5*PTS" output.{1}',
    'slowdown_video_conversion': '-i input.{0} -filter:v "setpts=2.0*PTS" output.{1}',
}

requests = {
    'simple_conversion': "Please convert the file 'input.{0}' to 'output.{1}' format.",
    'codec_conversion': "Could you transform the file 'input.{0}' into 'output.{1}' format using the H.264 video codec?",
    'audio_conversion': "I would like to change the file 'input.{0}' to 'output.{1}' format with a sample rate of 44.1 kHz, 2 audio channels, and a bitrate of 192 kbit/s, please.",
    'codec_audio_conversion': "Is it possible to convert the file 'input.{0}' into 'output.{1}' format using the VP8 video codec and Vorbis audio codec?",
    'resolution_conversion': "I need to transform the file 'input.{0}' into 'output.{1}' format with a resolution of 640x480, please.",
    'quality_conversion': "Please change the file 'input.{0}' to 'output.{1}' format with the best possible quality.",
    'frame_rate_conversion': "Could you convert the file 'input.{0}' into 'output.{1}' format with a frame rate of 30 fps?",
    'volume_adjust_conversion': "Can you adjust the volume of the file 'input.{0}' to 50% in the 'output.{1}' format?",
    'mute_audio_conversion': "Please convert the file 'input.{0}' to 'output.{1}' format without any audio.",
    'extract_audio_conversion': "Can you extract the audio from the file 'input.{0}' and save it in 'output.{1}' format?",
    'convert_to_gif_conversion': "Please convert the video in 'input.{0}' to a gif.",
    'subtitle_conversion': "Could you add the subtitles from 'input.srt' to the file 'input.{0}' and save it as 'output.{1}'?",
    'rotate_video_conversion': "Can you rotate the video in 'input.{0}' by 90 degrees clockwise and save it as 'output.{1}'?",
    'mirror_video_conversion': "Can you mirror the video in 'input.{0}' and save the result in 'output.{1}' format?",
    'speedup_video_conversion': "Can you speed up the video in 'input.{0}' by twice the original speed and save it in 'output.{1}' format?",
    'slowdown_video_conversion': "Can you slow down the video in 'input.{0}' by half the original speed and save it in 'output.{1}' format?",
}

data = []

for _ in range(100000):  # Generate 10000 commands and requests
    in_format, out_format = random.sample(formats, 2)  # Pick two random different formats
    command_type = random.choice(list(commands.keys()))  # Pick a random command type
    
    command = f"ffmpeg {commands[command_type].format(in_format, out_format)}"
    request = requests[command_type].format(in_format, out_format)

    data.append({"command": command, "request": request})

# Save all commands and requests in a json file
with open('commands.json', 'w') as file:
    json.dump(data, file, indent=4)
