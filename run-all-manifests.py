with open('convert.sh', 'w') as file:
    output = []
    for manifest in ['HV\\ Disc\\ 1d','HV\\ Disc\\ 2a','HV\\ Disc\\ 2b', 'Xmas\\ 95', 'Misc.\\ Max\\ Winter\\ 95-96']:
        output += [' '.join(['python', 'ffmpeg-split.py', 
            '-f', f'videos/{manifest+".m4v"}', 
            '-m', f'{manifest+".csv"}', 
            '-v', 'hevc', 
            '-e', '"-tag:v hvc1"'])]
    file.write(' && \n'.join(output))
