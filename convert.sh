python ffmpeg-split.py -f videos/HV\ Disc\ 1d.m4v -m HV\ Disc\ 1d.csv -v hevc -e "-tag:v hvc1" && 
python ffmpeg-split.py -f videos/HV\ Disc\ 2a.m4v -m HV\ Disc\ 2a.csv -v hevc -e "-tag:v hvc1" && 
python ffmpeg-split.py -f videos/HV\ Disc\ 2b.m4v -m HV\ Disc\ 2b.csv -v hevc -e "-tag:v hvc1" && 
python ffmpeg-split.py -f videos/Xmas\ 95.m4v -m Xmas\ 95.csv -v hevc -e "-tag:v hvc1" && 
python ffmpeg-split.py -f videos/Misc.\ Max\ Winter\ 95-96.m4v -m Misc.\ Max\ Winter\ 95-96.csv -v hevc -e "-tag:v hvc1"