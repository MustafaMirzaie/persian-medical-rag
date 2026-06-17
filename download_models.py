# دانلود مدل‌های لوکال از میرر HuggingFace (قابل ادامه پس از قطعی)
# import os
# os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"  # میرر برای ایران

from huggingface_hub import snapshot_download

JOBS = [
    ("sentence-transformers/clip-ViT-B-32", "models/clip-ViT-B-32",
     ["*.onnx", "onnx/*", "*.h5", "*.ot", "*.msgpack"]),
]

for repo_id, local_dir, ignores in JOBS:
    print(f"--- downloading {repo_id} ---")
    snapshot_download(repo_id=repo_id, local_dir=local_dir,
                      ignore_patterns=ignores, max_workers=4)
    print(f"OK -> {local_dir}")