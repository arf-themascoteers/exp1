import os
import sat_utils

src = "D:/Dataset/Sentinel/S2"
out = r'data/out/sat'

for file in os.listdir(src):
    path = os.path.join(src, file)

    tokens = file.split("_")
    last = tokens[-1]
    tokens = last.split(".")
    first = tokens[0]
    number_str = first[1:]
    number_int = int(number_str)
    dest = os.path.join(out, str(number_int)+".jp2")
    sat_utils.crop_jp2(path, dest, 142.15147294609447, -36.158194444674116,
                143.21430555608072, -36.92885610612682)
    print(f"Done {file}")
print("Done")

