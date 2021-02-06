python3 -c 'import sys;print("\n".join(" ".join(l) for l in zip(*list(map(str.split, sys.stdin)))))' < file.txt
