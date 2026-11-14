import base64
import os


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    with open("image.b64") as fh:
        data = fh.read().strip()
    raw = base64.b64decode(data)
    if raw[:2] != b"\xff\xd8":
        raise SystemExit("image.b64 is not a JPEG")
    if len(raw) > 1024 * 1024:
        raise SystemExit("image exceeds 1 MiB")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as fh:
        fh.write(raw)


if __name__ == "__main__":
    main()
