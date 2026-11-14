import base64
import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    b64_path = os.path.join(script_dir, "image.b64")
    if not os.path.isfile(b64_path):
        b64_path = os.path.join(os.getcwd(), "image.b64")
    if not os.path.isfile(b64_path):
        raise SystemExit("image.b64 not found next to main.py or in the cwd")
    with open(b64_path) as fh:
        data = fh.read().strip()
    raw = base64.b64decode(data)
    if raw[:2] != b"\xff\xd8":
        raise SystemExit("image.b64 is not a JPEG")
    if len(raw) > 1024 * 1024:
        raise SystemExit("image exceeds 1 MiB")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as fh:
        fh.write(raw)


if __name__ == "__main__":
    main()
