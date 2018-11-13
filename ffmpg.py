from ffmpy import FFmpeg
ff = FFmpeg(inputs={'movie.mp4': None}, outputs={"output.png": ['-ss', '00:00:4', '-vframes', '1']})

print(ff.cmd)

# Print result
#ffmpeg -i input.mp4 -vf fps=1 out%d.png

#ff.run()