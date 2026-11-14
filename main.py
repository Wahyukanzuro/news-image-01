import base64
import os

# news-image-01 v2 entry program: decode the bundled image and write it out.
# The image lives in image.b64 next to this file. The program is offline
# and deterministic: the same bytes are written on every run.


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "image.b64")
    if not os.path.exists(path):
        path = os.path.join(os.getcwd(), "image.b64")
    with open(path, "r", encoding="ascii") as fh:
        data = base64.b64decode(fh.read().strip())
    if not data.startswith(b"\xff\xd8\xff"):
        raise SystemExit("image.b64 is not a JPEG")
    if len(data) > 1048576:
        raise SystemExit("image over 1 MiB")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    with open(os.path.join(out_dir, "entry.png"), "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
