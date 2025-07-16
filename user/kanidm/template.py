pkgname = "kanidm"
pkgver = "1.6.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "linux-pam-devel",
    "udev-devel",
    "openssl3-devel",
    "sqlite-devel",
    "rust-std",
]
pkgdesc = "Modern and simple identity management platform written in rust"
license = "MPL-2.0"
url = "https://kanidm.com"
source = f"https://github.com/kanidm/kanidm/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4165a2762d5f5f6db5da34f084788f720d8f225dcbe35e00b650cefb6283bbd3"
