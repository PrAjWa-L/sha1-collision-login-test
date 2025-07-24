# 🔐 SHA-1 Collision Login Test (CTF Script)

This script demonstrates a real-world application of a **SHA-1 hash collision** to bypass a vulnerable login mechanism. It was written for educational purposes, specifically in the context of a [picoCTF](https://picoctf.org) challenge.

## 🧠 Background

SHA-1 is a cryptographic hash function that has been broken. In 2017, researchers from Google and CWI Amsterdam created two distinct PDF files that result in the **same SHA-1 hash** — a collision.

This script uses those two PDFs:
- [shattered-1.pdf](https://shattered.io/static/shattered-1.pdf)
- [shattered-2.pdf](https://shattered.io/static/shattered-2.pdf)

...to exploit a login form that relies on weak hash-based comparison (e.g., comparing `sha1(username)` to `sha1(password)`).

## 🚀 How It Works

1. The script downloads the two PDFs.
2. It sends them as the `username` and `pwd` in a POST request to a target login form.
3. If the server checks hashes (rather than actual values), the login may be accepted due to the SHA-1 collision.

## 📜 Requirements

- Python 3.x
- `requests` module (install via `pip install requests`)

## 💻 Usage

```bash
python3 solve.py
```
# ⚠️ Disclaimer
This script is for educational and ethical hacking purposes only.

Do not use this on systems you do not own or have explicit permission to test. Unauthorized use is illegal and unethical.

## 📚 References
SHA-1 Collision Demo (SHAttered)
picoCTF.org
GitHub: shattered PDFs
